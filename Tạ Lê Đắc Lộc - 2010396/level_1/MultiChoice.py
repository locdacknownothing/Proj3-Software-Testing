import unittest
import pandas as pd
import time
from Utils import *

class MultiChoiceUtils(Utils):
    def __init__(self):
        super().__init__("Data.xlsx", "MultiChoice")
    
    def createQuizIfNotExists(self): # if exists just click
        self.driver.get("https://sandbox.moodledemo.net/course/view.php?id=2")
        
        isQuizExist = True
        try:
            self.driver.find_element(By.PARTIAL_LINK_TEXT, "Black-box testing")
        except NoSuchElementException:
            isQuizExist = False

        if isQuizExist: return
        
        edit_mode = self.driver.find_element(By.CLASS_NAME, "custom-control-input")
        if not edit_mode.is_selected():
            edit_mode.click()

        try:
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='modal-dialog']")))

            skip_tour = self.driver.find_element(By.XPATH,"""//button[text()='Skip tour']""")
            skip_tour.click()
        except TimeoutException: pass
        # continue executing the script if the modal is not found

        wait = WebDriverWait(self.driver, 5)
        add_activity = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "activity-add-text")))
        add_activity.click()

        add_quiz = self.driver.get("https://sandbox.moodledemo.net/course/modedit.php?add=quiz&type&course=2&section=0&return=0&sr=0&beforemod=0")
        quiz_name = self.driver.find_element(By.ID, "id_name")
        quiz_name.clear()
        quiz_name.send_keys("Black-box testing")

        save_quiz = self.driver.find_element(By.ID, "id_submitbutton2")
        save_quiz.click()

        print("Create quiz success")
        
    def createMultiChoice(self):
        # self.driver.get("https://sandbox.moodledemo.net/course/view.php?id=2")
        quiz = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Black-box testing")
        quiz.click()

        questions = self.driver.find_element(By.XPATH, """//a[contains(text(), 'Questions')]""")
        questions.click()

        add_question = self.driver.find_element(By.CSS_SELECTOR, "#action-menu-toggle-1")
        add_question.click()

        # wait = WebDriverWait(self.driver, 5)
        # add_question = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#action-menu-toggle-1")))
        # add_question.click()

        new_question = self.driver.find_element(By.ID, "actionmenuaction-1")
        new_question.click()

        multichoice = self.driver.find_element(By.ID, "item_qtype_multichoice")
        multichoice.click()

        add_multichoice = self.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Add']")
        add_multichoice.click()
        print("Create multichoice success")

        # return self.driver.current_url

    def setNameAndText(self):
        question_name = self.driver.find_element(By.ID, "id_name")
        question_name.send_keys("Introduction")

        self._textToIframe_("id_questiontext_ifr", "What is Black-box testing?")

    def setChoice(self, number, text, grade):
        # choice_text
        if text:
            id = f"id_answer_{number-1}_ifr"
            self._textToIframe_(id, text)

        if grade != 0:
            choice_grade = self.driver.find_element(By.ID, f"id_fraction_{number-1}")  
            grade_select = Select(choice_grade)
            grade_select.select_by_value("{}".format(grade/100))

        print("Set choice {} success".format(number))

    def saveChanges(self):
        save_changes = self.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Save changes']")
        save_changes.click()
        print("Save success")
    
    def isSuccess(self):
        questions_url = "https://sandbox.moodledemo.net/mod/quiz/edit.php"
        curr_url = self.driver.current_url

        return questions_url in curr_url
    
    def isError(self, choice_number, at, error_message):
        error = None
        if at == 0:
            at = "answer"
        else:
            at = "fraction"

        try:
            error = self.driver.find_element(By.ID, f"id_error_{at}_{choice_number-1}")
        except NoSuchElementException:
            return False
        
        # print('Error:', error.text)

        if error_message in error.text:
            return True
        
        return False

class MultiChoiceTestCase(MultiChoiceUtils):
    def setUp(self):
        # self.data = self.getData()
        self.logIn()
        self.createQuizIfNotExists()
        self.createMultiChoice()
        self.setNameAndText()

    def test(self):
        # print(self.data)
        num_testcases = len(set([d['Testcase'] for d in self.data]))
        for i in range(1, num_testcases + 1):
            print('-----------Run testcase', i, '----------')
            self.setUp()

            choices = [choice for choice in self.data if choice['Testcase'] == i]
            expected = []

            for choice in choices:
                # print(choice)
                if not choice['Text']:
                    choice["Text"] = None

                if choice['Expected']:
                    if choice['Expected'] == 'Success':
                        expected += [choice['Expected']]
                    else:
                        # handle \n in string
                        slash = choice['Expected'].find('\n')
                        if slash != -1:
                            # print("Has new line in string")
                            choice['Expected'] = choice['Expected'][:slash]
                            # + '\n' + choice['Expected'][slash+1:]

                        errorAt = {"One of the choices should be 100%, so that it is": 1, 
                                   "This type of question requires at least 2 choices": 0, 
                                   "Grade set, but the Answer is blank": 1}
                        expected += [(choice['Number'], errorAt[choice['Expected']], choice['Expected'])]

                self.setChoice(choice['Number'], choice['Text'], choice['Grade'])

            self.saveChanges()
            if not expected:
                expected = False
            elif expected[0] == 'Success':
                expected = self.isSuccess()
            else:
                expected = [self.isError(expect[0], expect[1], expect[2]) for expect in expected]
                expected = all(expected)

            self.driver.quit()
            print(f"Testcase {i}: {'PASSED' if expected else 'FAILED'}")

testcases = MultiChoiceTestCase()
testcases.test()
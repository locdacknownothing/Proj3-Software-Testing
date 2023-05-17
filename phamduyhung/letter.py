import unittest
from utils import *

class EditLetterUtils(Utils):
    def init(self):
        super().init()
        self.error_id = ["id_error_firstname", "id_error_lastname", "id_error_email"]
        self.error_message = ["Missing given name", "Missing last name", "Required", "Invalid email address"]

    def getEditLetter(self):
        # Navigate to Site administration
        site_administration_menu = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Site administration")
        site_administration_menu.click()

        # Navigate to Grade
        grade_menu = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Grades")
        grade_menu.click()

        # Navigate to Letter
        wait = WebDriverWait(self.driver, 2)
        letter_navigation = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Letter")))
        letter_navigation.click()

        # Click "Edit" button
        wait = WebDriverWait(self.driver, 2)
        edit_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Edit"]')))
        edit_button.click()   

        print("Navigate to edit letter screen success")

    def setGradePoint(self, index, value):
        grade_point_id = 'id_gradeboundary_{x}'.format(x=index)
        print("grade_point_id: " + grade_point_id)
        grade_point = self.driver.find_element(By.ID, grade_point_id)
        grade_point.clear()
        grade_point.send_keys(value)

    def setGradeLetter(self, index, value):
        grade_letter_id = 'id_gradeletter_{x}'.format(x = index)
        print(grade_letter_id)
        grade_letter = self.driver.find_element(By.ID, grade_letter_id)
        grade_letter.clear()
        grade_letter.send_keys(value)

    def clickSave(self):
        save_change_button = self.driver.find_element(By.ID, "id_submitbutton")
        save_change_button.click()

    def isError(self, at, error_idx):
        error = None
        try:
            error = self.driver.find_element(By.ID, self.error_id[at])        
        except NoSuchElementException:
            return False
        
        print(error.text)
        return self.error_message[error_idx] in error.text
    
    def isSuccess(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            cont = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Edit"]')))
        except TimeoutException:
            return False

        cont.click()
        return True
    
class EditLetterTestCase(unittest.TestCase, EditLetterUtils):
    def setUp(self):
        self.init()
        self.logIn()
        self.getEditLetter()

    def testcase_001_001(self):
        self.setGradeLetter(0, 'A')
        self.setGradePoint(0, 50)
        
        self.setGradeLetter(1, 'B')
        self.setGradePoint(1, 0)

        self.clickSave()
        
        expected = self.isSuccess()
        self.driver.close()
        assert expected

    def testcase_001_002(self):
        self.setGradeLetter(0, 'A')
        self.setGradePoint(0, 50)

        self.setGradeLetter(1, 'B')
        self.setGradePoint(1, 1)

        self.clickSave()
        
        expected = self.isSuccess()
        self.driver.close()
        assert expected

    def testcase_001_003(self):
        self.setGradeLetter(0,'A')
        self.setGradePoint(0, 50)
        
        self.setGradeLetter(1, 'B')
        self.setGradePoint(1, -1)

        self.clickSave()
        
        expected = self.isSuccess()
        self.driver.close()
        assert expected

    def testcase_001_004(self):
        self.setGradeLetter(0,'A')
        self.setGradePoint(0, 50)
        
        self.setGradeLetter(1, 'B')
        self.setGradePoint(1, 100)

        self.clickSave()
        
        expected = self.isSuccess()
        self.driver.close()
        assert expected

    def testcase_001_005(self):
        self.setGradeLetter(0,'A')
        self.setGradePoint(0, 50)
        
        self.setGradeLetter(1, 'B')
        self.setGradePoint(1, 99)

        self.clickSave()
        
        expected = self.isSuccess()
        self.driver.close()
        assert expected

    def testcase_001_006(self):
        self.setGradeLetter(0,'A')
        self.setGradePoint(0, 50)
        
        self.setGradeLetter(1, 'B')
        self.setGradePoint(1, 101)

        self.clickSave()
        
        expected = self.isSuccess()
        self.driver.close()
        assert expected

    def testcase_001_007(self):
        self.setGradeLetter(0,'A')
        self.setGradePoint(0, 50)
        
        self.setGradeLetter(1, 'B')
        self.setGradePoint(1, 25)

        self.clickSave()
        
        expected = self.isSuccess()
        self.driver.close()
        assert expected

    def testcase_001_008(self):
        self.setGradeLetter(0,'A')
        self.setGradePoint(0, 100)
        
        self.setGradeLetter(1, 'B')
        self.setGradePoint(1, 25)

        self.clickSave()
        
        expected = self.isSuccess()
        self.driver.close()
        assert expected

    def testcase_001_009(self):
        self.setGradeLetter(0,'A')
        self.setGradePoint(0, 99)
        
        self.setGradeLetter(1, 'B')
        self.setGradePoint(1, 25)

        self.clickSave()
        
        expected = self.isSuccess()
        self.driver.close()
        assert expected

    def testcase_001_010(self):
        self.setGradeLetter(0,'A')
        self.setGradePoint(0, 101)
        
        self.setGradeLetter(1, 'B')
        self.setGradePoint(1, 25)

        self.clickSave()
        
        expected = self.isSuccess()
        self.driver.close()
        assert expected
unittest.main()

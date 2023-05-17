import unittest
import pandas
from utils import *

class LettersDDT(Utils):
    def init(self):
        super().init()
        self.error_id = ["id_error_firstname", "id_error_lastname", "id_error_email"]
        self.error_message = ["Missing given name", "Missing last name", "Required", "Invalid email address"]
        self.readData()

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
    
    def readData(self):
        filepath = '/data/data.csv'
        pandas.read_csv(filepath)
        print("hello")
        print(pandas)

    def test_valid_value(self):
        self.readData()
        file_path = "/path/to/jpg/image"
        self.driver.get("https://sandbox.moodledemo.net/user/editadvanced.php?id=2")
        self.driver.find_element_by_id("id_userpicture").send_keys(file_path)
        self.driver.find_element_by_id("id_submitbutton").click()
        assert "" in self.driver.page_source



class Test(LettersDDT):
    def init(self):
        super.init()

if __name__ == '__main__':
    unittest.main()
    test = Test()
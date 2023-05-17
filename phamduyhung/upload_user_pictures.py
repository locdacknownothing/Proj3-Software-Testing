import unittest
from utils import *

class UploadUserPictureUtils(Utils):
    def init(self):
        super().init()
        self.error_id = ["id_error_firstname", "id_error_lastname", "id_error_email"]
        self.error_message = ["Missing given name", "Missing last name", "Required", "Invalid email address"]
    
    def getUploadUserPictures(self):
        # Navigate to Site administration
        site_administration_menu = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Site administration")
        site_administration_menu.click()

        # Navigate to Grade
        user_menu = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Users")
        user_menu.click()

        # Navigate to Letter
        wait = WebDriverWait(self.driver, 2)
        upload_user_navigation = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Upload users")))
        upload_user_navigation.click()

        # Click "Choose a file..." button
        wait = WebDriverWait(self.driver, 3)
        choose_file_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Choose a file..."]')))
        choose_file_button.click()

        print("Hê lô woocs")

        wait = WebDriverWait(self.driver, 5)
        upload_a_file_link = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Upload a file")))
        upload_a_file_link.click()

        print("Navigate to upload user pictures screen success")
    
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

class UploadUserPictureTestCase(unittest.TestCase, UploadUserPictureUtils):
    def setUp(self):
        self.init()
        self.logIn()
        self.getUploadUserPictures()

    def testcase_001_001(self):
        print("test 1")

unittest.main()
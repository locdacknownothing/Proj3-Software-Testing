import unittest
import time
from Utils import *

class EditProfileUtils(Utils):
    def getEditProfile(self):
        user_menu = self.driver.find_element(By.ID, "user-menu-toggle")
        user_menu.click()

        profile = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Profile")
        profile.click()

        wait = WebDriverWait(self.driver, 5)
        edit_profile = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Edit profile")))
        edit_profile.click()

        print("Navigate to edit profile success")
    
    def editFirstName(self, text):
        first_name = self.driver.find_element(By.ID, "id_firstname")
        first_name.clear()
        if text:
            first_name.send_keys(text)

    def editLastName(self, text):
        last_name = self.driver.find_element(By.ID, "id_lastname")
        last_name.clear()
        if text:
            last_name.send_keys(text)

    def editEmail(self, text):
        email = self.driver.find_element(By.ID, "id_email")
        email.clear()
        if text:
            email.send_keys(text)
    
    def updateProfile(self):
        save_changes = self.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Update profile']")
        save_changes.click()
        print("Update success")
    
class EditProfileTestCase(unittest.TestCase, EditProfileUtils):
    def setUp(self):
        self.init()
        self.logIn()
        self.getEditProfile()
    
    def test_base(self):
        self.editFirstName("")
        self.editLastName("")
        self.editEmail("")
        self.updateProfile()
        # time.sleep(30)
        self.driver.quit()

unittest.main()
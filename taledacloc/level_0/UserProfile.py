import unittest
import time
from Utils import *

class EditProfileUtils(Utils):
    def init(self):
        super().init()
        self.error_id = ["id_error_firstname", "id_error_lastname", "id_error_email"]
        self.error_message = ["Missing given name", "Missing last name", "Required", "Invalid email address"]

    def getEditProfile(self):
        user_menu = self.driver.find_element(By.ID, "user-menu-toggle")
        user_menu.click()

        profile = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Profile")
        profile.click()

        wait = WebDriverWait(self.driver, 2)
        edit_profile = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Edit profile")))
        edit_profile.click()

        print("Navigate to edit profile success")
    
    def editFirstName(self, text, enter=False):
        first_name = self.driver.find_element(By.ID, "id_firstname")
        first_name.clear()
        if text:
            first_name.send_keys(text)
        
        if enter:
            first_name.send_keys(Keys.ENTER)

    def editLastName(self, text, enter=False):
        last_name = self.driver.find_element(By.ID, "id_lastname")
        last_name.clear()
        if text:
            last_name.send_keys(text)
        
        if enter:
            last_name.send_keys(Keys.ENTER)

    def editEmail(self, text, enter=False):
        email = self.driver.find_element(By.ID, "id_email")
        email.clear()
        if text:
            email.send_keys(text)

        if enter:
            email.send_keys(Keys.ENTER)
    
    def updateProfile(self):
        try:
            wait = WebDriverWait(self.driver, 3)
            save_changes = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='submit' and @value='Update profile']")))
        except TimeoutException:
            return False
        # save_changes = self.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Update profile']")
        save_changes.click()
        print("Update success")

    def isError(self, at, error_idx):
        error = None
        try:
            error = self.driver.find_element(By.ID, self.error_id[at])        
        except NoSuchElementException:
            return False
        
        # print(error.text)
        return self.error_message[error_idx] in error.text
    
    def isSuccess(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            cont = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@type="submit" and contains(text(), "Continue")]')))
        except TimeoutException:
            return False

        cont.click()
        # time.sleep(2)
        profile_url = "https://sandbox.moodledemo.net/user/profile.php"
        preference_url = "https://sandbox.moodledemo.net/user/preferences.php"
        curr_url = self.driver.current_url
        # print(curr_url)
        return (profile_url in curr_url) or (preference_url in curr_url)

    def checkEmailChange(self):
        try:
            wait = WebDriverWait(self.driver, 2)
            cancel = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Cancel email change")))
        except TimeoutException:
            return
        
        cancel.click()
    
class EditProfileTestCase(unittest.TestCase, EditProfileUtils):
    def setUp(self):
        self.init()
        self.logIn()
        self.getEditProfile()
        self.checkEmailChange()
    
    def test_002_001(self):
        self.editFirstName(None)
        self.updateProfile()
        
        expected = self.isError(0, 0)
        self.driver.quit()
        assert expected

    def test_002_002(self):
        self.editFirstName("Terry")
        self.editLastName(None)
        self.updateProfile()
        
        expected = self.isError(1, 1)
        self.driver.quit()
        assert expected

    def test_002_003(self):
        self.editFirstName("Terry")
        self.editLastName("Jom")
        self.editEmail(None)
        self.updateProfile()
        
        expected = self.isError(2, 2)
        self.driver.quit()
        assert expected

    def test_002_004(self):
        self.editFirstName("Terry")
        self.editLastName("Jom")
        self.editEmail("Jom@Terry")
        self.updateProfile()

        expected = self.isError(2, 3)
        self.driver.quit()
        assert expected

    def test_002_005(self):
        self.editFirstName("Terry")
        self.editLastName("Jom")
        self.editEmail("Jom@Terry", True)
        self.updateProfile()
        
        expected = self.isError(2, 3)
        self.driver.quit()
        assert expected

    def test_002_006(self):
        self.editFirstName("Terry")
        self.editLastName("Jom")
        self.editEmail("Jom@Terry.cartoon")
        self.updateProfile()
        
        expected = self.isSuccess()
        # time.sleep(30)
        self.driver.quit()
        assert expected
    
    def test_002_007(self):
        self.editLastName(None)
        self.editFirstName(None)
        self.editEmail("Jom@Terry.cartoon")
        self.updateProfile()
        
        expected = self.isError(0, 0) and self.isError(1, 1)
        # time.sleep(30)
        self.driver.quit()
        assert expected

    def test_002_008(self):
        self.editEmail(None)
        self.editFirstName(None)
        self.updateProfile()
        
        expected = self.isError(0, 0) and self.isError(2, 2)
        self.driver.quit()
        assert expected

    def test_002_009(self):
        self.editEmail("Jom&Teery")
        self.editFirstName(None, True)
        self.updateProfile()
        
        expected = self.isError(0, 0) and self.isError(2, 3)
        self.driver.quit()
        assert expected

    def test_002_010(self):
        self.editLastName(None, True)
        self.editEmail(None, True)
        self.updateProfile()
        
        expected = self.isError(1, 1) and self.isError(2, 2)
        self.driver.quit()
        assert expected

    def test_002_011(self):
        self.editLastName(None)
        self.editEmail("Jom&Teery", True)
        self.updateProfile()
        
        expected = self.isError(1, 1) and self.isError(2, 3)
        self.driver.quit()
        assert expected

    def test_002_012(self):
        self.editFirstName(None, True)
        self.editLastName(None)
        self.editEmail(None, True)
        self.updateProfile()
        
        expected = self.isError(0, 0) and self.isError(1, 1) and self.isError(2, 2)
        self.driver.quit()
        assert expected
    
    def test_002_013(self):
        self.editFirstName(None)
        self.editLastName(None)
        self.editEmail("Jom&Teery", True)
        self.updateProfile()
        
        expected = self.isError(0, 0) and self.isError(1, 1) and self.isError(2, 3)
        self.driver.quit()
        assert expected

    def test_002_014(self):
        self.editEmail("Jom&Teery")
        self.editFirstName(None)
        self.editLastName(None)
        self.updateProfile()
        
        expected = self.isError(0, 0) and self.isError(1, 1) and self.isError(2, 3)
        self.driver.quit()
        assert expected

    def test_002_015(self):
        self.editEmail("Jom&Teery", True)
        self.editFirstName(None, True)
        self.editLastName(None, True)
        self.updateProfile()
        
        expected = self.isError(0, 0) and self.isError(1, 1) and self.isError(2, 3)
        self.driver.quit()
        assert expected

unittest.main()
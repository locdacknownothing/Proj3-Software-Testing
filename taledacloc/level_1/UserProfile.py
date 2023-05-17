import unittest
import pandas as pd
import time
from Utils import *

class EditProfileUtils(Utils):
    def __init__(self):
        super().__init__("Data.xlsx", "EditProfile")
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
    
class EditProfileTestCase(EditProfileUtils):
    def setUp(self):
        self.logIn()
        self.getEditProfile()
        self.checkEmailChange()
    
    def test(self):
        for testcase in self.data:
            print('-----------Run testcase', testcase['Testcase'], '----------')
            # print(self.data[i-1])
            self.setUp()

            execute = str(testcase['Execute'])
            for i in range(len(execute)):
                if execute[i] == '0':
                    continue
                elif execute[i] == '1':
                    if i+1 < len(execute) and execute[i+1] == '0':
                        self.editFirstName(testcase['FirstName'], True)
                    else:
                        self.editFirstName(testcase['FirstName'])
                elif execute[i] == '2':
                    if i+1 < len(execute) and execute[i+1] == '0':
                        self.editLastName(testcase['LastName'], True)
                    else:
                        self.editLastName(testcase['LastName'])
                elif execute[i] == '3':
                    if i+1 < len(execute) and execute[i+1] == '0':
                        self.editEmail(testcase['Email'], True)
                    else:
                        self.editEmail(testcase['Email'])

            self.updateProfile()

            expected = True
            if testcase['Success'] == 1:
                expected = self.isSuccess()
            else:
                if testcase['Error1']:
                    expected = expected and self.isError(0, self.error_message.index(testcase['Error1']))
                if testcase['Error2']:
                    expected = expected and self.isError(1, self.error_message.index(testcase['Error2']))
                if testcase['Error3']:
                    expected = expected and self.isError(2, self.error_message.index(testcase['Error3']))

            self.driver.quit()
            print(f"Testcase {testcase['Testcase']}: {'PASSED' if expected else 'FAILED'}")


testcases = EditProfileTestCase()
testcases.test()
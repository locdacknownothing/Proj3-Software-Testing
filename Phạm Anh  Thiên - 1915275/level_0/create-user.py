import string
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait

# py -m unittest create-user.py


def random_char(char_num):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(char_num))


class TestCreateUser(unittest.TestCase):
    def setUp(self):

        self.browser = webdriver.Chrome(
            ChromeDriverManager().install())

        self.addCleanup(self.browser.quit)
        self.browser.get('https://sandbox.moodledemo.net/login/index.php')
        self.browser.find_element(By.ID, "username").send_keys('manager')
        self.browser.find_element(By.ID, "password").send_keys('sandbox')
        self.browser.find_element(By.ID, "loginbtn").click()
        self.browser.get(
            'https://sandbox.moodledemo.net/user/editadvanced.php?id=-1')

    def testValidCreate(self):
        self.browser.find_element(
            By.ID, "id_username").send_keys(random_char(17))
        self.browser.find_element(
            By.ID, "id_createpassword").click()
        # self.browser.find_element(By.ID, "id_newpassword").send_keys('sandbox')
        self.browser.find_element(By.ID, "id_firstname").send_keys('Thien')
        self.browser.find_element(By.ID, "id_lastname").send_keys('Pham')
        self.browser.find_element(By.ID, "id_email").send_keys(
            random_char(7) + "@hcmut.edu.vn")
        self.browser.find_element(By.ID, "id_submitbutton").click()
        self.assertIn('https://sandbox.moodledemo.net/admin/user.php',
                      self.browser.current_url)

    def testExistUser(self):

        self.browser.find_element(
            By.ID, "id_username").send_keys('admin')
        self.browser.find_element(
            By.ID, "id_createpassword").click()
        # self.browser.find_element(By.ID, "id_newpassword").send_keys('sandbox')
        self.browser.find_element(By.ID, "id_firstname").send_keys('Thien')
        self.browser.find_element(By.ID, "id_lastname").send_keys('Pham')
        self.browser.find_element(By.ID, "id_email").send_keys(
            random_char(7)+"@gmail.com")
        self.browser.find_element(By.ID, "id_submitbutton").click()
        textError = self.browser.find_element(By.ID, "id_error_username").text

        self.assertIn(
            'This username already exists, choose another', textError)

    def testExistEmail(self):
        self.browser.find_element(By.ID, "id_username").send_keys('thien')
        self.browser.find_element(
            By.ID, "id_createpassword").click()
        # self.browser.find_element(By.ID, "id_newpassword").send_keys('sandbox')
        self.browser.find_element(By.ID, "id_firstname").send_keys('Thien')
        self.browser.find_element(By.ID, "id_lastname").send_keys('Pham')
        self.browser.find_element(By.ID, "id_email").send_keys(
            'demo@moodle.a')
        self.browser.find_element(By.ID, "id_submitbutton").click()
        self.assertIn('This email address is already registered',
                      self.browser.page_source)

    def testUsernameIsLowerCase(self):
        self.browser.find_element(By.ID, "id_username").send_keys('DDDDDDDD')
        self.browser.find_element(
            By.ID, "id_createpassword").click()
        # self.browser.find_element(By.ID, "id_newpassword").send_keys('sandbox')
        self.browser.find_element(By.ID, "id_firstname").send_keys('Thien')
        self.browser.find_element(By.ID, "id_lastname").send_keys('Pham')
        self.browser.find_element(By.ID, "id_email").send_keys(
            'demo@moodle.a')
        self.browser.find_element(By.ID, "id_submitbutton").click()
        self.assertIn('Only lowercase letters allowed',
                      self.browser.page_source)

    def testMissingFirstName(self):
        self.browser.find_element(By.ID, "id_username").send_keys('DDDDDDDD')
        self.browser.find_element(
            By.ID, "id_createpassword").click()
        # self.browser.find_element(By.ID, "id_newpassword").send_keys('sandbox')

        self.browser.find_element(By.ID, "id_lastname").send_keys('Pham')
        self.browser.find_element(By.ID, "id_email").send_keys(
            'demo@moodle.a')
        self.browser.find_element(By.ID, "id_submitbutton").click()
        self.assertIn('Missing given name',
                      self.browser.page_source)

    def testMissingLastName(self):
        self.browser.find_element(By.ID, "id_username").send_keys('DDDDDDDD')
        self.browser.find_element(
            By.ID, "id_createpassword").click()

        self.browser.find_element(By.ID, "id_email").send_keys(
            'demo@moodle.a')
        self.browser.find_element(By.ID, "id_submitbutton").click()
        self.assertIn('Missing last name',
                      self.browser.page_source)


if __name__ == '__main__':
    unittest.main(verbosity=2)

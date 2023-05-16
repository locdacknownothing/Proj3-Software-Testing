import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# py -m unittest login.py


class TestPageLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.addCleanup(self.browser.quit)
        self.browser.get('https://sandbox.moodledemo.net/login/index.php')

    def testInvalidPassword(self):
        self.browser.find_element(By.ID, "username").send_keys('admin')
        self.browser.find_element(By.ID, "password").send_keys('sandbox123')
        self.browser.find_element(By.ID, "loginbtn").click()
        self.assertIn('Invalid login, please try again',
                      self.browser.page_source)

    def testInvalidUsername(self):
        self.browser.find_element(By.ID, "username").send_keys('admin123')
        self.browser.find_element(By.ID, "password").send_keys('sandbox')
        self.browser.find_element(By.ID, "loginbtn").click()
        self.assertIn('Invalid login, please try again',
                      self.browser.page_source)

    def testValidLogin(self):
        self.browser.find_element(By.ID, "username").send_keys('admin')
        self.browser.find_element(By.ID, "password").send_keys('sandbox')
        self.browser.find_element(By.ID, "loginbtn").click()
        self.assertIn('https://sandbox.moodledemo.net/',
                      self.browser.current_url)

    def testEmptyLogin(self):

        self.browser.find_element(By.ID, "loginbtn").click()
        self.assertIn('Invalid login, please try again',
                      self.browser.page_source)


if __name__ == '__main__':
    unittest.main(verbosity=2)

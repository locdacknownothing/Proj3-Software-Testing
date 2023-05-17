from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


class Utils():
    def init(self):
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)

    def login(self):
        self.driver.get("https://sandbox.moodledemo.net/login/index.php")

        username = self.driver.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("admin")

        password = self.driver.find_element(By.NAME, "password")
        password.clear()
        password.send_keys("sandbox")

        login = self.driver.find_element(By.ID, "loginbtn")
        login.click()

    def accessUserInAdminSite(self):
        adminSite = self.driver.find_element(
            By.LINK_TEXT, "Site administration")
        adminSite.click()

        users = self.driver.find_elements(By.PARTIAL_LINK_TEXT, "Users")
        users[0].click()

        action = self.driver.find_element(By.LINK_TEXT, "Add a new user")
        action.click()

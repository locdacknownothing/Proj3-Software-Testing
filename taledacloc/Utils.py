from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class Utils():
    def init(self):
        self.driver = webdriver.Chrome("C:\DRIVERS\chromedriver.exe")

    def logIn(self):
        self.driver.get('https://sandbox.moodledemo.net/login/index.php')

        username = self.driver.find_element(By.NAME, "username")
        username.clear()
        username.send_keys("teacher")

        password = self.driver.find_element(By.NAME, "password")
        password.clear()
        password.send_keys("sandbox")

        login = self.driver.find_element(By.ID, "loginbtn")
        login.click()

        print("Log in success")
        # time.sleep(2)
        # password.send_keys(Keys.RETURN)
        # time.sleep(2)

    def _textToIframe_(self, id, text):
        wait = WebDriverWait(self.driver, 5)
        iframe = wait.until(EC.visibility_of_element_located((By.XPATH, f"//iframe[@id='{id}']")))
        self.driver.switch_to.frame(iframe)

        body = self.driver.find_element(By.TAG_NAME, "body")
        body.clear()
        body.send_keys(text)

        self.driver.switch_to.default_content()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pandas as pd

class Utils():
    def __init__(self, data_path, sheet_name):
        # self.driver = webdriver.Chrome("C:\DRIVERS\chromedriver.exe")
        self.data_path = data_path
        self.sheet_name = sheet_name
        self.data = self._getData()

    def _getData(self):
        df = pd.read_excel(self.data_path, sheet_name=self.sheet_name)
        df.fillna('', inplace=True)
        columns = df.columns.tolist()
        all_values = df.values.tolist()
        data = [{column: value for column, value in zip(columns, row_values)} for row_values in all_values]

        return data
    
    def logIn(self):
        self.driver = webdriver.Chrome("C:\DRIVERS\chromedriver.exe")
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

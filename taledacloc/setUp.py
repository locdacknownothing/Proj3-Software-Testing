import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\DRIVERS\chromedriver.exe")
        self.driver.get('https://sandbox.moodledemo.net/login/index.php')
        elem = self.driver.find_element(By.NAME, "username")
        elem.send_keys("admin")
        elem = self.driver.find_element(By.NAME, "password")
        elem.send_keys("sandbox")
        elem.send_keys(Keys.RETURN)
        self.driver.get("https://sandbox.moodledemo.net/my/")

    def test_page_title(self):
        driver = self.driver
        elem1 = driver.find_element(By.CLASS_NAME,'maincalendar')
        wait = WebDriverWait(driver, 10)
        # elem2 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary')))
        elem2 = driver.find_element(By.XPATH,"""//button[text()='
            New event
        ']""")
        elem2.click()
        # elem2 = driver.find_element(By.CLASS_NAME,'btn-primary').click()
        # WebDriverWait(driver, 10).until(ExpectedConditions.visibilityOfElementLocated((By.CLASS_NAME, "btn-primary")))
        # driver.find_element(By.CLASS_NAME,'btn-primary')
        print("Element is visible? " + str(elem1.is_displayed()))
        print("Element is visible? " + str(elem2.is_displayed()))
        # ((JavascriptExecutor) driver).executeScript("arguments[0].click();", continue_button)
        # self.driver.implicitly_wait(1000)
        # self.assertIn('New event', self.driver.find_element(By.ID, "1-modal-title"))
    # def tearDown(self):
    #     self.driver.close()

unittest.main()
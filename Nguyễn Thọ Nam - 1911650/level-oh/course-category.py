import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
class CourseCategory(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://sandbox.moodledemo.net/login/index.php')
        elem = self.driver.find_element(By.NAME, "username")
        elem.send_keys("admin")
        elem = self.driver.find_element(By.NAME, "password")
        elem.send_keys("sandbox")
        elem.send_keys(Keys.RETURN)
        self.driver.get("https://sandbox.moodledemo.net/course/editcategory.php?parent=0")

    def test_1(self):
        driver = self.driver
        driver.implicitly_wait(10)
        elem1 = driver.find_element(By.XPATH,"""//span[text()='▼']""")
        driver.implicitly_wait(10)
        elem1.click()
        driver.implicitly_wait(10)

        wait = WebDriverWait(driver,60)
        succeed = False
        while not succeed:
            try:
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[data-value="1"]'))).click()
                succeed = True
            except:
                pass

        driver.implicitly_wait(10)
        name = driver.find_element(By.NAME,'name')
        name.send_keys("cate1")

        idnumber = driver.find_element(By.NAME,'idnumber')
        idnumber.send_keys("1")

        driver.switch_to.frame("id_description_editor_ifr")
        driver.find_element(By.ID,"tinymce").clear()
        driver.find_element(By.ID,"tinymce").send_keys("aaa")
        driver.switch_to.default_content()

        driver.find_element(By.NAME, 'submitbutton').click()

    def test_2(self):
        driver = self.driver
        driver.implicitly_wait(10)

        driver.find_element(By.XPATH,"//span[text()='× ']").click()
        driver.implicitly_wait(10)
        name = driver.find_element(By.NAME,'name')
        name.send_keys("cate2")

        idnumber = driver.find_element(By.NAME,'idnumber')
        idnumber.send_keys("2")

        driver.switch_to.frame("id_description_editor_ifr")
        driver.find_element(By.ID,"tinymce").clear()
        driver.find_element(By.ID,"tinymce").send_keys("aaa")
        driver.switch_to.default_content()

        driver.find_element(By.NAME, 'submitbutton').click()
        driver.implicitly_wait(10)
        self.assertEqual('https://sandbox.moodledemo.net/course/editcategory.php?parent=0', driver.current_url)

    def test_3(self):
        driver = self.driver
        driver.implicitly_wait(10)
        elem1 = driver.find_element(By.XPATH,"""//span[text()='▼']""")
        driver.implicitly_wait(10)
        elem1.click()
        driver.implicitly_wait(10)

        wait = WebDriverWait(driver,60)
        succeed = False
        while not succeed:
            try:
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[data-value="1"]'))).click()
                succeed = True
            except:
                pass
        
        driver.implicitly_wait(10)
        name = driver.find_element(By.NAME,'name')
        name.send_keys("")

        idnumber = driver.find_element(By.NAME,'idnumber')
        idnumber.send_keys("3")

        driver.switch_to.frame("id_description_editor_ifr")
        driver.find_element(By.ID,"tinymce").clear()
        driver.find_element(By.ID,"tinymce").send_keys("aaa")
        driver.switch_to.default_content()

        driver.find_element(By.NAME, 'submitbutton').click()
        driver.implicitly_wait(10)
        self.assertNotEqual('https://sandbox.moodledemo.net/course/editcategory.php?parent=0', driver.current_url)

    def test_4(self):
        driver = self.driver
        driver.implicitly_wait(10)
        elem1 = driver.find_element(By.XPATH,"""//span[text()='▼']""")
        driver.implicitly_wait(10)
        elem1.click()
        driver.implicitly_wait(10)

        wait = WebDriverWait(driver,60)
        succeed = False
        while not succeed:
            try:
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[data-value="1"]'))).click()
                succeed = True
            except:
                pass

        driver.implicitly_wait(10)
        name = driver.find_element(By.NAME,'name')
        name.send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbb111111")

        idnumber = driver.find_element(By.NAME,'idnumber')
        idnumber.send_keys("4")

        driver.switch_to.frame("id_description_editor_ifr")
        driver.find_element(By.ID,"tinymce").clear()
        driver.find_element(By.ID,"tinymce").send_keys("aaa")
        driver.switch_to.default_content()

        driver.find_element(By.NAME, 'submitbutton').click()
        driver.implicitly_wait(10)
        self.assertEqual('https://sandbox.moodledemo.net/course/editcategory.php', driver.current_url)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
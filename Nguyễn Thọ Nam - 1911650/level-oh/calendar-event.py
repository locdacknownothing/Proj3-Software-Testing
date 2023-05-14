import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
class CalendarEvent(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://sandbox.moodledemo.net/login/index.php')
        elem = self.driver.find_element(By.NAME, "username")
        elem.send_keys("admin")
        elem = self.driver.find_element(By.NAME, "password")
        elem.send_keys("sandbox")
        elem.send_keys(Keys.RETURN)
        self.driver.get("https://sandbox.moodledemo.net/my/")

    def test_1(self):
        driver = self.driver
        elem1 = driver.find_element(By.XPATH,"""//button[text()='
            New event
        ']""").click()
        driver.implicitly_wait(10)

        elem2 = driver.find_element(By.NAME,'name')
        elem2.send_keys("event1")

        select = Select(driver.find_element(By.NAME, 'timestart[day]'))
        select.select_by_index(12)

        select2 = Select(driver.find_element(By.NAME, 'timestart[month]'))
        select2.select_by_index(4)

        select3 = Select(driver.find_element(By.NAME, 'timestart[year]'))
        select3.select_by_index(123)

        select4 = Select(driver.find_element(By.NAME, 'timestart[hour]'))
        select4.select_by_index(12)

        select5 = Select(driver.find_element(By.NAME, 'timestart[minute]'))
        select5.select_by_index(30)

        show = driver.find_element(By.LINK_TEXT,"Show more...")
        show.click()
        driver.implicitly_wait(10)
        
        driver.switch_to.frame("id_description_ifr")
        driver.find_element(By.ID,"tinymce").clear()
        driver.find_element(By.ID,"tinymce").send_keys("aaa")
        driver.switch_to.default_content()

        location = driver.find_element(By.NAME,'location')
        location.send_keys("sandbox")

        driver.find_element(By.CSS_SELECTOR,'input#id_duration_2').click()
        driver.implicitly_wait(10)
        minute = driver.find_element(By.NAME, 'timedurationminutes').send_keys(1000)


        repeat = driver.find_element(By.NAME,'repeat')
        repeat.click()
        driver.implicitly_wait(10)

        repeats = driver.find_element(By.NAME,'repeats')
        repeats.clear()
        repeats.send_keys('1')

        save = driver.find_element(By.XPATH,"""//button[text()='

            Save
            ']""")
        save.click()
        driver.implicitly_wait(10)


    def test_2(self):
        driver = self.driver
        elem1 = driver.find_element(By.XPATH,"""//button[text()='
            New event
        ']""").click()
        driver.implicitly_wait(10)

        elem2 = driver.find_element(By.NAME,'name')
        elem2.send_keys("event2")

        select = Select(driver.find_element(By.NAME, 'timestart[day]'))
        select.select_by_index(12)

        select2 = Select(driver.find_element(By.NAME, 'timestart[month]'))
        select2.select_by_index(4)

        select3 = Select(driver.find_element(By.NAME, 'timestart[year]'))
        select3.select_by_index(123)

        select4 = Select(driver.find_element(By.NAME, 'timestart[hour]'))
        select4.select_by_index(12)

        select5 = Select(driver.find_element(By.NAME, 'timestart[minute]'))
        select5.select_by_index(30)

        show = driver.find_element(By.LINK_TEXT,"Show more...")
        show.click()
        driver.implicitly_wait(10)
        
        driver.switch_to.frame("id_description_ifr")
        driver.find_element(By.ID,"tinymce").clear()
        driver.find_element(By.ID,"tinymce").send_keys("aaa")
        driver.switch_to.default_content()

        location = driver.find_element(By.NAME,'location')
        location.send_keys("sandbox")

        driver.find_element(By.CSS_SELECTOR,'input#id_duration_2').click()
        driver.implicitly_wait(10)
        minute = driver.find_element(By.NAME, 'timedurationminutes').send_keys(0)


        repeat = driver.find_element(By.NAME,'repeat')
        repeat.click()
        driver.implicitly_wait(10)

        repeats = driver.find_element(By.NAME,'repeats')
        repeats.clear()
        repeats.send_keys('1')

        save = driver.find_element(By.XPATH,"""//button[text()='

            Save
            ']""")
        save.click()
        driver.implicitly_wait(10)
        self.assertEqual(True, driver.find_element(By.XPATH,"//div[@id='fgroup_id_error_durationgroup']").is_enabled())


    def test_3(self):
        driver = self.driver
        elem1 = driver.find_element(By.XPATH,"""//button[text()='
            New event
        ']""").click()

        driver.implicitly_wait(10)
        elem2 = driver.find_element(By.NAME,'name')
        elem2.send_keys("sandbox")

        select = Select(driver.find_element(By.NAME, 'timestart[day]'))
        select.select_by_index(5)

        select2 = Select(driver.find_element(By.NAME, 'timestart[month]'))
        select2.select_by_index(4)

        select3 = Select(driver.find_element(By.NAME, 'timestart[year]'))
        select3.select_by_index(123)

        select4 = Select(driver.find_element(By.NAME, 'timestart[hour]'))
        select4.select_by_index(12)

        select5 = Select(driver.find_element(By.NAME, 'timestart[minute]'))
        select5.select_by_index(30)

        show = driver.find_element(By.LINK_TEXT,"Show more...")
        show.click()
        driver.implicitly_wait(10)
        
        driver.switch_to.frame("id_description_ifr")
        driver.find_element(By.ID,"tinymce").clear()
        driver.find_element(By.ID,"tinymce").send_keys("aaa")
        driver.switch_to.default_content()

        location = driver.find_element(By.NAME,'location')
        location.send_keys("sandbox")

        duration = driver.find_element(By.CSS_SELECTOR,'input#id_duration_2')
        duration.click()
        driver.implicitly_wait(10)
        minute = driver.find_element(By.NAME, 'timedurationminutes')
        minute.send_keys('1e19')

        repeat = driver.find_element(By.NAME,'repeat')
        repeat.click()
        driver.implicitly_wait(10)

        repeats = driver.find_element(By.NAME,'repeats')
        repeats.clear()
        repeats.send_keys('2')

        save = driver.find_element(By.XPATH,"""//button[text()='

            Save
            ']""")
        save.click()
        driver.implicitly_wait(10)
        textError = driver.find_element(By.CLASS_NAME,'moodle-exception-message').text
        self.assertIn('Error writing to database', textError)

    def test_4(self):
        driver = self.driver
        elem1 = driver.find_element(By.XPATH,"""//button[text()='
            New event
        ']""").click()

        driver.implicitly_wait(10)
        elem2 = driver.find_element(By.NAME,'name')
        elem2.send_keys("event4")

        select = Select(driver.find_element(By.NAME, 'timestart[day]'))
        select.select_by_index(13)

        select2 = Select(driver.find_element(By.NAME, 'timestart[month]'))
        select2.select_by_index(4)

        select3 = Select(driver.find_element(By.NAME, 'timestart[year]'))
        select3.select_by_index(123)

        select4 = Select(driver.find_element(By.NAME, 'timestart[hour]'))
        select4.select_by_index(12)

        select5 = Select(driver.find_element(By.NAME, 'timestart[minute]'))
        select5.select_by_index(30)

        show = driver.find_element(By.LINK_TEXT,"Show more...")
        show.click()
        driver.implicitly_wait(10)
        
        driver.switch_to.frame("id_description_ifr")
        driver.find_element(By.ID,"tinymce").clear()
        driver.find_element(By.ID,"tinymce").send_keys("aaa")
        driver.switch_to.default_content()

        location = driver.find_element(By.NAME,'location')
        location.send_keys("sandbox")

        duration = driver.find_element(By.CSS_SELECTOR,'input#id_duration_2')
        duration.click()
        driver.implicitly_wait(10)
        minute = driver.find_element(By.NAME, 'timedurationminutes')
        minute.send_keys('1')

        repeat = driver.find_element(By.NAME,'repeat')
        repeat.click()
        driver.implicitly_wait(10)

        repeats = driver.find_element(By.NAME,'repeats')
        repeats.clear()
        repeats.send_keys('1')

        save = driver.find_element(By.XPATH,"""//button[text()='

            Save
            ']""")
        save.click()
        driver.implicitly_wait(10)
        self.assertIn('event4', driver.find_element(By.XPATH,"//span[text()='event4']").text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
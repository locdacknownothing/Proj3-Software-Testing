import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import Utils

path = "data.xlsx"
sheet = "calendar_event"
rows = Utils.getRowCount(path, sheet)
driver = webdriver.Chrome()
driver.get('https://sandbox.moodledemo.net/login/index.php')
driver.find_element(By.NAME, "username").send_keys("admin")
elem = driver.find_element(By.NAME, "password")
elem.send_keys("sandbox")
elem.send_keys(Keys.RETURN)
driver.get("https://sandbox.moodledemo.net/my/")


for r in range(2, rows + 1):
    event_name = Utils.readData(path, sheet, r, 1)
    timestart_day = Utils.readData(path, sheet, r, 2)
    timestart_month = Utils.readData(path, sheet, r, 3)
    timestart_year = Utils.readData(path, sheet, r, 4)
    timestart_hour = Utils.readData(path, sheet, r, 5)
    timestart_minute = Utils.readData(path, sheet, r, 6)
    description = Utils.readData(path, sheet, r, 7)
    location = Utils.readData(path, sheet, r, 8)
    duration = Utils.readData(path, sheet, r, 9)
    repeat = Utils.readData(path, sheet, r, 10)

    driver.find_element(By.XPATH,"""//button[text()='
            New event
        ']""").click()
    driver.implicitly_wait(10)
    driver.find_element(By.NAME,'name').send_keys(event_name)
    Select(driver.find_element(By.NAME, 'timestart[day]')).select_by_index(timestart_day)
    Select(driver.find_element(By.NAME, 'timestart[month]')).select_by_index(timestart_month)
    Select(driver.find_element(By.NAME, 'timestart[year]')).select_by_index(timestart_year)
    Select(driver.find_element(By.NAME, 'timestart[hour]')).select_by_index(timestart_hour)
    Select(driver.find_element(By.NAME, 'timestart[minute]')).select_by_index(timestart_minute)

    driver.find_element(By.LINK_TEXT,"Show more...").click()
    driver.implicitly_wait(20)

    driver.switch_to.frame("id_description_ifr")
    driver.find_element(By.ID,"tinymce").clear()
    driver.find_element(By.ID,"tinymce").send_keys(description)
    driver.switch_to.default_content()

    driver.find_element(By.NAME,'location').send_keys(location)

    driver.find_element(By.CSS_SELECTOR,'input#id_duration_2').click()
    driver.implicitly_wait(10)
    minute = driver.find_element(By.NAME, 'timedurationminutes')
    if (minute != 'none'):
        minute.send_keys(duration)

    driver.find_element(By.NAME,'repeat').click()
    driver.implicitly_wait(10)

    repeats = driver.find_element(By.NAME,'repeats')
    repeats.clear()
    if (repeat != 'none'):
        repeats.send_keys(repeat)

    driver.find_element(By.XPATH,"""//button[text()='

            Save
            ']""").click()
    
    driver.implicitly_wait(10)
    try:
        elem = driver.find_element(By.XPATH,"//span[text()='" + event_name + "']")
        if (elem.text == event_name):
            Utils.writeData(path, sheet, r, 11, "passed")
    except NoSuchElementException:  #spelling error making this code not work as expected
        Utils.writeData(path, sheet, r, 11, "failed")
        driver.refresh()
        continue

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import Utils

path = "data.xlsx"
sheet = "course_category"
rows = Utils.getRowCount(path, sheet)
driver = webdriver.Chrome()
driver.get('https://sandbox.moodledemo.net/login/index.php')
driver.find_element(By.NAME, "username").send_keys("admin")
elem = driver.find_element(By.NAME, "password")
elem.send_keys("sandbox")
elem.send_keys(Keys.RETURN)


for r in range(2, rows + 1):
    parent_category = Utils.readData(path, sheet, r, 1)
    name = Utils.readData(path, sheet, r, 2)
    id_number = Utils.readData(path, sheet, r, 3)
    description = Utils.readData(path, sheet, r, 4)

    driver.get("https://sandbox.moodledemo.net/course/editcategory.php?parent=0")
    driver.implicitly_wait(10)
    elem1 = driver.find_element(By.XPATH,"""//span[text()='▼']""")
    driver.implicitly_wait(10)
    elem1.click()
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver,5)
    succeed = False

    if (parent_category != 0):
        while not succeed:
            try:
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[data-value="' + str(parent_category) + '"]'))).click()
                succeed = True
            except:
                pass
    else:
        driver.find_element(By.XPATH,"//span[text()='× ']").click()

    driver.implicitly_wait(10)
    if (name != 'none'):
        driver.find_element(By.NAME,'name').send_keys(name)

    driver.find_element(By.NAME,'idnumber').send_keys(id_number)

    driver.switch_to.frame("id_description_editor_ifr")
    driver.find_element(By.ID,"tinymce").clear()
    driver.find_element(By.ID,"tinymce").send_keys(description)
    driver.switch_to.default_content()

    driver.find_element(By.NAME, 'submitbutton').click()

    if (driver.current_url != 'https://sandbox.moodledemo.net/course/editcategory.php?parent=0' and driver.current_url != 'https://sandbox.moodledemo.net/course/editcategory.php'):
        Utils.writeData(path, sheet, r, 5, "passed")
    else:
        Utils.writeData(path, sheet, r, 5, "failed")
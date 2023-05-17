from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import Utils

path = "data.xlsx"
sheet = "add_a_new_user"

rows = Utils.getRowCount(path, sheet)
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

driver.get('https://sandbox.moodledemo.net/login/index.php')

username = driver.find_element(By.NAME, "username")
username.clear()
username.send_keys("admin")

password = driver.find_element(By.NAME, "password")
password.clear()
password.send_keys("sandbox")

login = driver.find_element(By.ID, "loginbtn")
login.click()

for r in range(2, rows+1):

    driver.get(
        'https://sandbox.moodledemo.net/user/editadvanced.php?id=-1')

    username = Utils.readData(path, sheet, r, 1)
    password = Utils.readData(path, sheet, r, 2)
    firstname = Utils.readData(path, sheet, r, 3)
    lastname = Utils.readData(path, sheet, r, 4)
    email = Utils.readData(path, sheet, r, 5)
    city = Utils.readData(path, sheet, r, 6)

    driver.find_element(By.ID, "id_username").send_keys(username)
    driver.find_element(
        By.PARTIAL_LINK_TEXT, "Click to enter text").click()
    driver.find_element(By.ID, "id_newpassword").send_keys(password)
    driver.find_element(By.ID, "id_firstname").send_keys(firstname)
    driver.find_element(By.ID, "id_lastname").send_keys(lastname)
    driver.find_element(By.ID, "id_email").send_keys(email)
    driver.find_element(By.ID, "id_city").send_keys(city)
    driver.find_element(By.ID, "id_submitbutton").click()

    if (driver.current_url == 'https://sandbox.moodledemo.net/admin/user.php'):
        Utils.writeData(path, sheet, r, 7, "passed")
    else:
        Utils.writeData(path, sheet, r, 7, "failed")

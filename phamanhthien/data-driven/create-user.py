
import XLUtils
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

path = "ExcelFiles/data.xlsx"
sheet = "create_user"


rows = XLUtils.getRowCount(path, sheet)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://sandbox.moodledemo.net/login/index.php')
driver.find_element(By.ID, "username").send_keys('manager')
driver.find_element(By.ID, "password").send_keys('sandbox')
driver.find_element(By.ID, "loginbtn").click()

for r in range(2, rows+1):

    driver.get(
        'https://sandbox.moodledemo.net/user/editadvanced.php?id=-1')

    username = XLUtils.readData(path, sheet, r, 1)
    first_name = XLUtils.readData(path, sheet, r, 2)
    last_name = XLUtils.readData(path, sheet, r, 3)
    email = XLUtils.readData(path, sheet, r, 4)
    driver.find_element(
        By.ID, "id_username").send_keys(username)
    driver.find_element(
        By.ID, "id_createpassword").click()

    driver.find_element(By.ID, "id_firstname").send_keys(first_name)
    driver.find_element(By.ID, "id_lastname").send_keys(last_name)
    driver.find_element(By.ID, "id_email").send_keys(
        email)
    driver.find_element(By.ID, "id_submitbutton").click()

    if (driver.current_url == 'https://sandbox.moodledemo.net/admin/user.php'):
        XLUtils.writeData(path, sheet, r, 5, "passed")
    else:
        XLUtils.writeData(path, sheet, r, 5, "failed")


import XLUtils
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

path = "ExcelFiles/data.xlsx"
sheet = "login"


rows = XLUtils.getRowCount(path, sheet)
for r in range(2, rows+1):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://sandbox.moodledemo.net/login/index.php')
    username = XLUtils.readData(path, sheet, r, 1)
    password = XLUtils.readData(path, sheet, r, 2)
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "loginbtn").click()
    if (driver.current_url == 'https://sandbox.moodledemo.net/'):
        XLUtils.writeData(path, sheet, r, 3, "passed")
    else:
        XLUtils.writeData(path, sheet, r, 3, "failed")

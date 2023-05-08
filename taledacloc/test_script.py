from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from faker import Faker
from time import time
fake = Faker()

print(webdriver.__version__)

def test_facebook_login(email, password):
    driver = webdriver.Chrome("C:\DRIVERS\chromedriver.exe")
    driver.get("https://www.facebook.com/")
    email_field = driver.find_element(value="email")
    password_field = driver.find_element(value="pass")
    submit_button = driver.find_element("name", "login")
    # email = fake.email()
    # password = fake.password()
    email_field.clear()
    email_field.send_keys(email)
    password_field.clear()
    password_field.send_keys(password)
    submit_button.click()
    print(f'Email: {email}, Password: {password}')
    assert "facebook.com/profile.php" in driver.current_url
    driver.quit()

for i in range(1):
    test_facebook_login()
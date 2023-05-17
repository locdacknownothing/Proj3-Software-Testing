import unittest
from Utils import *


class AddANewUserUtils(Utils):
    def init(self):
        super().init()
        self.error_id = ["id_error_username", "id_error_newpassword", "id_error_firstname",
                         "id_error_lastname", "id_error_email"]
        self.error_message = [
            "The username can only contain alphanumeric lowercase characters (letters and numbers), underscore (_), hyphen (-), period (.) or at symbol (@).", "Required", "Missing given name", "Missing last name", "Invalid email address", "Only lowercase letters allowed", "This username already exists, choose another"]

    def editUsername(self, text, enter=False):
        username = self.driver.find_element(By.ID, "id_username")
        username.clear()
        if text:
            username.send_keys(text)

        if enter:
            username.send_keys(Keys.ENTER)

    def editPassword(self, text):
        newpassword = self.driver.find_element(
            By.PARTIAL_LINK_TEXT, "Click to enter text")
        newpassword.click()

        password = self.driver.find_element(By.ID, "id_newpassword")
        password.send_keys(text)

    def editFirstName(self, text, enter=False):
        first_name = self.driver.find_element(By.ID, "id_firstname")
        first_name.clear()
        if text:
            first_name.send_keys(text)

        if enter:
            first_name.send_keys(Keys.ENTER)

    def editLastName(self, text):
        last_name = self.driver.find_element(By.ID, "id_lastname")
        last_name.clear()
        if text:
            last_name.send_keys(text)

    def editEmail(self, text, enter=False):
        email = self.driver.find_element(By.ID, "id_email")
        email.clear()
        if text:
            email.send_keys(text)

        if enter:
            email.send_keys(Keys.ENTER)

    def editCity(self, text, enter=False):
        city = self.driver.find_element(By.ID, "id_city")
        city.clear()
        if text:
            city.send_keys(text)

        if enter:
            city.send_keys(Keys.ENTER)

    def createUser(self):
        try:
            wait = WebDriverWait(self.driver, 3)
            submit = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='submit' and @value='Create user']")))
        except TimeoutException:
            return False

        submit.click()

    def isError(self, at, error_idx):
        error = None
        try:
            error = self.driver.find_element(By.ID, self.error_id[at])
        except NoSuchElementException:
            return False

        print(error.text)
        return self.error_message[error_idx] in error.text

    def isSuccess(self):
        curr_url = self.driver.current_url
        user_url = "https://sandbox.moodledemo.net/admin/user.php"
        print(curr_url)
        return user_url in curr_url


class AddANewUserTestCase(AddANewUserUtils, unittest.TestCase):
    def setUp(self):
        self.init()
        self.login()
        self.accessUserInAdminSite()

    def test_002_001(self):
        self.editUsername("manhnguyen")
        self.editPassword("123456")
        self.editFirstName("Manh")
        self.editLastName("Nguyen")
        self.editEmail("manhnguyen1312@hcmut.edu.vn")
        self.createUser()

        expected = self.isSuccess()
        self.driver.quit()
        assert expected

    def test_002_002(self):
        self.editUsername("manhnguyen1312")
        self.editPassword("1234567")
        self.editFirstName("Manh")
        self.editLastName("Nguyen")
        self.editEmail("manhnguyen132@hcmut.edu.vn")
        self.editCity("HCMC")
        self.createUser()

        expected = self.isSuccess()
        self.driver.quit()
        assert expected

    def test_002_003_1(self):
        self.editUsername(None)
        self.createUser()

        expected = self.isError(2, 2) and self.isError(
            3, 3) and self.isError(4, 1)
        self.driver.quit()
        assert expected

    def test_002_003_2(self):
        self.editUsername("m10")
        self.editFirstName("Manh")
        self.createUser()

        expected = self.isError(3, 3) and self.isError(4, 1)
        self.driver.quit()
        assert expected

    def test_002_003_3(self):
        self.editUsername("m10")
        self.editFirstName("Manh")
        self.editLastName("Nguyen")
        self.createUser()

        expected = self.isError(4, 1)
        self.driver.quit()
        assert expected

    def test_002_003_4(self):
        self.editUsername("m10")
        self.editFirstName("Manh")
        self.editLastName("Nguyen")
        self.editEmail("manh.nguyen@hcmut.edu.vn")
        self.createUser()

        expected = self.isError(1, 1)
        self.driver.quit()
        assert expected

    def test_002_003_5(self):
        self.editFirstName("Manh")
        self.editLastName("Nguyen")
        self.editEmail("manh.nguyen@hcmut.edu.vn")
        self.editPassword("123456")
        self.createUser()

        expected = self.isError(0, 1)
        self.driver.quit()
        assert expected

    def test_002_004_1(self):
        self.editUsername("M10")
        self.editFirstName("Manh")
        self.editLastName("Nguyen")
        self.editEmail("manh.nguyen@hcmut.edu.vn")
        self.editPassword("123456")
        self.createUser()

        expected = self.isError(0, 5)
        self.driver.quit()
        assert expected

    def test_002_004_2(self):
        self.editUsername("m*")
        self.editFirstName("Manh")
        self.editLastName("Nguyen")
        self.editEmail("manh.nguyen@hcmut.edu.vn")
        self.editPassword("123456")
        self.createUser()

        expected = self.isError(0, 0)
        self.driver.quit()
        assert expected

    def test_002_004_3(self):
        self.editUsername("manh1312")
        self.editFirstName("Manh")
        self.editLastName("Nguyen")
        self.editEmail("manh.nguyen@hcmut.edu.vn")
        self.editPassword("123456")
        self.createUser()

        expected = self.isError(0, 6)
        self.driver.quit()
        assert expected

    def test_002_005(self):
        self.editUsername("m10")
        self.editFirstName("Manh")
        self.editLastName("Nguyen")
        self.editEmail("abc@gmail")
        self.editPassword("123456")
        self.createUser()

        expected = self.isError(4, 4)
        self.driver.quit()
        assert expected


unittest.main()

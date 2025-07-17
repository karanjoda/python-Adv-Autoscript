from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class LoginPage(BasePage):
    username_input = (By.NAME, "email")
    password_input = (By.NAME, "password")
    signin_button  = (By.XPATH, "//button[@type='submit']")

    def login(self,username,password):
        self.enter_text(self.username_input, username)
        self.enter_text(self.password_input, password)
        self.click(self.signin_button)
        self.wait_for_url("licence")

    def assert_error_message(self, expected_msg):
        if expected_msg in self.driver.page_source:
            print("✅ Error message found in page source.")
            return
        else:
            print("❌ Error message NOT found. Page snippet:")
            print(self.driver.page_source[:1000])
            assert False, "Expected error message not found in page source."
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator, timeout=10):
        print(f"Waiting to click element: {locator}")

        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()


    def enter_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        # element.clear()
        element.send_keys(text)

    def select_dropdown_by_visible_text(self, locator, text, timeout=10):
        dropdown = Select(self.find_element(locator, timeout))
        dropdown.select_by_visible_text(text)

    def select_dropdown_by_index(self, locator, index, timeout=10):
        dropdown = Select(self.find_element(locator, timeout))
        dropdown.select_by_index(index)

    def select_dropdown_by_value(self, locator, value, timeout=10):
        dropdown = Select(self.find_element(locator, timeout))
        dropdown.select_by_value(value)

    def wait_for_url(self, url_fragment, timeout=10):
        """Wait until the URL contains the given fragment."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_contains(url_fragment))
            return True
        except TimeoutException:
            print(f"Timeout: URL did not contain '{url_fragment}' within {timeout} seconds.")
            return False

    def wait_for_element_visible(self, locator, timeout=15):
        """Wait until the element is visible on the page."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"Timeout: Element {locator} not visible after {timeout} seconds.")
            return None    

    def wait_until_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    

    def select_custom_dropdown(self, dropdown_locator, option_text):
        self.wait_until_clickable(dropdown_locator).click()
        option_locator = (By.XPATH, f"//li[normalize-space(text())='{option_text}']")
        self.wait_until_clickable(option_locator).click()

    def select_autocomplete_input(self, input_locator, option_text):
        self.enter_text(input_locator, option_text)
        suggestion_locator = (By.XPATH, f"//li[contains(text(), '{option_text}')]")
        self.wait_until_clickable(suggestion_locator).click()

    def clear_and_type(self, locator, text):
        field = self.wait_for_element_visible(locator)
        try:
            field.clear()
        except:
            self.driver.execute_script("arguments[0].value = '';", field)
        field.send_keys(text)
    

    def select_ant_dropdown_option(self, dropdown_trigger_locator, input_locator, option_text):
        self.wait_until_clickable(dropdown_trigger_locator).click()
        input_elem = self.wait_for_element_visible(input_locator)
        input_elem.send_keys(option_text)
        input_elem.send_keys(Keys.ENTER)
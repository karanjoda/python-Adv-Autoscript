from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException



class LicencePage(BasePage):


    create_licence_btn = (By.XPATH, "//button[span[text()='Create Licence']]")
    product_dropdown_trigger = (By.XPATH, "//input[@id='product_name']")  # This is usually a div that opens the dropdown
    product_input = (By.ID, "product_name")  # This is the invisible input where we type

    # Actions
    def create_licence(self):
        self.wait_until_clickable(self.create_licence_btn).click()
        time.sleep(5)

        # self.select_ant_dropdown_option(
        #     dropdown_trigger_locator=self.product_dropdown_trigger,
        #     input_locator=self.product_input,
        #     option_text=product_name
        # )
        self.find_element(self.product_dropdown_trigger).click()
        time.sleep(5)


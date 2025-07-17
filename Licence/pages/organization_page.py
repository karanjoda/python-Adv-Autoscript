from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException



class OrganisationPage(BasePage):
    organisation_sidebar = (By.XPATH, "//a[@href='/organisation']")
    neworg_btn           = (By.XPATH, "//button[span[text()='New Organisation']]")
    orgname              = (By.ID, "organization_name") 
    firstname            = (By.ID, "first_name")
    lastname             = (By.ID, "last_name")
    email                = (By.ID, "email")
    phone                = (By.ID, "phone")
    countrycode_dropdown = (By.ID, "country_code")
    addbtn               = (By.XPATH, "//button[span[text()='Add']]")
    organizationtext     = (By.XPATH, "//h1[text()='Organisation']")
    edit                 = (By.XPATH, "(//*[name()='svg'])[22]")
    delete               = (By.XPATH, "(//*[name()='svg'])[23]")
    update               = (By.XPATH, "//button[span[text()='Update']]")
    cancel               = (By.XPATH, "//button[span[text()='Cancel']]")
    Delete               = (By.XPATH, "//button[span[text()='Delete']]")

    def organisation(self,orgname,firstname,lastname,email,phone):

       self.wait_until_clickable(self.organisation_sidebar).click()
       self.wait_until_clickable(self.neworg_btn).click()
       self.wait_for_element_visible(self.orgname)
       self.enter_text(self.orgname,   orgname)
       self.enter_text(self.firstname, firstname)
       self.enter_text(self.lastname,  lastname)
       self.enter_text(self.email,     email)
       self.enter_text(self.phone,     phone)
       dropdown = self.find_element(self.countrycode_dropdown)
       dropdown.click()
       dropdown.send_keys(Keys.RETURN)
       self.find_element(self.addbtn).click()
       time.sleep(3)

    
 

    def edit_update_organisation(self,firstname,lastname,phone):
        self.wait_until_clickable(self.organisation_sidebar).click()
        self.wait_for_element_visible(self.organizationtext)
        self.wait_until_clickable(self.edit).click()
        self.clear_and_type(self.firstname, firstname)
        self.clear_and_type(self.lastname, lastname)
        self.clear_and_type(self.phone, phone)
        self.wait_until_clickable(self.update).click()
        time.sleep(3)



    def edit_cancel_organisation(self,firstname,lastname,phone):
        self.wait_until_clickable(self.organisation_sidebar).click()
        self.wait_for_element_visible(self.organizationtext)
        self.wait_until_clickable(self.edit).click()
        self.clear_and_type(self.firstname, firstname)
        self.clear_and_type(self.lastname, lastname)
        self.clear_and_type(self.phone, phone)
        self.wait_until_clickable(self.cancel).click()
        time.sleep(3)


    def delete_cancel_organisation(self):
        self.wait_until_clickable(self.organisation_sidebar).click()
        self.wait_for_element_visible(self.organizationtext)
        self.wait_until_clickable(self.delete).click()
        self.wait_until_clickable(self.cancel).click()
        time.sleep(3)

    def delete_delete_organisation(self):
        self.wait_until_clickable(self.organisation_sidebar).click()
        self.wait_for_element_visible(self.organizationtext)
        self.wait_until_clickable(self.delete).click()
        self.wait_until_clickable(self.Delete).click()
        time.sleep(3)


    def assert_error_message(self, expected_msg):
            if expected_msg in self.driver.page_source:
                print("✅ Error message found in page source.")
                return
            else:
                print("❌ Error message NOT found. Page snippet:")
                print(self.driver.page_source[:1000])
                assert False, "Expected error message not found in page source."
         
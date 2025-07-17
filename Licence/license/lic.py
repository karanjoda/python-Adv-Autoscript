from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def test_newlicese(driver):
    
    # test logging in with correct credentials
    driver.find_element(By.NAME, "email").send_keys("snarhe@noc.softcell.com")
    driver.find_element(By.NAME, "password").send_keys("StrongP@ssw0rd!")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//button[@type='button'])[1]").click()
    time.sleep(2)
    dropdown = driver.find_element(By.XPATH, "//input[@id='product_name']")# Change "dropdown_id" accordingly
    dropdown.click()
    dropdown.send_keys(Keys.RETURN)    
    dropdown = driver.find_element(By.XPATH, "//input[@id='rc_select_1']")# Change "dropdown_id" accordingly
    dropdown.click()
    dropdown.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.find_element(By.ID, "expires_at").send_keys("2025-02-28")
    time.sleep(2)
    driver.find_element(By.ID, "allowed_devices").send_keys("10")
    time.sleep(2)
    # driver.find_element(By.XPATH, "//span[normalize-space()='Cancel']").click() #cancel
    driver.find_element(By.XPATH, "//span[normalize-space()='Create']").click() #create
    time.sleep(2)




def test_login_newlicese_edit(driver):
    
    # test logging in with correct credentials
    driver.find_element(By.NAME, "email").send_keys("snarhe@noc.softcell.com")
    driver.find_element(By.NAME, "password").send_keys("StrongP@ssw0rd!")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//*[name()='svg'])[22]").click()







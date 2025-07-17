from pages.login_page import LoginPage
from pages.licence_page import LicencePage


def test_create_licence(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login("karan@noc.softcell.com", "Tester@12345")
    licence_page = LicencePage(driver)
    licence_page.create_licence()

def test_delete_liccence
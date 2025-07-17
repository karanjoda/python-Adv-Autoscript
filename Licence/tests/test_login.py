from pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize("username_input,password_input ,expected_error",[
    ("karan@noc.softcell.com","Tester@12345","licence"),
    ("kar@testcom","Tester@12345","An error occurred while logging in"),  # Invalid email
    ("karan@noc.softcell.com", "invalidpassword","An error occurred while logging in"), # Invalid password
    ("","","Please enter a valid email or username")   #empty password
])


def test_Invalid_negativecases(setup,username_input,password_input,expected_error):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login(username_input,password_input)
    login_page.assert_error_message(expected_error)
     

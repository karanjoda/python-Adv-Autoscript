# import pytest
from pages.login_page import LoginPage
from pages.organization_page import OrganisationPage 



# def test_Add_new_organisation(setup):
#     driver = setup
#     login_page = LoginPage(driver)
#     login_page.login("karan@noc.softcell.com", "Tester@12345")
#     organization_page = OrganisationPage(driver)
#     organization_page.organisation("Testing","test","team","karan@test.com","1234567890")
#     assert "Organisation created successfully" in driver.page_source

   

# @pytest.mark.parametrize("orgname, firstname, lastname, email, phone, expected_error", [
#     ("", "test", "team", "karan@test.com", "1234567890", "Failed to create organisation. Please try again."), #empty org
#     ("Testing", "test", "team", "karan@test.com", "1234567890", "organization with the same email already exists"),#same email 
#     ("TestOrg", "", "Doe", "john@example.com", "1234567890", "First name is required"),  # Empty first name
#     ("TestOrg", "John", "Doe", "invalid-email", "1234567890", "Please enter a valid email address"),    # Invalid email
# ])

# def test_Invalid_org_data(setup, orgname, firstname, lastname, email, phone, expected_error):
#     driver = setup
#     login_page = LoginPage(driver)
#     login_page.login("karan@noc.softcell.com", "Tester@12345")
#     organization_page = OrganisationPage(driver)
#     organization_page.organisation(orgname, firstname, lastname, email, phone)
#     organization_page.assert_error_message(expected_error)

# def test_edit_organisation_update(setup):
#     driver = setup
#     login_page = LoginPage(driver)
#     login_page.login("karan@noc.softcell.com", "Tester@12345")  
#     organization_page = OrganisationPage(driver)
#     organization_page.update_organisation(
#         firstname="UpdatedFirst",
#         lastname="UpdatedLast",
#         phone="9876543210"
#     )

#     assert "Organisation updated successfully" in driver.page_source #sucess msg 'Device updated successfully'

# def test_edit_organisation_cancel(setup):
#     driver = setup
#     login_page = LoginPage(driver)
#     login_page.login("karan@noc.softcell.com", "Tester@12345")  
#     organization_page = OrganisationPage(driver)
#     organization_page.cancel_organisation(
#         firstname="cancelFirst",
#         lastname="cancelLast",
#         phone="9876543210"
#     )


def test_delete_organisation_cancel(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login("karan@noc.softcell.com", "Tester@12345")
    organization_page = OrganisationPage(driver)
    organization_page.delete_cancel_organisation()

# def test_delete_organisation_delete(setup):
#     driver  = setup
#     login_page = LoginPage(driver)
#     login_page.login("karan@noc.softcell.com", "Tester@12345")
#     organization_page = OrganisationPage(driver)
#     organization_page.delete_delete_organisation()

#     assert "Organisation deleted successfully" in driver.page_source

from loginPage import LoginPage
from selenium.webdriver.common.by import By
from utilities import BaseClass


class TestInspectingHTMLLocators(BaseClass):
    EMAIL = 'your_email@example.com'
    PASSWORD = 'your_password_here'
    NAME = 'your_name_here'
    GENDER = 'Male'
    
    def test_inspecting_html_locators(self):
        login = LoginPage(self.driver)
        login.enter_email().send_keys(self.EMAIL)
        login.enter_password().send_keys(self.PASSWORD)
        login.tick_checkbox().click()

        
        login.enter_name().send_keys(self.NAME)
        login.tick_radio_button().click()

        login.choose_dropdpwn_option_by_text(self.GENDER)

        # //tagname[@attribute='value'] custom XPATH
        login.submit().click()  # Submit button
        message = self.driver.find_element(By.CLASS_NAME, 'alert-success').text  # Alert after submitting
        print(message)

        # Validation
        assert 'Success' in message

        self.driver.find_element(By.XPATH, '(//input[@type="text"])[3]').send_keys(', middle name huseyin')
        self.driver.find_element(By.XPATH, '(//input[@type="text"])[3]').clear()

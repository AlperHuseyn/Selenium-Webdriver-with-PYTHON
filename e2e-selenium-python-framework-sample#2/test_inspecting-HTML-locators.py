from homePage import HomePage
from homePageData import HomePageData
import pytest
from selenium.webdriver.common.by import By
from utilities import BaseClass


class TestHomePage(BaseClass):
        
    dropdown_locator = (By.ID, 'exampleFormControlSelect1')

    def test_form_submission(self, get_params):
        # Use utility method to get logger name
        log = self.get_logs(self.get_unique_logger_name())  
        submission = HomePage(self.driver)
        submission.get_email().send_keys(get_params['email'])
        log.info(f'Email: {get_params["email"]}')
        submission.get_password().send_keys(get_params['password'])
        log.info(f'Password: {get_params["password"]}')
        submission.tick_checkbox().click()
        log.info('Agreement accepted...')
        submission.get_name().send_keys(get_params['name'])
        log.info(f'Name: {get_params["name"]}')
        submission.tick_radio_button().click()
        log.info('Employment status checked...')
        self.choose_dropdown_option_by_text(self.dropdown_locator, get_params['gender'])
        log.info(f'Gender: {get_params["gender"]}')
        # //tagname[@attribute='value'] custom XPATH
        submission.submit().click()  # Submit button
        log.info('Submitted...')
        message = submission.get_success_message().text  # Alert after submitting

        # Validation
        assert 'Success' in message
        
        # Refresh page befor next run
        self.driver.refresh()
        log.info('Refreshed the page...')
        
    @pytest.fixture(params=HomePageData.test_form_submission_data)
    def get_params(self, request):
        return request.param
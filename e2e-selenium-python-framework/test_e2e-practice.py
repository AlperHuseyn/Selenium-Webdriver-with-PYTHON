'Import necessary modules'
from selenium.webdriver.common.by import By
from utilities import BaseClass
from HomePage import HomePage


class TestE2EFramework(BaseClass):
    def test_e2e_framework(self):
        # Switch to shop page
        checkout = HomePage(self.driver).switch_to_checkout_page()

        # Do the things related to checkout
        checkout.add_to_card().click()
        checkout.switch_to_checkout_page().click()
        confirmation = checkout.checkout()

        # Do the things relted to confirmation
        confirmation.enter_country()
        confirmation.wait_for_country_to_appear()
        confirmation.choose_country_in_the_list().click()
        confirmation.accept_agreement().click()
        confirmation.purchase().click()

        assert 'Success' in self.driver.find_element(By.CSS_SELECTOR, '.alert-success').text

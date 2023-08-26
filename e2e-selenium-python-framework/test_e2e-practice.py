'Import necessary modules'
from CheckoutPage import CheckoutPage
from ConfirmationPage import ConfirmationPage
from selenium.webdriver.common.by import By
from utilities import BaseClass
from HomePage import HomePage


class TestE2EFramework(BaseClass):
    def test_e2e_framework(self):
        # Switch to shop page
        HomePage(self.driver).shop_button().click()

        # Do the things related to checkout
        checkout = CheckoutPage(self.driver)
        checkout.add_to_card().click()
        checkout.switch_to_checkout_page().click()
        checkout.checkout().click()
        
        conformation = ConfirmationPage(self.driver)
        conformation.enter_country()
        conformation.wait_for_country_to_appear()
        conformation.choose_country_in_the_list().click()
        conformation.accept_agreement().click()
        conformation.purchase().click()

        assert 'Success' in self.driver.find_element(By.CSS_SELECTOR, '.alert-success').text
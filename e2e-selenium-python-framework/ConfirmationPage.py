from selenium.webdriver.common.by import By


class ConfirmationPage():
    COUNTRY =  'Turkey'

    def __init__(self, driver):
        self.driver = driver

    country_input_locator = (By.ID, 'country')
    country_in_list_locator = (By.LINK_TEXT, COUNTRY)
    agreement_checkbox_locator = (By.CSS_SELECTOR, 'label[for="checkbox2"]')
    purchase_button_locator = (By.CSS_SELECTOR, 'input[class*="btn-lg"]')

    def enter_country(self):
        return self.driver.find_element(*self.country_input_locator).send_keys(self.COUNTRY[:3])

    def choose_country_in_the_list(self):
        return self.driver.find_element(*self.country_in_list_locator)

    def accept_agreement(self):
        return self.driver.find_element(*self.agreement_checkbox_locator)

    def purchase(self):
        return self.driver.find_element(*self.purchase_button_locator)

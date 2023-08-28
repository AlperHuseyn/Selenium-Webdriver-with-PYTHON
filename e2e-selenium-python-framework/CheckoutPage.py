from ConfirmationPage import ConfirmationPage
from selenium.webdriver.common.by import By


class CheckoutPage():
    BRAND = 'Blackberry'

    def __init__(self, driver):
        self.driver = driver

    products_card_locator = (By.XPATH, '//div[@class="card h-100"]')
    product_title_locator = (By.XPATH, 'div/h4/a')

    def get_product_cards(self):
        return self.driver.find_elements(*self.products_card_locator)

    def add_to_card(self):
        for product in self.get_product_cards():
            brand = product.find_element(*self.product_title_locator).text
            if brand != self.BRAND:
                continue
            return product.find_element(By.XPATH, 'div/button')

    def switch_to_checkout_page(self):
        # CSS_SELECTOR;
        # //tagname[contains(@attribute, 'partial text inside attribute')],
        # tagname[attribute*='partial text inside attribute']
        return self.driver.find_element(By.XPATH, '//a[contains(@class, "btn-primary")]')
    
    def checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[class*="btn-success"]').click()
        return ConfirmationPage(self.driver)
    
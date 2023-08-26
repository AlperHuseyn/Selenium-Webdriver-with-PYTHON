from selenium.webdriver.common.by import By


class HomePage():
    def __init__(self, driver):
        self.driver = driver

    shop_button_locator = (By.LINK_TEXT, 'Shop')

    def shop_button(self):
        return self.driver.find_element(*self.shop_button_locator)

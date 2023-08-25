'Import necessary modules'
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utilities import BaseClass


class TestE2EFramework(BaseClass):
    def test_e2e_framework(self):
        BRAND = 'Blackberry'

        self.driver.find_element(By.LINK_TEXT, 'Shop').click()
        products = self.driver.find_elements(By.XPATH, '//div[@class="card h-100"]')

        for product in products:
            brand = product.find_element(By.XPATH, 'div/h4/a').text
            if brand != BRAND:
                continue
            product.find_element(By.XPATH, 'div/button').click()

        # CSS_SELECTOR;
        # //tagname[contains(@attribute, 'partial text inside attribute')],
        # tagname[attribute*='partial text inside attribute']
        self.driver.find_element(By.XPATH, '//a[contains(@class, "btn-primary")]').click()

        self.driver.find_element(By.CSS_SELECTOR, 'button[class*="btn-success"]').click()

        self.driver.find_element(By.ID, 'country').send_keys('Tur')
        wait = WebDriverWait(self.driver, 10)  # Add a delay
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Turkey")))
        self.driver.find_element(By.LINK_TEXT, "Turkey").click()

        self.driver.find_element(By.CSS_SELECTOR, 'label[for="checkbox2"]').click()

        self.driver.find_element(By.CSS_SELECTOR, 'input[class*="btn-lg"]').click()

        assert 'Success' in self.driver.find_element(By.CSS_SELECTOR, '.alert-success').text
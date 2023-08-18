'Import necessary modules'
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


WEBSITE_URL = r'https://rahulshettyacademy.com/seleniumPractise/#/'
PROMO_CODE = 'rahulshettyacademy'

service = Service()
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)  # Add implicit wait here

driver.get(WEBSITE_URL)

driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys('ber')
sleep(2)  # Add delay here, implicitly_wait not apply here cause find_elements is used
findings = driver.find_elements(By.XPATH, '//div[@class="products"]/div')
assert len(findings) > 0

for item in findings:
    item.find_element(By.XPATH, 'div/button').click()

driver.find_element(By.CSS_SELECTOR, 'img[alt="Cart"]').click()
driver.find_element(By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]').click()
driver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys(PROMO_CODE)
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()
promo_info = driver.find_element(By.CLASS_NAME, 'promoInfo').text
assert 'applied' in promo_info

# Close driver
driver.close()

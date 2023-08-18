'Import necessary modules'
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


WEBSITE_URL = r'https://rahulshettyacademy.com/seleniumPractise/#/'
PROMO_CODE = 'rahulshettyacademy'

service = Service()
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(2)  # Add implicit wait here

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
wait = WebDriverWait(driver, 10)  # Add explicitly wait here
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'promoInfo')))
promo_info = driver.find_element(By.CSS_SELECTOR, '.promoInfo').text
assert 'applied' in promo_info

# Validate discounted prices is always less than total amount
total_amount = int(driver.find_element(By.CSS_SELECTOR, '.totAmt').text)  # Total amount

discounted_amount = float(driver.find_element(By.CLASS_NAME, 'discountAmt').text)

assert discounted_amount < total_amount

# Validate items
expected_list = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']

items_in_chart = driver.find_elements(By.CSS_SELECTOR, 'tr td:nth-child(2) p')
items = []
for item_in_chart in items_in_chart:
    items.append(item_in_chart.text)

assert expected_list == items
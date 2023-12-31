'Import necessary modules'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


WEBSITE_URL = r'https://rahulshettyacademy.com/seleniumPractise/#/'

service = Service()
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(2)  # Add implicit wait here

driver.get(WEBSITE_URL)

driver.find_element(By.LINK_TEXT, 'Top Deals').click()

driver.switch_to.window(driver.window_handles[-1])
driver.find_element(By.CSS_SELECTOR, '.sort-icon').click()
veggies = driver.find_elements(By.XPATH, '//tr/td[1]')

in_table = [veggie.text for veggie in veggies]
assert in_table == sorted(in_table)

# Close the driver
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.close()

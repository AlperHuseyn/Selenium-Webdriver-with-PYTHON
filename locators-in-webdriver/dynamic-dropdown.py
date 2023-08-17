from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep


WEBSITE_URL = r'https://rahulshettyacademy.com/dropdownsPractise/'

service = Service()
driver = webdriver.Chrome(service=service)

driver.get(WEBSITE_URL)

driver.find_element(By.ID, 'autosuggest').send_keys('ind')
sleep(2)  # Add delay to see suggestions
countries = driver.find_elements(By.CSS_SELECTOR, 'li[class="ui-menu-item"] a')

for country in countries:
    if country.text == 'India':
        country.click()
        break
        
assert driver.find_element(By.ID, 'autosuggest').get_attribute('value') == 'India'

# Close driver
driver.close()




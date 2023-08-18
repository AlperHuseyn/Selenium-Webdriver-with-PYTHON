from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


WEBSITE_URL = r'https://rahulshettyacademy.com/AutomationPractice/'

service = Service()
driver = webdriver.Chrome(service=service)

driver.get(WEBSITE_URL)
options = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')

for option in options:
    if option.get_attribute('value') == 'option2':
        option.click()
        assert option.is_selected()
        break

radio_buttons = driver.find_elements(By.CSS_SELECTOR, '.radioButton')

# If we are sure that button positions not change, we can use indexing. Below selecting radio3.
radio_buttons[2].click()
assert radio_buttons[2].is_selected()

"""
for radio_button in radio_buttons:
    if radio_button.get_attribute('value') == 'radio3':
        radio_button.click()
        assert radio_button.is_selected()
        break
"""

assert driver.find_element(By.ID, 'displayed-text').is_displayed()
driver.find_element(By.ID, 'hide-textbox').click()
assert not driver.find_element(By.ID, 'displayed-text').is_displayed()




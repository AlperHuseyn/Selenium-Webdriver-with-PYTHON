from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep


WEBSITE_URL = r'https://rahulshettyacademy.com/AutomationPractice/'
NAME = 'your_name_here'

service = Service()
driver = webdriver.Chrome(service=service)

driver.get(WEBSITE_URL)

driver.find_element(By.CSS_SELECTOR, '#name').send_keys(NAME)
sleep(1)  # Add delay 
driver.find_element(By.ID, 'alertbtn').click()

# Switching to alert mode
alert = driver.switch_to.alert
assert NAME in alert.text
sleep(1)  # Add delay
alert.accept()  # .dismiss() if cancel applicable


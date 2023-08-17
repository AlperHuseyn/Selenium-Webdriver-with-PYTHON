from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


WEBSITE_URL = r'https://rahulshettyacademy.com/client'
EMAIL = 'your_email@example.com'
PASSWORD = 'your_password_here'
NAME = 'your_name_here'

service = Service()
driver = webdriver.Chrome(service=service)

driver.get(WEBSITE_URL)
# LINK_TEXT locator
driver.find_element(By.LINK_TEXT, 'Forgot password?').click()
driver.find_element(By.XPATH, '//form/div[1]/input').send_keys(EMAIL)  # Using tagnames only for creating XPATHs if there is no unique attribute, email input
driver.find_element(By.CSS_SELECTOR, 'form div:nth-child(2) input').send_keys(PASSWORD) # Using tagnames to create CSS_SELECTOR, password input
driver.find_element(By.ID, 'confirmPassword').send_keys(PASSWORD)
driver.find_element(By.XPATH, '//button[text()="Save New Password"]').click()

# Close driver
driver.close()


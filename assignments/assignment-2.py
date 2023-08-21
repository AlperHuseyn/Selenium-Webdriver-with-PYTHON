'Import necessary modules'
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


WEBSITE_URL = r'https://rahulshettyacademy.com/loginpagePractise/'

service = Service()
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get(WEBSITE_URL)

driver.find_element(By.CSS_SELECTOR, '.blinkingText').click()
driver.switch_to.window(driver.window_handles[-1])
email = driver.find_element(By.LINK_TEXT, 'mentor@rahulshettyacademy.com').text
driver.close()

driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.ID, 'username').send_keys(email)
driver.find_element(By.NAME, 'password').send_keys('dummy_password')
driver.find_element(By.NAME, 'signin').click()

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.alert')))
print(driver.find_element(By.CSS_SELECTOR, '.alert').text)

driver.close()


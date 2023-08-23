'Import necessary modules'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


WEBSITE_URL = r'https://rahulshettyacademy.com/AutomationPractice'

service = Service()
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get(WEBSITE_URL)

driver.switch_to.frame('iframe-name')
driver.find_element(By.LINK_TEXT, 'Courses').click()

driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, 'h1').text)

# Close the driver
driver.close()

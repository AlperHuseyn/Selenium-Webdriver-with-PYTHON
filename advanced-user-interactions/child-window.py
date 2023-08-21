'Import necessary modules'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


WEBSITE_URL = r'https://randomfox.ca/'

service = Service()
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get(WEBSITE_URL)

driver.find_element(By.LINK_TEXT, 'GitHub').click()
driver.switch_to.window(driver.window_handles[-1])
assert 'xinitrc-dev' == driver.find_element(By.LINK_TEXT, 'xinitrc-dev').text
driver.close()
driver.switch_to.window(driver.window_handles[0])
assert 'Add more floof!' == driver.find_element(By.LINK_TEXT, 'Add more floof!').text
driver.close()

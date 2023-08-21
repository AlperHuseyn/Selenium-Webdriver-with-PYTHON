'Import necessary modules'
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


WEBSITE_URL = r'https://www.youtube.com'

service = Service()
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get(WEBSITE_URL)

actions = ActionChains(driver)


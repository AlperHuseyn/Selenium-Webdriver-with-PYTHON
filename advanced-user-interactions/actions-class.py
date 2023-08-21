'Import necessary modules'
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


WEBSITE_URL = r'https://rahulshettyacademy.com/AutomationPractice/'

service = Service()
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get(WEBSITE_URL)
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, 'mousehover')).perform()
# action.context_click(driver.find_element(By.LINK_TEXT, 'Top')).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, 'Reload')).click().perform()

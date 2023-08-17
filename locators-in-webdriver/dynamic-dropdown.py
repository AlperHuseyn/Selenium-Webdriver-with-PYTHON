from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


WEBSITE_URL = r'https://rahulshettyacademy.com/dropdownsPractise/'
EMAIL = 'your_email@example.com'
PASSWORD = 'your_password_here'
NAME = 'your_name_here'

service = Service()
driver = webdriver.Chrome(service=service)

driver.get(WEBSITE_URL)
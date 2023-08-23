'Import necessary modules'
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


WEBSITE_URL = r'https://rahulshettyacademy.com/angularpractice/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('headless')
chrome_options.add_argument('--ignore-certificate-errors')

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(2)  # Add implicit wait here

driver.get(WEBSITE_URL)
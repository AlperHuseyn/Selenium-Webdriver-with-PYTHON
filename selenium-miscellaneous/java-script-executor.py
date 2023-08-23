'Import necessary modules'
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


WEBSITE_URL = r'https://rahulshettyacademy.com/AutomationPractice'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('--ignore-certificate-errors')

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get(WEBSITE_URL)

driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')
driver.get_screenshot_as_file('screen.png')

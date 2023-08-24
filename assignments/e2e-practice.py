'Import necessary modules' 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BRAND = 'Blackberry'
WEBSITE_URL = r'https://rahulshettyacademy.com/angularpractice/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--ignore-certificate-errors')

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(2)  # Add implicit wait here

driver.get(WEBSITE_URL)

driver.find_element(By.LINK_TEXT, 'Shop').click()

products = driver.find_elements(By.XPATH, '//div[@class="card h-100"]')

for product in products:
    brand = product.find_element(By.XPATH, 'div/h4/a').text
    if brand != BRAND:
        continue
    product.find_element(By.XPATH, 'div/button').click()

# CSS_SELECTOR; //tagname[contains(@attribute, 'partial text inside attribute')], tagname[attribute*='partial text inside attribute']
driver.find_element(By.XPATH, '//a[contains(@class, "btn-primary")]').click()

driver.find_element(By.CSS_SELECTOR, 'button[class*="btn-success"]').click()

driver.find_element(By.ID, 'country').send_keys('Tur')
wait = WebDriverWait(driver, 10)  # Add a delay
wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Turkey")))
driver.find_element(By.LINK_TEXT, "Turkey").click()

driver.find_element(By.CSS_SELECTOR, 'label[for="checkbox2"]').click()

driver.find_element(By.CSS_SELECTOR, 'input[class*="btn-lg"]').click()

assert 'Success' in driver.find_element(By.CSS_SELECTOR, '.alert-success').text 


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select


WEBSITE_URL = r'https://rahulshettyacademy.com/angularpractice/'
EMAIL = 'your_email@example.com'
PASSWORD = 'your_password_here'
NAME = 'tour_name_here'

service = Service()
driver = webdriver.Chrome(service=service)

driver.get(WEBSITE_URL)

driver.find_element(By.NAME, 'email').send_keys(EMAIL)
driver.find_element(By.ID, 'exampleInputPassword1').send_keys(PASSWORD)
driver.find_element(By.ID, 'exampleCheck1').click()

# tagname[attribute='value'] custom CSS SELECTOR; #id; .classname
driver.find_element(By.CSS_SELECTOR, 'input[name="name"]').send_keys(NAME)
driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()

# Static dropdown
drop_down = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
# drop_down.select_by_visible_text('Female')
drop_down.select_by_index(0)  # Male
# drop_down.select_by_value('male')  # if applicable

# //tagname[@attribute='value'] custom XPATH
driver.find_element(By.XPATH, '//input[@type="submit"]').click()  # Submit button
message = driver.find_element(By.CLASS_NAME, 'alert-success').text  # Alert after submitting
print(message)

# Validation
assert 'Success' in message

driver.find_element(By.XPATH, '(//input[@type="text"])[3]').send_keys(', middle name huseyin')
driver.find_element(By.XPATH, '(//input[@type="text"])[3]').clear()

# Close driver
driver.close()




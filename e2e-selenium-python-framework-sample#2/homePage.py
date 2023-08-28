from selenium.webdriver.common.by import By


class HomePage():
    def __init__(self, driver):
        self.driver = driver
        
    email_input_locator = (By.NAME, 'email')
    password_input_locator = (By.ID, 'exampleInputPassword1')
    checkbox_locator = (By.ID, 'exampleCheck1')
    # tagname[attribute='value'] custom CSS SELECTOR; #id; .classname
    name_input_locator = (By.CSS_SELECTOR, 'input[name="name"]')
    employment_status_locator = (By.CSS_SELECTOR, '#inlineRadio1')
    submit_button_locator = (By.XPATH, '//input[@type="submit"]')
    alert_locator = (By.CLASS_NAME, 'alert-success')
    
    def get_email(self):
        return self.driver.find_element(*self.email_input_locator)
    
    def get_password(self):
        return self.driver.find_element(*self.password_input_locator)
    
    def tick_checkbox(self):
        return self.driver.find_element(*self.checkbox_locator)
    
    def get_name(self):
        return self.driver.find_element(*self.name_input_locator)
    
    def tick_radio_button(self):
        return self.driver.find_element(*self.employment_status_locator)
    
    def submit(self):
        return self.driver.find_element(*self.submit_button_locator)
    
    def get_success_message(self):
        return self.driver.find_element(*self.alert_locator)

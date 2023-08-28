from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        
    email_input_locator = (By.NAME, 'email')
    password_input_locator = (By.ID, 'exampleInputPassword1')
    checkbox_locator = (By.ID, 'exampleCheck1')
    # tagname[attribute='value'] custom CSS SELECTOR; #id; .classname
    name_input_locator = (By.CSS_SELECTOR, 'input[name="name"]')
    employment_status_locator = (By.CSS_SELECTOR, '#inlineRadio1')
    dropdown_locator = (By.ID, 'exampleFormControlSelect1')
    submit_button_locator = (By.XPATH, '//input[@type="submit"]')
    
    def enter_email(self):
        return self.driver.find_element(*self.email_input_locator)
    
    def enter_password(self):
        return self.driver.find_element(*self.password_input_locator)
    
    def tick_checkbox(self):
        return self.driver.find_element(*self.checkbox_locator)
    
    def enter_name(self):
        return self.driver.find_element(*self.name_input_locator)
    
    def tick_radio_button(self):
        return self.driver.find_element(*self.employment_status_locator)
    
    def choose_dropdpwn_option_by_text(self, text):
        dropdown = Select(self.driver.find_element(*self.dropdown_locator))
        return dropdown.select_by_visible_text(text)
    
    def submit(self):
        return self.driver.find_element(*self.submit_button_locator)

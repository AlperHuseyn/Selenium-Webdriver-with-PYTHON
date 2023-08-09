"""
Please note that this script serves as a demonstration and cannot be used directly without modifications. It showcases 
techniques for automating tasks such as accessing a website, logging in, interacting with elements using Selenium, and 
controlling OBS Studio through its WebSocket plugin. To adapt this script for your specific use case, carefully review and 
replace the XPATHs, URLs, login credentials, and OBS WebSocket connection details with values relevant to your target website 
and OBS setup. Understanding and applying the concepts presented here will help you create a customized automation solution 
tailored to your requirements.

Author: Alper Huseyin DOGAN
"""

from obswebsocket import obsws, requests
from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class ObsRecorder():
    def __init__(self):
        self.driver = webdriver.Edge()  # Default web browser is Edge in my case, change if necessary
        self.wait = WebDriverWait((self.driver), 10)
        
    def open_website(self, url):
        self.driver.get(url)
        self.driver.maximize_window()  # Maximizes the browser window
    
    def click_elem(self, locator):
        elem = self.wait.until(EC.element_to_be_clickable(locator))
        elem.click()
        
    def enter_text(self, locator, text):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.send_keys(text)
        
    def login(self, email, password):
        sign_in_locator = (By.XPATH, '//a[contains(text(), "Giriş Yap")]')
        self.click_elem(sign_in_locator)
        
        email_locator = (By.XPATH, '//*[@id="Input_Email"]')
        password_locator = (By.XPATH, '//*[@id="Input_Password"]')
        submit_locator = (By.XPATH, '//*[@id="account"]/div[5]/button')
        
        self.enter_text(email_locator, email)
        self.enter_text(password_locator, password)
        self.click_elem(submit_locator)
        
    def get_video_password(self, video_num):
        video_password_locator = (By.XPATH, f'/html/body/div/main/table/tbody/tr[{video_num}]/td[2]/div')
        video_password_elem = self.wait.until(EC.visibility_of_element_located(video_password_locator))
        return video_password_elem.text
    
    def open_video_link(self, video_num):
        video_link_locator = (By.XPATH, f'/html/body/div/main/table/tbody/tr[{video_num}]/td[1]/a')
        self.click_elem(video_link_locator)
        
        # Switch to the newly opened tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
    
    def set_video_speed(self, speed):
        # Execute JavaScript to change video playback speed
        self.driver.execute_script(f'document.querySelector("video").playbackRate = {speed}')
    
    def expand_video_to_fullscreen(self):
        current_url = self.driver.current_url
        id = current_url[current_url.rfind('/') + 1:]
        video_elem = self.driver.find_element(By.XPATH, f'//*[@id="{id}"]/div[4]')
        actions = ActionChains((self.driver))
        actions.double_click(video_elem).perform()
        
    def open_OBS_studio_and_record(self):
        host = 'xx.xxx.xx.x'  # your host name
        port = 4455
        password = 'xxxxxxxxxxxxxxxx'  # your password for OBS connection
        
        try:
            print("Connecting to OBS WebSocket server...")
            obs_ws = obsws(host, port, password)
            obs_ws.connect()
            
            print("Connected to OBS WebSocket server.")
            
            print("Sending request to start recording...")
            response = obs_ws.call(requests.StartRecord())
            if response.status:    
                print("Recording started successfully. Response: ", response.status)
                print("Waiting for video to finish...")
                sleep(10)  # Change here, it should be the video lenght in seconds.
            else:
                print("Failed to start recording. Response: ", response.status)
            print("Disconnecting from OBS WebSocket server...")
            obs_ws.disconnect()
            print("Disconnected from OBS WebSocket server.")
        except Exception as e:
            print("Failed to start recording:", str(e))            
            
    def close_OBS_studio_and_stop_recording(self):
        host = 'xx.xxx.xx.x'  # your host name
        port = 4455
        password = 'xxxxxxxxxxxxxxxx'  # your password for OBS connection
        
        try:
            print("Connecting to OBS WebSocket server...")
            obs_ws = obsws(host, port, password)
            obs_ws.connect()
            
            print("Connected to OBS WebSocket server.")
    
            print("Sending request to stop recording...")
            response = obs_ws.call(requests.StopRecord())
            if response.status:
                print("Recording stopped successfully. Response: ", response.status)
            else:
                print("Failed to stop recording Response: ", response.status)
    
            print("Disconnecting from OBS WebSocket server...")
            obs_ws.disconnect()
            print("Disconnected from OBS WebSocket server.")
        except Exception as e:
            print("Failed to stop recording: ", str(e))

def main():    
    start_video_num = 61
    end_video_num = 61
    
    for video_num in range(start_video_num, end_video_num - 1,  -1):
        obs = ObsRecorder()
        obs.open_website(r'https://example.com/')  # The website contains the video
        obs.login('example@xyz.com', 'xxxxxxxx')  # Login info    
        obs.click_elem((By.XPATH, '/html/body/header/nav/div/div/ul[2]/li[2]/a'))
        obs.click_elem((By.XPATH, '/html/body/div/main/table/tbody/tr[2]/td[1]/a'))    
        
        password = obs.get_video_password(video_num)
        obs.open_video_link(video_num)    
        obs.enter_text((By.XPATH, '//*[@id="password"]'), password)
        obs.click_elem((By.XPATH, '//*[@id="pw_form"]/input[5]'))
        obs.set_video_speed(2)
        obs.expand_video_to_fullscreen()
        obs.open_OBS_studio_and_record()
        obs.close_OBS_studio_and_stop_recording()
        
        obs.driver.close()
        
    input('Press enter for closing the browser...')


if __name__ == '__main__':
    main()
    
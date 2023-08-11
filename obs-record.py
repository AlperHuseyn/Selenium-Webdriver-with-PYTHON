"""
Please note that this script serves as a demonstration and cannot be used directly without modifications. It showcases 
techniques for automating tasks such as accessing a website, logging in, interacting with elements using Selenium, and 
controlling OBS Studio through its WebSocket plugin. To adapt this script for your specific use case, carefully review and 
replace the XPATHs, URLs, login credentials, and OBS WebSocket connection details with values relevant to your target website 
and OBS setup. Understanding and applying the concepts presented here will help you create a customized automation solution 
tailored to your requirements.

Author: Alper Huseyin DOGAN
"""

import colorama
from colorama import Back
colorama.init(autoreset=True)
from obswebsocket import obsws, requests
from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

        
class ObsRecorder():
    def __init__(self, host, port, password):
        self.driver = webdriver.Edge()  # choose a browser
        self.wait = WebDriverWait((self.driver), 10)
        self.host = host
        self.port = port
        self.password= password
        
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
        # Get the current playback speed and check if it's set correctly
        curr_speed = self.driver.execute_script('return document.querySelector("video").playbackRate')
        
        if curr_speed == speed:
            print(Back.GREEN + f'Video speed set to x{speed} successfully.' + '\033[39m')
        else:
            print(Back.RED + 'Video speed was not set correctly.' + '\033[39m')
    
    def get_current_video_id(self):
        current_url = self.driver.current_url
        return current_url[current_url.rfind('/') + 1:]
    
    def expand_video_to_fullscreen(self):
        id = self.get_current_video_id()
        video_elem = self.driver.find_element(By.XPATH, f'//*[@id="{id}"]/div[4]')
        
        # Get the initial size of the video element
        initial_size = video_elem.size
        
        # Double click to expand the window
        actions = ActionChains((self.driver))
        actions.double_click(video_elem).perform()
        
        # Get the initial size of the video element
        updated_size = video_elem.size
        
        if updated_size != initial_size:
            print(Back.GREEN + 'Video maximized successfully.' + '\033[39m')
        else:
            print(Back.GREEN + 'Video was not maximized correctly.' + '\033[39m')
            
    def open_OBS_studio_and_record(self):
        try:
            print("Connecting to OBS WebSocket server...")
            obs_ws = obsws(host=self.host, port=self.port, password=self.password)
            obs_ws.connect()
            
            print(Back.GREEN + "Connected to OBS WebSocket server." + '\033[39m')
            
            print("Sending request to start recording...")
            response = obs_ws.call(requests.StartRecord())
            if response.status:    
                print(Back.GREEN + "Recording started successfully" + '\033[39m' + ". Response:", Back.GREEN + str(response.status) + '\033[39m')
                print("Waiting for video to finish...")
                
            else:
                print(Back.RED + "Failed to start recording. Response:", str(response.status) + '\033[39m')
            print("Disconnecting from OBS WebSocket server...")
            obs_ws.disconnect()
            print("Disconnected from OBS WebSocket server.")
        except Exception as e:
            print("Failed to start recording:", str(e))            
            
    def close_OBS_studio_and_stop_recording(self):
        try:
            print("Connecting to OBS WebSocket server...")
            obs_ws = obsws(host=self.host, port=self.port, password=self.password)
            obs_ws.connect()
            
            print(Back.GREEN + "Connected to OBS WebSocket server." + '\033[39m')
    
            print("Sending request to stop recording...")
            response = obs_ws.call(requests.StopRecord())
            if response.status:
                print(Back.GREEN + "Recording stopped successfully" + '\033[39m' + ". Response:", Back.GREEN + str(response.status) + '\033[39m')
            else:
                print(Back.RED + "Failed to stop recording. Response:", str(response.status) + '\033[39m')
    
            print("Disconnecting from OBS WebSocket server...")
            obs_ws.disconnect()
            print("Disconnected from OBS WebSocket server.")
        except Exception as e:
            print("Failed to stop recording: ", str(e))
    
    def is_player_ended(self):
        return self.driver.execute_script("""
            var video = document.querySelector("video");
            return video.ended || (video.currentTime >= video.duration);
        """)

def main():        
    start_video_num = 49  # Change here
    end_video_num = 39  # change here
    for course_num, video_num in enumerate(range(start_video_num, end_video_num - 1,  -1), start=48):
        obs = ObsRecorder(host='xxx.xxx.x.xx', port=4455, password='xxxxxxxxxxxxxxxx')    
        obs.open_website(r'https://example.org/')  # The website contains the video        
        obs.login('example@xyz.com', 'xxxxxxxx')  # Login info            
        obs.click_elem((By.XPATH, '/html/body/header/nav/div/div/ul[2]/li[2]/a'))        
        obs.click_elem((By.XPATH, '/html/body/div/main/table/tbody/tr[2]/td[1]/a'))                
        password = obs.get_video_password(video_num)
        obs.open_video_link(video_num)    
        obs.enter_text((By.XPATH, '//*[@id="password"]'), password)
        obs.click_elem((By.XPATH, '//*[@id="pw_form"]/input[5]'))
        print('#-----------------------------------------#')
        print(f'## ders {course_num} ##')
        obs.set_video_speed(2)        
        obs.expand_video_to_fullscreen()
        obs.open_OBS_studio_and_record()
        
        while True:
            if obs.is_player_ended():
                obs.close_OBS_studio_and_stop_recording()
                break
        
        obs.driver.close()
    
    print('#-----------------------------------------#')
    input('Press enter for closing the browser...')


if __name__ == '__main__':
    main()
    
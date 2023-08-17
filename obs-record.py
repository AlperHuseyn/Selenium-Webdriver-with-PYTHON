"""
Please note that this script serves as a demonstration and cannot be used 
directly without modifications. It showcases techniques for automating tasks 
such as accessing a website, logging in, interacting with elements using 
Selenium, and controlling OBS Studio through its WebSocket plugin. To adapt 
this script for your specific use case, carefully review and replace the 
XPATHs, URLs, login credentials, and OBS WebSocket connection details with 
values relevant to your target website and OBS setup. Understanding and 
applying the concepts presented here will help you create a customized 
automation solution tailored to your requirements.

Author: Alper Huseyin DOGAN
"""

import colorama
from colorama import Back
colorama.init(autoreset=True)
from obswebsocket import obsws, requests
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class VideoAutomation():
    """
    This class handles various tasks related to web automation, including 
    logging in, navigating to videos, setting playback speed, etc.
    """
    WEBSITE_URL = r'https://course.csystem.org/'
    LOGIN_EMAIL = 'your_email@example.com'  # Replace with your login email
    LOGIN_PASSWORD = 'your_password_here'  # Replace with your login password

    def __init__(self):
        """
        Initialize the Selenium WebDriver.
        Note: The default web browser used here is Microsoft Edge. 
        Modify this line as needed, to use a different web browser (e.g., Firefox, Chrome).
        """
        self.service = Service()
        self.driver = webdriver.Edge(service=self.service)
        self.wait = WebDriverWait((self.driver), 10)

    def open_website(self):
        self.driver.get(self.WEBSITE_URL)
        self.driver.maximize_window()  # Maximizes the browser window

    def click_elem(self, locator):
        elem = self.wait.until(EC.element_to_be_clickable(locator))
        elem.click()

    def enter_text(self, locator, text):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.send_keys(text)

    def login(self):
        sign_in_locator = (By.CSS_SELECTOR, 'a[href="/Identity/Account/Login"]')  # Giriş Yap
        self.click_elem(sign_in_locator)

        email_locator = (By.ID, 'Input_Email')
        password_locator = (By.ID, 'Input_Password')
        submit_locator = (By.CSS_SELECTOR, 'button[type="submit"]')

        self.enter_text(email_locator, self.LOGIN_EMAIL)
        self.enter_text(password_locator, self.LOGIN_PASSWORD)
        self.click_elem(submit_locator)

    def get_video_password(self, video_selector_num):
        video_password_locator = (By.CSS_SELECTOR, f'''body > div > main >
                                  table > tbody > 
                                  tr:nth-child({video_selector_num}) > 
                                  td:nth-child(2) > div''')
        video_password_elem = self.wait.until(EC.visibility_of_element_located(video_password_locator))
        return video_password_elem.text

    def open_video_link(self, video_selector_num):
        video_link_locator = (By.CSS_SELECTOR, f'''body > div > main > table >
                              tbody > tr:nth-child({video_selector_num}) > 
                              td:nth-child(1) > a''')
        self.click_elem(video_link_locator)

        # Switch to the newly opened tab
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_course_title(self):
        return self.driver.title[:2]  # first two character to get course number

    def set_video_speed(self, speed):
        # Execute JavaScript to change video playback speed
        self.driver.execute_script(f'document.querySelector("video").playbackRate = {speed}')

        sleep(1)  # Add a delay to give the video player time to process the speed change

        # Get the current playback speed and check if it's set correctly
        curr_speed = self.driver.execute_script('''return document.
                                                querySelector("video").
                                                playbackRate''')

        if curr_speed == speed:
            print(Back.GREEN + f'Video speed set to x{speed} successfully.' + '\033[39m')
        else:
            print(Back.YELLOW + 'Video speed was not set correctly.' + '\033[39m')

    def get_current_video_id(self):
        current_url = self.driver.current_url
        return current_url[current_url.rfind('/') + 1:]

    def expand_video_to_fullscreen(self):
        video_id = self.get_current_video_id()
        video_elem = self.driver.find_element(By.ID, f'{video_id}')

        # Get the initial size of the video element
        initial_size = video_elem.size

        # Double click to expand the window
        actions = ActionChains((self.driver))
        actions.double_click(video_elem).perform()

        # Add delay for video player to process double click action
        sleep(1)

        # Get the updated size of the video element
        updated_size = video_elem.size

        if updated_size != initial_size:
            print(Back.GREEN + 'Video maximized successfully.' + '\033[39m')
        else:
            print(Back.RED+'Video was not maximized correctly.'+ '\033[39m')
            return

    def is_player_ended(self):
        return self.driver.execute_script("""
            var video = document.querySelector("video");
            return video.ended || (video.currentTime >= video.duration);
        """)

# Define the ObsRecorder class for OBS interactions
class ObsRecorder():
    """
    This class manages interactions with OBS Studio via the OBS WebSocket API.
    """
    OBS_HOST = 'your_obs_host_ip'  # Replace with your OBS host IP
    OBS_PORT = 4455
    OBS_PASSWORD = 'your_obs_password'  # Replace with your OBS password

    def __init__(self):
        """
        Initializes the OBS WebSocket connection.
        """
        self.obs_ws = obsws(host=self.OBS_HOST, port=self.OBS_PORT, password=self.OBS_PASSWORD)

    def obs_connect(self):
        self.obs_ws.connect()

    def obs_disconnect(self):
        self.obs_ws.disconnect()

    def obs_record_request(self, record_request):
        return self.obs_ws.call(record_request)

    def perform_recording_request(self, request):
        try:
            print("Connecting to OBS WebSocket server...")
            self.obs_connect()

            print(Back.GREEN + "Connected to OBS WebSocket server." + '\033[39m')

            print("Sending request to take necessary recording action...")
            response = self.obs_record_request(request)
            if response.status:
                print(Back.GREEN + "SUCCESS. Response: " +
                      str(response.status) + r'\033[39m')
                print("Waiting for video to finish...")

            else:
                print(Back.RED + "Failed recording action. Response:",
                      str(response.status) + r'\033[39m')
                return

        except Exception as e:
            print(Back.RED + "Failed recording action. Response:",
                  str(e) + r'\033[39m')      
            return

        finally:
            print("Disconnecting from OBS WebSocket server...")
            self.obs_disconnect()
            print("Disconnected from OBS WebSocket server.")

    def start_recording(self):
        start_request = requests.StartRecord()
        self.perform_recording_request(start_request)

    def stop_recording(self):
        stop_request = requests.StopRecord()
        self.perform_recording_request(stop_request)

def main():
    start_video_selector_num = 42
    end_video_selector_num = 41
    for video_selector_num in range(start_video_selector_num, end_video_selector_num - 1,  -1):
        video_automation = VideoAutomation()
        video_automation.open_website()
        video_automation.login()
        video_automation.click_elem((By.CSS_SELECTOR, 'a[href="/UsersCourses"]'))
        video_automation.click_elem((By.CSS_SELECTOR, 'a[href="/UsersCourses/Details/29"]'))

        video_password = video_automation.get_video_password(video_selector_num)
        video_automation.open_video_link(video_selector_num)
        video_automation.enter_text((By.ID, 'password'), video_password)
        video_automation.click_elem((By.CSS_SELECTOR,'input[type="submit"]'))
        print('#-----------------------------------------#')
        print(f'Course number: {video_automation.get_course_title()}')
        video_automation.set_video_speed(2)
        video_automation.expand_video_to_fullscreen()

        obs_recorder = ObsRecorder()
        obs_recorder.start_recording()

        while True:
            if video_automation.is_player_ended():
                obs_recorder.stop_recording()
                break

        video_automation.driver.close()

    print('#-----------------------------------------#')
    input('Press enter for closing the browser...')


if __name__ == '__main__':
    main()

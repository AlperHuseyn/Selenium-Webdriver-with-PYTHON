import inspect
import logging
import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('setup')
class BaseClass():
    def choose_dropdown_option_by_text(self, locator, text):
        dropdown = Select(self.driver.find_element(*locator))
        return dropdown.select_by_visible_text(text)
    
    def get_logs(self):
        # Get name of the calling function for contextual logging.
        logger_name = inspect.stack()[1][3]
        # Create a logger instance using the calling function's name.
        logger = logging.getLogger(logger_name)
        # Create a file handler to write logs to a file named 'logfile.log'.
        file_handler = logging.FileHandler('logfile.log')
        logger.addHandler(file_handler)
        # Define a log message format with timestamp, log level, logger name, and message.
        formatter = logging.Formatter('%(asctime)s :%(levelname)s :%(name)s :%(message)s')
        file_handler.setFormatter(formatter)
        # Set the logging level to INFO, meaning it will capture messages of INFO level and above.
        logger.setLevel(logging.INFO)
        
        return logger

import inspect
import logging
import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('setup')
class BaseClass():
    def choose_dropdown_option_by_text(self, locator, text):
        dropdown = Select(self.driver.find_element(*locator))
        return dropdown.select_by_visible_text(text)
    
    loggers = {}  # Store loggers to prevent duplicate handlers
    
    def get_logs(self, logger_name):
        if logger_name not in self.loggers:
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
            self.loggers[logger_name] = logger
        else:
            logger = self.loggers[logger_name]
        
        return logger
    
    def get_unique_logger_name(self):
        # Get name of the calling function for contextual logging.
        caller_name = inspect.stack()[1][3]
        class_name = self.__class__.__name__
        unique_logger_name = f'{class_name}.{caller_name}'
        return unique_logger_name

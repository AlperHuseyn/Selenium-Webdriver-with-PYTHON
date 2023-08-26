import logging
import pytest


@pytest.mark.usefixtures('setup')
class BaseClass:
    def get_logs(self):
        logger = logging.getLogger(__name__)
        file_handler =logging.FileHandler('logfile.log')
        logger.addHandler(file_handler)
        formatter = logging.Formatter('%(asctime)s :%(levelname)s :%(name)s :%(message)s')
        file_handler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        
        return logger
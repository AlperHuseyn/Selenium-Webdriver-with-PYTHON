import pytest
from selenium import webdriver


WEBSITE_URL = r'https://rahulshettyacademy.com/angularpractice/'

def pytest_addoption(parser):
    parser.addoption(
        '--browser-name', action='store', default='edge'
        )

@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption('--browser-name')

    if browser_name == 'chrome':
        service = webdriver.ChromeService()
        driver = webdriver.Chrome(service=service)

    elif browser_name == 'edge':
        service = webdriver.EdgeService()
        driver = webdriver.Edge(service=service)
        
    # Other browsers can be added as well.

    driver.get(WEBSITE_URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

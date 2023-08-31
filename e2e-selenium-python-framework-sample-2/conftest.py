import datetime
import pytest
import os
from selenium import webdriver
driver = None


DEV = r'https://rahulshettyacademy.com/angularpractice/'
# PROD = r'https://rahulshettyacademy.com/angularpractice/'  

def pytest_addoption(parser):
    parser.addoption(
        '--browser-name', action='store', default='edge'
    )  
     
    parser.addoption(
        '--url', action='store', default='dev'
    )
    

@pytest.fixture(scope='class')
def setup(request):
    global driver

    browser_name = request.config.getoption('--browser-name')
    assert browser_name in ['chrome', 'edge']

    if browser_name == 'chrome':
        service = webdriver.ChromeService()
        driver = webdriver.Chrome(service=service)

    elif browser_name == 'edge':
        service = webdriver.EdgeService()
        driver = webdriver.Edge(service=service)

    # Other browsers can be added as well.
    
    url = request.config.getoption('--url')
    assert url in ['dev', 'prod']

    if url == 'dev':
        driver.get(DEV)
    
    elif url == 'prod':
        driver.get(PROD)
    
    # driver.get(DEV)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

def _capture_screenshot(name):
    # global driver
    driver.get_screenshot_as_file(name)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report,
        whenever test fails.
        :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    cwd = os.getcwd()
    current_datetime = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    report_dir = cwd + '\\reports'
    
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    config.option.htmlpath = os.path.join(report_dir, f'{current_datetime}.html')

import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser............")
    elif browser=='edge':
        driver=webdriver.Edge()
        print("Launching edge browser......")
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'Clover Assessment Framework'
        config._metadata['Module Name'] = 'Search Engine'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("SEARCH", None)
    metadata.pop("Plugins", None)



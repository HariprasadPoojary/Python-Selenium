import pytest
import time
from Basics.test_framework.base.web_drivers import WebDrivers
from Basics.test_framework.utilities.logger import InfoLogger

@pytest.fixture()
def setup():
    pass

@pytest.fixture(scope="class")
def class_setup(request, browser):
    log = InfoLogger('debug').info_logger()
    log.info("Conftest running now")
    log.info(f"Running on Browser {browser}")
    wd = WebDrivers(browser)
    driver = wd.get_webdriver_instance()
    request.cls.driver = driver
    yield driver
    time.sleep(3)
    driver.quit()
    log.info("Conftest ran")

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Options for --browser | chrome | ie | opera")

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")

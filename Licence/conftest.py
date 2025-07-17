import pytest
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import chromedriver_autoinstaller
import geckodriver_autoinstaller
import os

# ------------------- Logging Setup -------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ------------------- Auto-install Drivers -------------------
chromedriver_autoinstaller.install()
geckodriver_autoinstaller.install()

# ------------------- Pytest CLI Option -------------------
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox"
    )

# ------------------- WebDriver Fixture -------------------
@pytest.fixture(scope="function")
def setup(request):
    browser = request.config.getoption("--browser").lower()
    
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        service = FirefoxService()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()

    try:
        driver.set_page_load_timeout(10)
        driver.get("http://172.31.52.38:9090")
    except Exception as e:
        logging.error(f"Page load timeout or navigation error: {e}")

    yield driver

    # Screenshot on test failure
       # Screenshot on test failure
    if request.node.rep_call.failed:
        timestamp = time.strftime('%Y%m%d%H%M%S')
        screenshot_dir = './screenshots'
        os.makedirs(screenshot_dir, exist_ok=True)  # Ensure folder exists
        screenshot_path = f'{screenshot_dir}/failed_test_{timestamp}.png'
        driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshot saved to: {screenshot_path}")


    driver.quit()

# ------------------- Hook for capturing test result -------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)

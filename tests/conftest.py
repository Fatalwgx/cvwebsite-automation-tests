import os
import pytest
from selene.support.shared import browser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from lzavodskov.controls import attach


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = os.getenv('selene.base_url', 'http://api:80')
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.hold_browser_open = (
        os.getenv('selene.hold_browser_open', 'false').lower() == 'true'
    )
    browser.config.timeout = float(os.getenv('selene.timeout', '3'))
    browser.config.window_width = 1920
    browser.config.window_height = 1080


DEFAULT_BROWSER_VERSION = "112.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='112.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    remote_drv = os.getenv('REMOTE_DRV')
    driver = webdriver.Remote(
        command_executor=f'{remote_drv}',
        options=options
    )
    browser.config.driver = driver

    yield browser

    attach.add_html
    attach.add_logs
    attach.add_screenshot
    attach.add_video

    browser.quit()

import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    options = Options()
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(options=options)
    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1020
    yield
    browser.quit()
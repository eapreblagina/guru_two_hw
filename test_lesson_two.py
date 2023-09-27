from selene.support.shared import browser
from selene import be, have
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


@pytest.fixture(scope='session', autouse=True)
def browser_settings():
    browser.config.window_width = 1920
    browser.config.window_height = 1020
    yield
    browser.quit()

def test_one(browser_settings):
    options = Options()
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(options=options)
    browser.config.driver = driver

    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests'))


def test_two(browser_settings):
    options = Options()
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(options=options)
    browser.config.driver = driver

    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('fhkefbjhwfbhjbdbfjfbwqfb').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))

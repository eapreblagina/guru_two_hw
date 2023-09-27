from selene.support.shared import browser
from selene import be, have


def test_one(browser_settings):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser'))


def test_two(browser_settings):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('fhkefbjhwfbhjbdbfjfbwqfb').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))

from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture(scope='module')
def window_size():
    browser.config.window_height = 1080
    browser.config.window_width = 1920


def test_find_link_positive():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_find_link_negative():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('kjfjfrieo').press_enter()
    browser.element('[class="card-section"]').should(have.text('не найдено'))

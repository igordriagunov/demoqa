import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utils.browser import setup_browser


@pytest.fixture(scope='module')
def browser():
    browser = setup_browser('chrome')  # Ввести chrome или firefox
    yield browser
    browser.close()
    browser.quit()

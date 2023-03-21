import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='module')
def browser():
    import chromedriver_binary
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver

    driver.close()
    driver.quit()

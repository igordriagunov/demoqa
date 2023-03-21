from selenium import webdriver


def setup_browser(browser_name=None):
    if browser_name == 'chrome':
        browser = chrome_browser()
    elif browser_name == 'firefox':
        browser = firefox_browser()
    else:
        raise Exception(f'Browser {browser_name} не найден!')
    return browser


def chrome_browser():
    import chromedriver_binary
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)
    return browser


def firefox_browser():
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from webdriver_manager.firefox import GeckoDriverManager

    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    browser.maximize_window()
    browser.implicitly_wait(5)
    return browser

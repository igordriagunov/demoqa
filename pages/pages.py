import abc

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(abc.ABC):
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def open_page(self, url):
        self.browser.get(url)

    def find_element(self, locator):
        return self.browser.find_element(By.XPATH, locator)

    def find_elements(self, locator):
        return self.browser.find_elements(By.XPATH, locator)

    def find_element_than_click(self, element):
        self.browser.find_element(By.XPATH, element).click()

    def wait_visible(self, locator):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of(
                self.browser.find_element(By.XPATH, locator)
            )
        )

    def get_element_text(self, locator):
        return self.browser.find_element(By.XPATH, locator).text


class MainPage(BasePage):
    class Locators:
        elements_card = "//div[contains(@class, 'card-body')][contains(.,'Elements')]"

    def open_demoqa_page(self):
        self.open_page('https://demoqa.com/')
        assert 'https://demoqa.com/' == self.browser.current_url

    def click_to_elements_card(self):
        self.find_element_than_click(self.Locators.elements_card)
        assert 'https://demoqa.com/elements' == self.browser.current_url


class ElementsPage(BasePage):
    class Locators:
        list_item_check_box = "//*[@id='item-1'][contains(.,'Check Box')]"

    def click_on_check_box(self):
        self.find_element_than_click(self.Locators.list_item_check_box)
        assert 'https://demoqa.com/checkbox' == self.browser.current_url


class CheckboxPage(BasePage):
    class Locators:
        toggle_dir_home = "//button[contains(@title, 'Toggle')]"
        toggle_dir_downloads = "//span[contains(., 'Downloads')]//.//button[contains(@title, 'Toggle')]"
        elem_dir_downloads = "//label//span[contains(., 'Downloads')]"
        elem_word_file = "//label//span[contains(., 'Word File.doc')]"
        checkbox_word_file_doc = "//label//span[contains(., 'Word File.doc')]"
        text_result = "//div[contains(@id,'result')]"

    def toggle_home_dir(self):
        self.find_element_than_click(self.Locators.toggle_dir_home)
        self.wait_visible(self.Locators.elem_dir_downloads)

    def toggle_downloads_dir(self):
        self.find_element_than_click(self.Locators.toggle_dir_downloads)
        self.wait_visible(self.Locators.elem_word_file)

    def select_checkbox_word_file_doc(self):
        self.find_element_than_click(self.Locators.checkbox_word_file_doc)
        text = self.get_element_text(self.Locators.text_result)
        self.wait_visible(self.Locators.text_result)
        result = text.replace('\n', '')
        print(result)
        assert 'You have selected :wordFile' in result

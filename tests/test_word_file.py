from pages.pages import *
from utils.allure import allure_step


def test_checkbox_word_file_selected(browser):
    with allure_step("1. Открыть в браузере ссылку https://demoqa.com/", browser):
        MainPage(browser).open_demoqa_page()

    with allure_step("2. Нажать кнопку Elements", browser):
        MainPage(browser).click_to_elements_card()

    with allure_step("3. В раскрытом меню справа кликнуть лкм Check Box", browser):
        ElementsPage(browser).click_on_check_box()

    with allure_step("4. Раскрыть директорию Home", browser):
        CheckboxPage(browser).toggle_home_dir()

    with allure_step("5. Раскрыть директорию Downloads ", browser):
        CheckboxPage(browser).toggle_downloads_dir()

    with allure_step("6. Выбрать чек-бокс Word File.doc", browser):
        CheckboxPage(browser).select_checkbox_word_file_doc()

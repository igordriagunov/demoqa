from contextlib import contextmanager

import allure
from allure_commons.types import AttachmentType


@contextmanager
def allure_step(name, browser):
    with allure.step(name):
        yield allure.attach(browser.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)

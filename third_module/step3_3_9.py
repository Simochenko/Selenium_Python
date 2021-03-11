import unittest

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class TestUnit(unittest.TestCase):

    def test_exception1(self):
        try:
            browser = webdriver.Chrome()
            browser.get("http://selenium1py.pythonanywhere.com/")
            with pytest.raises(NoSuchElementException):
                browser.find_element_by_css_selector("button.btn")
                pytest.fail("Не должно быть кнопки Отправить")
        finally:
            browser.quit()

    def test_exception2(self):
        try:
            browser = webdriver.Chrome()
            browser.get("http://selenium1py.pythonanywhere.com/")
            with pytest.raises(NoSuchElementException):
                browser.find_element_by_css_selector("no_such_button.btn")
                pytest.fail("Не должно быть кнопки Отправить")

        finally:
            browser.quit()


if __name__ == "__main__":
    unittest.main()

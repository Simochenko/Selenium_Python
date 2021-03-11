import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    mess = ""
    link = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]

    @pytest.mark.parametrize('links', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
    def test_see(self, browser, links):
        answer = str(math.log(int(time.time())))
        link = f"https://stepik.org/lesson/{links}/step/1"
        browser.get(link)
        time.sleep(5)
        input1 = browser.find_element_by_css_selector('.textarea')
        input1.send_keys(answer)
        time.sleep(3)
        button = browser.find_element(By.CLASS_NAME, "submit-submission")
        button.click()
        time.sleep(3)
        message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        assert "Correct!" in message.text

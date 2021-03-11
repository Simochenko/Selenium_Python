import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


class TestUnit(unittest.TestCase):

    def test_link1(self):
        browser = webdriver.Chrome()
        browser.get(link1)
        input1 = browser.find_element(By.CSS_SELECTOR,
                                      "body > div > form > div.first_block > div.form-group.first_class > input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR,
                                      "body > div > form > div.first_block > div.form-group.second_class > input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR,
                                      "body > div > form > div.first_block > div.form-group.third_class > input")
        input3.send_keys("Petrov@hz.ru")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(5)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(
             welcome_text, "Congratulations! You have successfully registered!")
        browser.quit()

    def test_link2(self):
        browser = webdriver.Chrome()
        browser.get(link2)
        time.sleep(3)
        input1 = browser.find_element(By.CSS_SELECTOR,
                                      "body > div > form > div.first_block > div.form-group.first_class > input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR,
                                      "body > div > form > div.first_block > div.form-group.second_class > input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR,
                                      "body > div > form > div.first_block > div.form-group.third_class > input")
        input3.send_keys("Petrov@hz.ru")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(5)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(
            welcome_text, "Congratulations! You have successfully registered!")
        browser.quit()


if __name__ == "__main__":
    unittest.main()
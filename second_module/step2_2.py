import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects2.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = welcome_text_elt.text
    print(x)
    welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = welcome_text_elt.text
    print(y)
    summ = int(x) + int(y)
    print(summ)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summ))  # ищем элемент с текстом "Summ"
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # time.sleep(5)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

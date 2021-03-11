import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "#id-l")
    input1.send_keys("simochenko_s")
    input2 = browser.find_element(By.CSS_SELECTOR, "#id-p")
    input2.send_keys("35750185Zz")
    button = browser.find_element_by_css_selector(".form__submit")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

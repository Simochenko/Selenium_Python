import os
import time

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR,
                                  "body > div > form > div > input:nth-child(2)")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR,
                                  "body > div > form > div > input:nth-child(4)")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR,
                                  "body > div > form > div > input:nth-child(6)")
    input3.send_keys("Petrov@hz.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

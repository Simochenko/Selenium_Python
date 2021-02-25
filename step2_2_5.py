from time import sleep
from selenium import webdriver


try:

    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    # В итоге, чтобы кликнуть на перекрытую кнопку, нам нужно выполнить следующие команды в коде:
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    #Также можно проскроллить всю страницу целиком на строго заданное количество пикселей.Эта команда проскроллит страницу на 100 пикселей вниз:
    # browser.execute_script("window.scrollBy(0, 100);")
    # javascript
    # button = document.getElementsByTagName("button")[0];
    # button.scrollIntoView(true);
    button.click()
    assert True

finally:
    # успеваем скопировать код за 30 секунд
    sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

link = "http://selenium1py.pythonanywhere.com/"
options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': 'user_language'})
browser = webdriver.Chrome(options=options)


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")


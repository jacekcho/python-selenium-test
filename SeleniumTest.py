from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class SeleniumTest(unittest.TestCase):
    # // given
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()

    # // when
    driver.get('https://modivo.pl/')

    # // then
    element = driver.find_elements_by_class_name("marketing-bar-global")
    is_displayed = element.is_displayed()
    print(is_displayed)
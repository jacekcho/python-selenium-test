from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class SeleniumTest(unittest.TestCase):
    # // given
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()

    # // when
    driver.get('https://modivo.pl/')
    element = driver.find_element(By.CLASS_NAME, 'marketing-bar-global')
    is_displayed = element.is_displayed()

    # // then
    driver.close()
    print('=====================')
    print(is_displayed)
    print('=====================')
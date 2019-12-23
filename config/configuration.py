from selenium import webdriver

from base.base_methods import SeleniumDriver


class TestConfiguration():
    def __init__(self):
        baseURL = "http://automationpractice.com"
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        self.browser.get(baseURL)
        self.driver = SeleniumDriver(self.browser)

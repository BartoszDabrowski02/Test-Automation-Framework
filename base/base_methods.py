# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class SeleniumDriver():
    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            print('Locator type ' + locator_type + 'not supported.')
            return False

    def get_element(self, locator, locator_type):
        by_type = self.get_by_type(locator_type)
        element = self.driver.find_element(by_type, locator)
        return element

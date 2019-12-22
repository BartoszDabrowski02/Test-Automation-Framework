from selenium.webdriver.common.by import By
import os
from datetime import datetime


class SeleniumDriver():
    def __init__(self, browser):
        self.browser = browser

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
        element = self.browser.find_element(by_type, locator)
        return element

    def screenshot(self, description):
        file_name = str(datetime.now().strftime("_%Y%m%d_%H%M%S_")) + description + ".png"
        directory = "../screenshots/"
        relative_file_name = directory + file_name
        if not os.path.exists("../screenshots/"):
            os.makedirs(directory)
        self.browser.save_screenshot(relative_file_name)

    def set_page(self, page_module):
        return page_module(self)

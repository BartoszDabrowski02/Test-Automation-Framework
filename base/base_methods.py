from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from traceback import print_stack

# Explicit - wymagane moduły
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class SeleniumDriver():
    # TO-DO dodać opis
    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        # TO-DO dodać opis
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
        # TO-DO zrobić w ramach else zwracanie wyjątku


    # def get_element(self, locator, locator_type):
    #     # TO-DO dodać opis
    #     element = None
    #     try:
    #         by_type = self.get_by_type(locator_type)
    #         print(by_type)
    #         element = self.driver.find_element(by_type, locator)
    #         print(element)
    #         print('Element found with locator: ' + locator + ' and locator type: ' + locator_type)
    #     except:
    #         print('Error : 1 Element NOT found with locator: ' + locator + ' and locator type: ' + locator_type)
    #     return element

    def get_element(self, locator, locator_type):
        # TO-DO dodać opis
        element = None
        by_type = self.get_by_type(locator_type)
        print(by_type)
        element = self.driver.find_element(by_type, locator)
        print(element)
        print('Element found with locator: ' + locator + ' and locator type: ' + locator_type)
        return element

    #
    # def get_element_driver(self, locator, locator_type):
    #     # TO-DO dodać opis
    #     element = None
    #     by_type = self.get_by_type(locator_type)
    #     print(by_type)
    #     element = self.driver.find_element(by_type, locator)
    #     print('Element found with locator: ' + locator + ' and locator type: ' + locator_type)
    #     return element

    def element_click(self, locator, locatorType="id"):
        try:
            element = self.get_element(locator, locatorType)
            element.click()
        except:
            print("Cannot click on button with locator " + locator + " and locator type: " + locatorType)

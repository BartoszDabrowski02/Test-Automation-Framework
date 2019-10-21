from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Element:
    def __init__(self, locator, locatorType='css', description=''):
        self.locator = locator
        self.locatorType = locatorType
        self.description = description
        # W przyszłości - wait_for_visible
        # self.element = self.driver.get_element(locator, locatorType)

    def __str__(self):
        return self.description

    @property
    def element(self):
        self.current_element = self.driver.get_element(self.locator, self.locatorType)
        return self.current_element

    def click(self):
        self.element.click()

    def get_text(self):
        return self.element.text

    def print_text(self):
        print(self.element.text)


class Button(Element):
    """    Podstawowy przycisk    """

class Input(Element):
    """    Pole tekstowe    """
    def send_keys(self, keys):
        return self.element.send_keys(keys)

class Checkbox(Element):
    """Klasa obsługująca checkboxy"""

    def isSelected(self):
        return self.element.is_selected()

class Radiobutton(Checkbox):
    """Klasa obsługująca radiobuttony"""

class RadioGroup(Radiobutton):
    """Klasa obsługująca grupę radiobuttonów"""

class Dropdown(Element):
    """Klasa obsługująca dropdowny"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


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
    def webelement(self):
        return self.driver.get_element(self.locator, self.locatorType)

    def click(self):
        self.webelement.click()

    def get_text(self):
        return self.webelement.text

    def print_text(self):
        print(self.webelement.text)

class Button(Element):
    """Podstawowy przycisk"""

class Input(Element):
    """Pole tekstowe"""
    def send_keys(self, keys):
        return self.webelement.send_keys(keys)

class Checkbox(Element):
    """Klasa obsługująca checkboxy"""
    def isSelected(self):
        return self.webelement.is_selected()

class Radiobutton(Checkbox):
    """Klasa obsługująca radiobuttony"""

class RadioGroup:
    """Klasa obsługująca grupę radiobuttonów"""
    # def __init__(self, radiobutton_a_locator, radiobutton_b_locator, locator_type_a, locator_type_b):
        # self.radiogroup=[
        #     Radiobutton(radiobutton_a),
        #     radiobutton_b
        # ]

class Dropdown(Element):
    """Klasa obsługująca dropdowny"""
    @property
    def select_webelement(self):
        return Select(self.webelement)

    def select_by_value(self, value):
        self.select_webelement.select_by_value(value)

    def select_by_index(self, index):
        self.select_webelement.select_by_index(index)

    def select_by_visible_text(self, text):
        self.select_webelement.select_by_visible_text(text)

    def select_option(self, option):
        if isinstance(option, int) == True:
            self.select_webelement.select_by_index(option)
        elif option.startswith('v_'):
            option = option[2:]
            self.select_webelement.select_by_value(option)
        else:
            self.select_webelement.select_by_visible_text(option)

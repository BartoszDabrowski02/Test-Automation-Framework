from selenium.webdriver.support.select import Select


class Element:
    def __init__(self, locator, locatorType='css', description=''):
        self.locator = locator
        self.locatorType = locatorType
        self.description = description

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

    def is_visible(self):
        return self.webelement.is_displayed()

    def get_attribute(self, attribute):
        return self.webelement.get_attribute(attribute)


class Label(Element):
    """Klasa obsługująca etykiety"""
    pass


class Button(Element):
    """Class operating the buttons"""
    pass


class Input(Element):
    """Pole tekstowe"""
    def send_keys(self, keys):
        self.clear()
        return self.webelement.send_keys(keys)

    def get_value(self):
        return self.webelement.get_attribute("value")

    def clear(self):
        self.webelement.clear()


class Checkbox(Element):
    """Klasa obsługująca checkboxy"""
    def is_selected(self):
        return self.webelement.is_selected()


class Radiobutton(Checkbox):
    """Klasa obsługująca radiobuttony"""
    pass

class RadioGroup(Element):
    """Class operating the radio groups"""
    def prepare_options(self, list_of_options):
        return {option.text: option for option in list_of_options}

    def __init__(self, locator, locatorType='css', description=''):
        super().__init__(locator, locatorType, description)
        self.radio_options = self.prepare_options(self.driver.get_elements(self.locator, self.locatorType))

    def choose_option(self, option):
        try:
            self.radio_options[option].click()
        except KeyError:
            print('No such element: {}'.format(option))


class Dropdown(Element):
    """Class operating the dropdowns"""
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
        else:
            self.select_webelement.select_by_visible_text(option)

    def get_options(self):
        # TODO
        pass

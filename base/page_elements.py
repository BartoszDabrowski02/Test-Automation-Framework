from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Element:
    def __init__(self, locator, locatorType="id"):
        self.locator = locator
        self.locatorType = locatorType
        # self.element = self.driver.get_element(locator, locatorType)

    @property
    def element(self):
        self.current_element = self.driver.get_element(self.locator, self.locatorType)
        return self.current_element


    def click(self):
        # try:
            self.element.click()
        # except:
        #     print("Cannot click on button with locator " + self.locator + " and locator type: " + self.locatorType)

    def get_text(self):
        return self.element.text

    def print_text(self):
        print(self.element.text)

    def send_keys(self, keys):
        return self.element.send_keys(keys)

class Button(Element):
    """
    Podstawowy przycisk.
    """
    pass

class Input(Element):
    """
    Pole tekstowe
    """
    pass





    #
    # def __init__(
    #         self,
    #         selector,
    #         locator_type,
    #         description,
    # ):
    #     self._selector = selector
    #     self._locator_type = locator_type
    #     self._description = description
    #     # self._get_element()
    #     # self._base_methods = SeleniumDriver()
    #
    # def test(self):
    #     # return SeleniumDriver.click1(self)
    #     self.SeleniumDriver.click1()
    #
    # def _get_element(self):
    #     try:
    #         element = SeleniumDriver.get_element(self._selector, self._locator_type)
    #         return element
    #     except:
    #         print(
    #             'Error : Element NOT found with locator: ' + self._selector + ' and locator type: ' + self._locator_type)
            # TO-DO dodać wyjątek

    # def __get__(self):
    #     return self._get_element()


    # def click_button(self):
    #     SeleniumDriver.click1(self)


    # def click(self):
    #     # TO-DO dodać opis
    #     try:
    #         element = self._get_element()
    #         element.click()
    #         print("Clicked on element")
    #     except:
    #         print("Cannot send data")

    # def _get_element(self, _selector, _locator_type):
    #     #try:
    #         print('1')
    #         print(_selector)
    #         print(_locator_type)
    #         print('2')
    #         element = SeleniumDriver.get_element_driver(self, self._selector, self._locator_type)
    #         # element = SeleniumDriver.get_element(self, 'testowy_selector', 'testowy_locator_t')
    #         # element = SeleniumDriver.get_element(By.Class, "login")
    #         return element
        # except:
        #     print(
        #         'Error : 2 Element NOT found with locator: ' + self._selector + ' and locator type: ' + self._locator_type)




    # def __get__(self):
    #     return self._get_element()




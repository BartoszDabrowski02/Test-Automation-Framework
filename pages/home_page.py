from base.page_elements import Element, Button
# from base.base_methods import SeleniumDriver
from pages.upper_menu import UpperMenu

class HomePage(UpperMenu):
    def __init__(self, driver):
        super().__init__(driver)

        self.best_sellers_button = Button(
            locator=".blockbestsellers",
            locatorType="css",
        )
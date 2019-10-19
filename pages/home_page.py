from base.page_elements import Element, Button
# from base.base_methods import SeleniumDriver

class HomePage:
    def __init__(self, driver):
        # super(SeleniumDriver, self).__init__(driver)
        # self.driver = driver

        Element.driver = driver


        self.sign_button = Button(
            locator=".login",
            locatorType="css",
        )

        self.best_sellers_button = Button(
            locator=".blockbestsellers",
            locatorType="css",
        )
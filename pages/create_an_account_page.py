from base.page_elements import Element, Button, Input, Checkbox


class CreateAnAccountPage:
    def __init__(self, driver):
        Element.driver = driver

        self.sign_up_checkbox = Checkbox(
            locator="#uniform-newsletter input#newsletter",
            locatorType="css",
            description="Checkbox 'Sign up for our newsletter!'"
        )
        self.sign_up_checkbox_label = Element(
            locator=".checkbox > label[for='newsletter']",
            locatorType="css",
            description="Etykieta 'Sign up for our newsletter!'"
        )
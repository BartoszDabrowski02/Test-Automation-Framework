from base.page_elements import Element, Button, Input, Checkbox, RadioGroup, Radiobutton, Dropdown


class UpperMenu:
    def __init__(self, driver):
        Element.driver = driver

        self.sign_in_button = Button(
            locator=".login",
            description="Przycisk 'Sign in'"
        )


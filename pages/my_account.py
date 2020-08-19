from base.page_elements import Element, Button, Input
from pages.upper_menu import UpperMenu


class MyAccountPage(UpperMenu):
    def __init__(self, driver):
        super().__init__(driver)

        self.my_account_label = Element(
            locator=".page-heading",
            description="Etykieta 'MY ACCOUNT'"
        )
        self.welcome_to_your_account_label = Element(
            locator=".info-account",
            description="Etykieta 'Welcome to your account. Here you can manage (...)'"
        )

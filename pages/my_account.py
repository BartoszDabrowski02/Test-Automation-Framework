from base.page_elements import Label
from pages.upper_menu import UpperMenu


class MyAccountPage(UpperMenu):
    def __init__(self, driver):
        super().__init__(driver)

        self.my_account_label = Label(
            locator=".page-heading",
            description="Label 'MY ACCOUNT'"
        )
        self.welcome_to_your_account_label = Label(
            locator=".info-account",
            description="Label 'Welcome to your account. Here you can manage (...)'"
        )

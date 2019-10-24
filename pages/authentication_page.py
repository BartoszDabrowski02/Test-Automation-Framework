from base.page_elements import Element, Button, Input
from pages.upper_menu import UpperMenu


class AuthenticationPage(UpperMenu):
    def __init__(self, driver):
        super().__init__(driver)

        self.create_an_account_button = Button(
            locator="SubmitCreate",
            locatorType="name",
            description="Przycisk 'Create an account'"
        )
        self.create_an_account_email_address_label = Element(
            locator=".//form[@id='create-account_form']//label[text()='Email address']",
            locatorType="xpath",
            description="Etykieta 'Email address'"
        )
        self.create_an_account_email_address_input = Input(
            locator=".//input[@name='email_create']",
            locatorType="xpath",
            description="Input 'Email address'"
        )
        self.authentication_label = Element(
            locator="//div[@id='center_column']/h1[@class='page-heading']",
            locatorType="xpath",
            description="Etykieta 'AUTHENTICATION'"
        )


        # self.create_account_error_label = Element(
        #     locator="",
        #     locatorType=""
        # )

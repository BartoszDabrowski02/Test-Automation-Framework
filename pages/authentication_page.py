from base.page_elements import Button, Input, Label
from pages.upper_menu import UpperMenu


class AuthenticationPage(UpperMenu):
    def __init__(self, driver):
        super().__init__(driver)

        self.create_an_account_button = Button(
            locator="SubmitCreate",
            locatorType="name",
            description="Button 'Create an account'"
        )
        self.create_an_account_email_address_label = Label(
            locator=".//form[@id='create-account_form']//label[text()='Email address']",
            locatorType="xpath",
            description="Label 'Email address'"
        )
        self.create_an_account_email_address_input = Input(
            locator=".//input[@name='email_create']",
            locatorType="xpath",
            description="Input 'Email address'"
        )
        self.authentication_label = Label(
            locator="//div[@id='center_column']/h1[@class='page-heading']",
            locatorType="xpath",
            description="Label 'AUTHENTICATION'"
        )
        self.create_account_alert_label = Label(
            "#create_account_error li",
            description="Label z informacją o nieprawidłowej wartości w polu 'Email address'"
        )

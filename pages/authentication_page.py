from base.page_elements import Element, Button, Input


class AuthenticationPage:
    def __init__(self, driver):
        Element.driver = driver

        self.create_an_account_button = Button(
            locator="SubmitCreate",
            locatorType="name",
        )
        self.create_an_account_email_address_label = Element(
            locator=".//form[@id='create-account_form']//label[text()='Email address']",
            locatorType="xpath",
        )
        self.create_an_account_email_address_input = Input(
            locator=".//input[@name='email_create']",
            locatorType="xpath",
        )

        self.xxx = Element(
            locator="//div[@id='center_column']/h1[@class='page-heading']",
            locatorType="xpath"
        )

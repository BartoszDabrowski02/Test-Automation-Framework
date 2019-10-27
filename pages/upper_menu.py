from base.page_elements import Element, Button, Input, Checkbox, RadioGroup, Radiobutton, Dropdown


class UpperMenu:
    def __init__(self, driver):
        Element.driver = driver

        self.sign_in_button = Button(
            locator=".login",
            description="Przycisk 'Sign in'"
        )
        self.contact_us_button = Button(
            locator="[title=Contact Us]",
            description="Przycisk 'Contact us'"
        )
        self.search_input = Input(
            locator="#search_query_top",
            description="Input 'Search'"
        )
        self.search_button = Button(
            locator="submit_search",
            locatorType="name",
            description="Przycisk lupy"
        )
        self.cart_dropdown = Dropdown(
            locator=".shopping_cart > a",
            description="Dropdown 'Cart'"
        )
        self.women_button = Button(
            locator="[title='Women']",
            description="Przycisk 'WOMEN'"
        )
        self.dresses_button = Button(
            locator="[title='Dresses']",
            description="Przycisk 'DRESSES'"
        )
        self.tshirts_button = Button(
            locator="[title='T-shirts']",
            description="Przycisk 'T-SHIRTS'"
        )
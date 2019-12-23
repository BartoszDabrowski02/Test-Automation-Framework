from base.page_elements import Button, Input, Dropdown, Element, Label


class UpperMenu:
    def __init__(self, driver):
        Element.driver = driver

        self.sign_in_button = Button(
            locator=".login",
            description="Button 'Sign in'"
        )
        self.contact_us_button = Button(
            locator="[title=Contact Us]",
            description="Button 'Contact us'"
        )
        self.search_input = Input(
            locator="#search_query_top",
            description="Input 'Search'"
        )
        self.search_button = Button(
            locator="submit_search",
            locatorType="name",
            description="Button lupy"
        )
        self.cart_dropdown = Dropdown(
            locator=".shopping_cart > a",
            description="Dropdown 'Cart'"
        )
        self.number_of_products_in_cart = Label(
            locator="//div[@class='shopping_cart']/a",
            locatorType="xpath",
            description="Number of elements in cart"
        )
        self.women_button = Button(
            locator="[title='Women']",
            description="Button 'WOMEN'"
        )
        self.dresses_button = Button(
            locator="[title='Dresses']",
            description="Button 'DRESSES'"
        )
        self.tshirts_button = Button(
            locator="[title='T-shirts']",
            description="Button 'T-SHIRTS'"
        )

    def check_number_of_products_in_cart(self):
        num_of_prod = [x for x in self.number_of_products_in_cart.get_text() if x.isdigit()]
        if len(num_of_prod) == 0:
            return 0
        else:
            return int(''.join(num_of_prod))

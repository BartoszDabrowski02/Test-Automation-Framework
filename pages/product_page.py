from base.page_elements import Label, Button
from pages.upper_menu import UpperMenu


class ProductPage(UpperMenu):
    def __init__(self, driver):
        super().__init__(driver)

        self.product_title = Label(
            locator="[itemprop='name']",
            description="Product title label"
        )
        self.model_label = Label(
            locator="#product_reference",
            description="Model label"
        )
        self.condition_label = Label(
            locator="#product_condition",
            description="Condition label"
        )
        self.short_description_label = Label(
            locator="#short_description_content",
            description="Short description label"
        )
        self.add_to_cart_button = Button(
            locator="#add_to_cart > button > span",
            description="Button 'Add to cart'"
        )


class ProductSuccessfullyAdded(ProductPage):
    def __init__(self, driver):
        super().__init__(driver)

        self.product_name_label = Label(
            locator="[style*='display: block'] #layer_cart_product_title",
            description="Product name label",
        )
        self.product_attributes = Label(
            locator="[style*='display: block'] #layer_cart_product_attributes",
            description="Product attributes label",
        )
        self.product_successfully_added_label = Label(
            locator="[style*='display: block'] .layer_cart_product h2",
            description="Label 'Product successfully added to your shopping cart'",
        )
        self.continue_shopping_button = Button(
            locator="[style*='display: block'] .continue",
            description="Button 'Continue shopping'",
        )
        self.proceed_to_checkout_label = Button(
            locator="[style*='display: block'] [title='Proceed to checkout']",
            description="Button 'Proceed to checkout'",
        )
        self.close_window_button = Button(
            locator="[style*='display: block'] .cross",
            description="Close window button 'x'",
        )

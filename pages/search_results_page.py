from base.page_elements import Element, Button, Input, Dropdown
from pages.upper_menu import UpperMenu


class SearchResultsPage(UpperMenu):
    def __init__(self, driver):
        super().__init__(driver)

        self.add_to_cart_1_button = Button(
            "(//*[text()='Add to cart'])[1]/..",
            "xpath",
        )
        self.result_title_1_label = Element(
            "(//*[contains(text(),'Printed Summer Dress')])[1]",
            "xpath"
        )
        self.sort_by_dropdown = Dropdown(
            "#selectProductSort",
            # '//*[@id="selectProductSort"]',
            'css'
        )
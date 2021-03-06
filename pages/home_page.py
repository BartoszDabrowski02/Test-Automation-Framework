from base.page_elements import Button, Input
from pages.upper_menu import UpperMenu


class HomePage(UpperMenu):
    def __init__(self, driver):
        super().__init__(driver)

        self.best_sellers_button = Button(
            ".blockbestsellers",
            "css"
        )
        self.search_input = Input(
            "search_query",
            "name"
        )
        self.search_button = Button(
            "submit_search",
            "name"
        )

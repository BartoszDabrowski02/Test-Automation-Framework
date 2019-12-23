from base.page_elements import Element, Button, Input, Dropdown
from pages.upper_menu import UpperMenu
from selenium.webdriver.common.action_chains import ActionChains


class SearchResultsPage(UpperMenu):
    def __init__(self, driver):
        super().__init__(driver)

        self.add_to_cart_1_button = Button(
            "(//*[text()='Add to cart'])[1]/..",
            "xpath",
        )
        self.result_title_1_label = Element(
            "(//*[contains(text(),'Printed Summer Dress')])[4]",
            "xpath"
        )
        self.sort_by_dropdown = Dropdown(
            "#selectProductSort",
            # '//*[@id="selectProductSort"]',
            'css'
        )
        self.proceed_to_checkout_button = Button(
            "//*[contains(text(),'Proceed to checkout')]",
            'xpath'
        )

    def add_item_to_cart(self, browser, product_num):
        item_tile = Element(".product_list > li:nth-of-type({})".format(product_num))
        add_to_cart_button = Button("(//span[text()='Add to cart']/ancestor::a)[{}]".format(product_num),
                                    'xpath')
        ActionChains(browser).move_to_element(item_tile.webelement).move_to_element(add_to_cart_button.webelement).click().perform()

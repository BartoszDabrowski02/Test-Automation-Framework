from selenium import webdriver
from pages.home_page import HomePage
from pages.authentication_page import AuthenticationPage
from pages.create_an_account_page import CreateAnAccountPage
from pages.my_account import MyAccountPage
from pages.search_results_page import SearchResultsPage

from base.assertions import SeleniumAssertionBasic

from base.base_methods import SeleniumDriver
from base.support import create_unique_email
from selenium.webdriver.common.action_chains import ActionChains


class CartTests(SeleniumAssertionBasic):
    def __init__(self):
        baseURL = "http://automationpractice.com"

        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        self.browser.get(baseURL)
        self.driver = SeleniumDriver(self.browser)

    def test_add_product_to_cart(self):
        page = self.driver.set_page(HomePage)
        page.search_input.send_keys("dress")
        page.search_button.click()

        page = self.driver.set_page(SearchResultsPage)
        self.driver.screenshot("Searching results")
        # page.add_to_cart_1_button.click()
        # page.sort_by_dropdown.click()
        # time.sleep(1)
        # page.sort_by_dropdown.click()
        # print(page.sort_by_dropdown.webelement)
        ActionChains(self.browser).move_to_element(page.add_to_cart_1_button.webelement).move_to_element(page.add_to_cart_1_button.webelement).click().perform()
            # .move_to_element(page.add_to_cart_1_button.locator).click().perform()
        # .move_to_element(page.add_to_cart_1_button).click()


class LoginTests(SeleniumAssertionBasic):
    def __init__(self):
        baseURL = "http://automationpractice.com"
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        self.browser.get(baseURL)
        self.driver = SeleniumDriver(self.browser)

    def set_page(self, page_module):
        return page_module(self.driver)

    def test_incorrect_email_address(self):
        page = self.driver.set_page(HomePage)
        page.sign_in_button.click()

        page = self.driver.set_page(AuthenticationPage)
        page.create_an_account_email_address_input.send_keys("abc@gmail.com")
        self.driver.screenshot("Incorrect email")
        page.create_an_account_button.click()
        self.assert_element_text_equal(
            page.create_account_alert_label,
            "An account using this email address has already been registered. "
            "Please enter a valid password or request a new one."
        )
        self.driver.screenshot("Incorrect email alert")

    def test_create_an_account(self):
        page = self.driver.set_page(HomePage)
        page.sign_in_button.click()

        page = self.driver.set_page(AuthenticationPage)
        self.assert_element_text_equal(
            page.authentication_label,
            "AUTHENTICATION"
        )
        page.create_an_account_email_address_input.send_keys(create_unique_email())
        page.create_an_account_button.click()

        page = self.driver.set_page(CreateAnAccountPage)
        page.fill_personal_information_form(date_of_birth_days=4, date_of_birth_months=8,
                                            date_of_birth_years="2000\u00A0\u00A0", title="Mrs", first_name="Karol",
                                            last_name="Karolski", password="qwerty5", sign_up=True)
        self.driver.screenshot("Filled personal information")
        page.fill_your_address_form(first_name="Tomasz", last_name="Krążek", company="FFg", address="Polna 5/10",
                                    address_line_2="Kasztanowa 10/1, 03-494 Warszawa", zip_postal_code="12312",
                                    additional_information="fadfasd fasdf fgbn xcvb v", home_phone="823-23-23",
                                    mobile_phone="745 345 234", assign_an_address_alias="Kok", state="Arizona",
                                    country="v_21", city="Warsaw")
        self.assert_element_is_checked(
            page.sign_up_checkbox,
        )
        self.driver.screenshot("Filled entire form")
        page.register_button.click()

        page = self.driver.set_page(MyAccountPage)
        self.assert_element_text_equal(
            page.welcome_to_your_account_label,
            "Welcome to your account. Here you can manage all of your personal information and orders."
        )
        self.driver.screenshot("Account created")


ff = CartTests()
ff.test_add_product_to_cart()

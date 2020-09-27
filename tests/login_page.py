from base.assertions import SeleniumAssertionBasic
from base.support import create_unique_email
from config.configuration import TestConfiguration
from pages.authentication_page import AuthenticationPage
from pages.create_an_account_page import CreateAnAccountPage
from pages.home_page import HomePage
from pages.my_account import MyAccountPage
from pages.product_page import ProductPage, ProductSuccessfullyAdded
from pages.search_results_page import SearchResultsPage


class LoginTests(TestConfiguration, SeleniumAssertionBasic):

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
        page.fill_personal_information_form(
            title="Mrs.",
            date_of_birth_days=4,
            date_of_birth_months=8,
            date_of_birth_years="2000\u00A0\u00A0",
            first_name="Tamara",
            last_name="Morrison",
            password="qwerty5",
            sign_up=True
        )
        page.fill_your_address_form(
            first_name="Tamara",
            last_name="Morrison",
            company="FFG",
            address="1830 Tully Street",
            address_line_2="",
            zip_postal_code="48226",
            additional_information="Lorem ipsum",
            home_phone="313-673-8139",
            mobile_phone="313-970-0034",
            assign_an_address_alias="MI",
            state="Michigan",
            country="United States",
            city="Detroit"
        )
        self.driver.screenshot("Filled personal information")
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


class CartTests(TestConfiguration, SeleniumAssertionBasic):

    def test_add_product_to_cart(self):
        page = self.driver.set_page(HomePage)
        page.search_input.send_keys("dress")
        page.search_button.click()

        page = self.driver.set_page(SearchResultsPage)
        self.driver.screenshot("Searching results")
        page.item_details(self.browser, 1)

        page = self.driver.set_page(ProductPage)
        products_before_click = page.check_number_of_products_in_cart()
        self.assert_element_text_equal(
            page.product_title,
            'Printed Summer Dress',
        )
        self.assert_element_text_equal(
            page.model_label,
            'Model demo_5',
        )
        self.assert_element_text_equal(
            page.condition_label,
            'Condition New',
        )
        self.assert_element_text_equal(
            page.short_description_label,
            'Long printed dress with thin adjustable straps. '
            'V-neckline and wiring under the bust with ruffles at the bottom of the dress.',
        )
        self.driver.screenshot("Product details page")
        page.add_to_cart_button.click()

        page = self.driver.set_page(ProductSuccessfullyAdded)
        self.assert_element_text_equal(
            page.product_name_label,
            'Printed Summer Dress'
        )
        self.assert_element_text_equal(
            page.product_attributes,
            'Yellow, S'
        )
        self.assert_element_text_contains(
            page.product_successfully_added_label,
            'Product successfully added to your shopping cart'
        )
        self.assert_element_text_equal(
            page.continue_shopping_button,
            'Continue shopping'
        )
        self.assert_element_text_equal(
            page.proceed_to_checkout_label,
            'Proceed to checkout'
        )
        self.driver.screenshot("Product successfully added to your shopping cart window")
        page.continue_shopping_button.click()

        page = self.driver.set_page(ProductPage)
        products_after_click = page.check_number_of_products_in_cart()
        self.assert_value_is_greater_then(
            products_after_click,
            products_before_click,
            "Uncorrect number of products"
        )
        self.driver.screenshot("Product successfully added to your shopping cart")


ff = LoginTests()
ff.test_create_an_account()

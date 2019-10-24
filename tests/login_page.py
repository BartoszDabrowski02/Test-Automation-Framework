# -*- coding: utf-8 -*-
from selenium import webdriver
from pages.home_page import HomePage
from pages.authentication_page import AuthenticationPage
from pages.create_an_account_page import CreateAnAccountPage

from base.assertions import SeleniumAssertionBasic

from base.base_methods import SeleniumDriver
from base.support import create_unique_email

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.select import Select


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

    def test_create_an_account(self):
        page = self.set_page(HomePage)
        page.sign_in_button.click()

        page = self.set_page(AuthenticationPage)
        self.assert_element_text_equal(
            page.authentication_label,
            "AUTHENTICATION"
        )
        page.create_an_account_email_address_input.send_keys(create_unique_email())
        page.create_an_account_button.click()

        page = self.set_page(CreateAnAccountPage)

        # element = self.browser.find_element_by_css_selector("#days")
        # sel = Select(element)
        # sel.select_by_index(10)
        # element = self.browser.find_element_by_id("id_state")
        # sel = Select(element)
        # sel.select_by_visible_text("California")

        # page.fill_personal_information_form(date_of_birth_days="4")

# title="Mrs", first_name="Karol", last_name="Karolski", password="qwerty5", sign_up=True

        page.fill_your_address_form(first_name="Tomasz", last_name="Krążek", company="FFg", address="Polna 5/10",
                                    address_line_2="Kasztanowa 10/1, 03-494 Warszawa", zip_postal_code="12-312",
                                    additional_information="fadfasd fasdf fgbn xcvb v", home_phone="823-23-23",
                                    mobile_phone="745 345 234", assign_an_address_alias="Kok")


ff = LoginTests()
ff.test_create_an_account()
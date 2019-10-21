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
        page.sign_button.click()

        page = self.set_page(AuthenticationPage)
        self.assert_element_text_equal(
            page.authentication_label,
            "AUTHENTICATION"
        )
        page.create_an_account_email_address_input.send_keys(create_unique_email())
        page.create_an_account_button.click()

        page = self.set_page(CreateAnAccountPage)
        page.fill_personal_information_form(title="Mrs", first_name="Karol", last_name="Karolski", password="qwerty5",
                                            date_of_birth_months=2, sign_up=True)






ff = LoginTests()
ff.test_create_an_account()
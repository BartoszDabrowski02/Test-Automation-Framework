from selenium import webdriver
from pages.home_page import HomePage
from pages.authentication_page import AuthenticationPage

from base.assertions import SeleniumAssertionBasic

from base.base_methods import SeleniumDriver


class LoginTests(SeleniumAssertionBasic):
    def __init__(self):
        baseURL = "http://automationpractice.com"
        browser = webdriver.Firefox()
        browser.maximize_window()
        ### ustalić czy poniższe niezbędne
        browser.implicitly_wait(3)
        browser.get(baseURL)
        # driver.implicitly_wait(20)
        ### strona na której użytkownik się znajduje
        self.driver = SeleniumDriver(browser)


    def set_page(self, page_module):
        return page_module(self.driver)


    def test_valid_login(self):
        page = self.set_page(HomePage)
        page.best_sellers_button.click()
        page.sign_button.click()

        page = self.set_page(AuthenticationPage)
        page.create_an_account_button.click()
        page.create_an_account_email_address_label.click()
        page.create_an_account_email_address_input.click()

        self.assert_element_text_equal(
            page.create_an_account_email_address_label,
            'Email address'
        )


        # self.driver.quit()




ff = LoginTests()
ff.test_valid_login()
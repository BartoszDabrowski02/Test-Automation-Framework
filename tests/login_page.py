# -*- coding: utf-8 -*-
from selenium import webdriver
from pages.home_page import HomePage
from pages.authentication_page import AuthenticationPage

from base.assertions import SeleniumAssertionBasic

from base.base_methods import SeleniumDriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class LoginTests(SeleniumAssertionBasic):
    def __init__(self):
        baseURL = "http://automationpractice.com"
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        ### ustalić czy poniższe niezbędne
        self.browser.implicitly_wait(3)
        self.browser.get(baseURL)
        # driver.implicitly_wait(20)
        ### strona na której użytkownik się znajduje
        self.driver = SeleniumDriver(self.browser)


    def set_page(self, page_module):
        return page_module(self.driver)


    def test_valid_login(self):
        page = self.set_page(HomePage)
        page.sign_button.click()

        page = self.set_page(AuthenticationPage)
        page.create_an_account_button.click()
        page.create_an_account_email_address_label.click()
        page.create_an_account_email_address_input.click()

        print("*A*")
        self.assert_element_text_equal(
            page.create_an_account_email_address_label,
            "Email address"
        )

        print("*1*")
        page.create_an_account_email_address_label.print_text()

        print("*2*")
        print(self.browser.find_element_by_xpath("//div[@id='center_column']/h1[@class='page-heading']").text)
        print("*3*")
        self.browser.find_element_by_xpath("//div[@id='center_column']/h1[@class='page-heading']").text

        print("**Y**")
        self.browser.find_element_by_xpath(".//input[@name='email_create']").send_keys("XYZ")
        print("**X**")
        page.create_an_account_email_address_input.send_keys("abc")


        print("*4*")
        page.create_an_account_email_address_label.text




        # self.driver.get_element("//div[@id='center_column']/h1[@class='page-heading']", By.XPATH)
        #
        # page.create_an_account_email_address_label.get_text()


        # element = self.driver.find_element_by_xpath("//div[@id='center_column']/h1[@class='page-heading']")

        # self.assert_element_text_equal(
        #     page.create_an_account_email_address_label,
        #     'Email address'
        # )


        # self.driver.quit()




ff = LoginTests()
ff.test_valid_login()
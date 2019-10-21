from base.page_elements import Element, Button, Input, Checkbox, RadioGroup, Radiobutton, Dropdown


class CreateAnAccountPage:
    def __init__(self, driver):
        Element.driver = driver

        self.page_heading_label = Element(
            locator=".page-heading",
            description="Etykieta 'CREATE AN ACCOUNT'"
        )
        self.your_personal_information_label = Element(
            locator=".page-subheading",
            description="Etykieta 'YOUR PERSONAL INFORMATION'"
        )
        # self.title_radiogroup = RadioGroup(
        #     locator="clearfix",
        #     description="Radio grupa 'Title'"
        # )
        self.title_mr_radiobutton = Radiobutton(
            locator="#id_gender1",
            description="Radiobutton 'Mr.'"
        )
        self.title_mrs_radiobutton = Radiobutton(
            locator="#id_gender2",
            description="Radiobutton 'Mrs.'"
        )
        self.first_name_input = Input(
            locator="#customer_firstname",
            description="Input 'First name'"
        )
        self.last_name_input = Input(
            locator="#customer_lastname",
            description="Input 'Last name'"
        )
        self.email_input = Input(
            locator="#email",
            description="Input 'Email'"
        )
        self.password_input = Input(
            locator="#passwd",
            description="Input 'Password '"
        )
        self.date_of_birth_days_dropdown = Dropdown(
            locator="days",
            description="Dropdown Date of Birth - dni"
        )
        self.date_of_birth_months_dropdown = Dropdown(
            locator="#months",
            description="Dropdown Date of Birth - miesiące"
        )
        self.date_of_birth_years_dropdown = Dropdown(
            locator="#years",
            description="Dropdown Date of Birth - lata"
        )
        self.sign_up_checkbox = Checkbox(
            locator="#uniform-newsletter input#newsletter",
            description="Checkbox 'Sign up for our newsletter!'"
        )
        self.receive_special_offers_checkbox = Checkbox(
            locator="#uniform-optin input#optin",
            description="Checkbox 'Sign up for our newsletter!'"
        )
        self.your_address_label = Element(
            locator=".page-subheading",
            description="Etykieta 'YOUR ADDRESS'"
        )


    def fill_personal_information_form(self,
                                       title=None,
                                       first_name=None,
                                       last_name=None,
                                       email=None,
                                       password=None,
                                       # date_of_birth_days=None,
                                       # date_of_birth_months=None,
                                       # date_of_birth_years=None,
                                       sign_up=None,
                                       receive_special_offers=None):
        """Metoda pozwalająca wypełnić formularz YOUR PERSONAL INFORMATION"""
        if title == "Mr":
            self.title_mr_radiobutton.click()
        elif title == "Mrs":
            self.title_mrs_radiobutton.click()
        if first_name != None:
            self.first_name_input.send_keys(first_name)
        if last_name != None:
            self.last_name_input.send_keys(last_name)
        if email != None:
            self.email_input.send_keys(email)
        if password != None:
            self.password_input.send_keys(password)
        # if date_of_birth_days != None:
        #     self.date_of_birth_days_dropdown.select_by_value(date_of_birth_days)
        # if date_of_birth_months != None:
        #     self.date_of_birth_months_dropdown.select_by_value(date_of_birth_months)
        # if date_of_birth_years != None:
        #     self.date_of_birth_years_dropdown.select_by_value(date_of_birth_years)
        if sign_up == True:
            if self.sign_up_checkbox.isSelected() == False:
                self.sign_up_checkbox.click()
        if receive_special_offers == True:
            if self.receive_special_offers_checkbox.isSelected() == False:
                self.receive_special_offers_checkbox.click()








        # self. = Input(
        #     locator="",
        #     locatorType="",
        #     description="Input ''"
        # )
        # self. = Input(
        #     locator="",
        #     locatorType="",
        #     description="Input ''"
        # )
        # self. = Input(
        #     locator="",
        #     locatorType="",
        #     description="Input ''"
        # )
        #
        #



        # self.sign_up_checkbox_label = Element(
        #     locator=".checkbox > label[for='newsletter']",
        #     description="Etykieta 'Sign up for our newsletter!'"
        # )
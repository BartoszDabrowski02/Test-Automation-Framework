from base.page_elements import Label, Button, Input, Checkbox, Radiobutton, Dropdown
from pages.upper_menu import UpperMenu


class CreateAnAccountPage(UpperMenu):
    def __init__(self, driver):
        super().__init__(driver)

        self.page_heading_label = Label(
            locator=".page-heading",
            description="Label 'CREATE AN ACCOUNT'"
        )
        # Section "YOUR PERSONAL INFORMATION"
        self.your_personal_information_label = Label(
            locator="//div[@class='account_creation'][1]/h3[@class='page-subheading']",
            locatorType="xpath",
            description="Label 'YOUR PERSONAL INFORMATION'"
        )
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
            locator="#days",
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
        self.your_address_label = Label(
            locator=".page-subheading",
            description="Label 'YOUR ADDRESS'"
        )
        # Section "YOUR ADDRESS"
        self.your_address_label = Label(
            locator="//div[@class='account_creation'][2]/h3[@class='page-subheading']",
            locatorType="xpath",
            description="Label 'YOUR ADDRESS'"
        )
        self.first_name_address_input = Input(
            locator="firstname",
            locatorType="name",
            description="Input 'First name'"
        )
        self.last_name_address_input = Input(
            locator="lastname",
            locatorType="name",
            description="Input 'Last name'"
        )
        self.company_input = Input(
            locator="#company",
            description="Input 'Company'"
        )
        self.address_input = Input(
            locator="[name=address1]",
            description="Input 'Address'"
        )
        self.address_line_2_input = Input(
            locator="address2",
            locatorType="name",
            description="Input 'Address (Line 2)'"
        )
        self.city_input = Input(
            locator="#city",
            description="Input 'City'"
        )
        self.state_dropdown = Dropdown(
            locator="#id_state",
            description="Dropdown 'State'"
        )
        self.zip_postal_code_input = Input(
            locator=".uniform-input",
            description="Input 'Zip/Postal Code'"
        )
        self.country_dropdown = Dropdown(
            locator="#id_country",
            description="Dropdown 'Country'"
        )
        self.additional_information_input = Input(
            locator="#other",
            description="Input 'Additional information'"
        )
        self.home_phone_input = Input(
            locator="#phone",
            description="Input 'Home phone'"
        )
        self.mobile_phone_input = Input(
            locator="#phone_mobile",
            description="Input 'Mobile phone'"
        )
        self.assign_an_address_alias_input = Input(
            locator="#alias",
            description="Input 'Assign an address alias for future reference'"
        )
        self.register_button = Button(
            locator="#submitAccount",
            description="Button 'Register'"
        )

    def fill_personal_information_form(
        self,
        title=None,
        first_name=None,
        last_name=None,
        email=None,
        password=None,
        date_of_birth_days=None,
        date_of_birth_months=None,
        date_of_birth_years=None,
        sign_up=None,
        receive_special_offers=None
    ):
        """This method allows to fill YOUR PERSONAL INFORMATION form"""
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
        if date_of_birth_days != None:
            self.date_of_birth_days_dropdown.select_option(date_of_birth_days)
        if date_of_birth_months != None:
            self.date_of_birth_months_dropdown.select_option(date_of_birth_months)
        if date_of_birth_years != None:
            self.date_of_birth_years_dropdown.select_option(date_of_birth_years)
        if sign_up == True:
            if self.sign_up_checkbox.is_selected() == False:
                self.sign_up_checkbox.click()
        if receive_special_offers == True:
            if self.receive_special_offers_checkbox.is_selected() == False:
                self.receive_special_offers_checkbox.click()

    def fill_your_address_form(
        self,
        first_name=None,
        last_name=None,
        company=None,
        address=None,
        address_line_2=None,
        city=None,
        state=None,
        zip_postal_code=None,
        country=None,
        additional_information=None,
        home_phone=None,
        mobile_phone=None,
        assign_an_address_alias=None
    ):
        """This method allows to fill YOUR ADDRESS form"""
        if first_name != None:
            self.first_name_address_input.send_keys(first_name)
        if last_name != None:
            self.last_name_address_input.send_keys(last_name)
        if company != None:
            self.company_input.send_keys(company)
        if address != None:
            self.address_input.send_keys(address)
        if address_line_2 != None:
            self.address_line_2_input.send_keys(address_line_2)
        if city != None:
            self.city_input.send_keys(city)
        if state != None:
            self.state_dropdown.select_option(state)
        if zip_postal_code != None:
            self.zip_postal_code_input.send_keys(zip_postal_code)
        if country != None:
            self.country_dropdown.select_option(country)
        if additional_information != None:
            self.additional_information_input.send_keys(additional_information)
        if home_phone != None:
            self.home_phone_input.send_keys(home_phone)
        if mobile_phone != None:
            self.mobile_phone_input.send_keys(mobile_phone)
        if assign_an_address_alias != None:
            self.assign_an_address_alias_input.send_keys(assign_an_address_alias)

import re

regex = {
        'DATE' : "^\d{4}[-.\/]\d{2}[-.\/]\d{2}$",
    }

DEFAULT_ASSERION_MESSAGES = {
    'assert_element_text_equal' : 'Oczekiwana treść elementu {0} to {1} a jest {2}.',
    'assert_element_value_equal' : 'Oczekiwana wartość elementu {0} to {1} a jest {2}.',
    'assert_element_value_contains' : 'Wartość elementu {0}« nie zawiera {1}.',
    'assert_element_value_starts' : 'Wartość elementu {0} nie zaczyna się od {1}.',
    'assert_element_is_visible' : 'Element {0} jest niewidoczny.',
    'assert_element_is_checked' : 'Element {0} nie jest zaznaczony.',
    'assert_element_is_not_checked': 'Element {0} jest zaznaczony.',
    'assert_element_css_attribute_equal': 'Oczekiwana wartość atrybutu {0} pola {1} to {2}. (Aktualna wartość to: {3}).',
    'assert_element_value_is_date' : 'Oczekujemy iż wartość elementu {0} będzie datą. (Wartość elementu to: {1}).',
}

def _default_assertion_message(method_name):
    return DEFAULT_ASSERION_MESSAGES[method_name]

def assertion_message(assertion_name, *args, msg=None):
    if msg is None:
        msg = _default_assertion_message(assertion_name).format(*args,)
    raise Exception(msg)


class SeleniumAssertionBasic:

    def assert_element_text_equal(self, element, excepted_value, msg=None):
        actual_text = element.get_text()
        if actual_text != excepted_value:
            assertion_message("assert_element_text_equal", element, excepted_value, actual_text, msg=msg)

    def assert_element_value_equal(self, element, excepted_value, msg=None):
        actual_value = element.get_value()
        if actual_value != excepted_value:
            assertion_message("assert_element_value_equal", element, excepted_value, actual_value, msg=msg)

    def assert_element_value_contains(self, element, contained_value, msg=None):
        actual_value = element.get_value()
        if contained_value not in actual_value:
            assertion_message("assert_element_value_contains", element, contained_value, msg=msg)

    def assert_element_value_starts(self, element, excepted_value, msg=None):
        actual_value = element.get_value()
        if actual_value.startswith(excepted_value) == False:
            assertion_message("assert_element_value_starts", element, excepted_value, msg=msg)

    def assert_element_is_visible(self, element, msg=None):
        if not element.is_visible():
            assertion_message("assert_element_is_visible", element, msg=msg)

    def assert_element_is_checked(self, element, msg=None):
        if not element.is_selected():
            assertion_message("assert_element_is_checked", element, msg=msg)

    def assert_element_is_not_checked(self, element, msg=None):
        if element.is_selected():
            assertion_message("assert_element_is_not_checked", element, msg=msg)

    def assert_element_css_attribute_equal(self, element, attribute, excepted_value, msg=None):
        actual_value = element.get_attribute(attribute)
        if excepted_value != actual_value:
            assertion_message("assert_element_css_attribute_equal", attribute, element, excepted_value, actual_value, msg)

    def assert_element_value_is_date(self, element, msg=None):
        actual_value = element.get_value()
        print(actual_value)
        print(type(actual_value))
        if re.search(regex["DATE"], actual_value) == None:
            assertion_message("assert_element_value_is_date", element, actual_value, msg)

    def assert_date_earlier(self, element, date_to_compare, msg=None):
        actuale_value = element.get_value()
        y, m, d = [x for x in actuale_value.split("-")]
        print("YYYY: {},\nMM: {},\nDD: {},".format(y, m, d, ))
        actuale_date = y + m + d
        print(actuale_date)
        y, m, d = [x for x in date_to_compare.split("-")]
        compare_date = y + m + d
        if actuale_date > compare_date:
            print("Śmieszki!")
            # TODO
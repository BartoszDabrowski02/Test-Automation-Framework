import re

regex = {
        'DATE' : "^\d{4}[-.\/]\d{2}[-.\/]\d{2}$",
    }

DEFAULT_ASSERION_MESSAGES = {
    'assert_date_earlier': "We expect that element's {0} date will be earlier than {1}.\nCurrent date: {2}.",
    'assert_date_later': "We expect that element's {0} date will be later than {1}.\nCurrent date: {2}.",
    'assert_element_text_equal' : "We expect that element's {0} text will be {1}.\nCurrent text: {2}.",
    'assert_element_text_contains': "We expect that element's {0} text contains {1}.\nCurrent text: {2}.",
    'assert_element_value_equal' : "We expect that element's {0} value will be {1}.\nCurrent value: {2}.",
    'assert_element_value_contains' : "We expect that element's {0} value will contains {1}.\nCurrent value: {2}.",
    'assert_element_value_starts' : "We expect that element's {0} value will start {1}.\nCurrent value: {2}.",
    'assert_element_is_visible' : "We expect that element {0} will be visible.",
    'assert_element_is_checked' : "We expect that element {0} will be checked.",
    'assert_element_is_not_checked': "We expect that element {0} will be not checked.",
    'assert_element_css_attribute_equal': "We expect that element's {1} attribute {0} will be {2}.\nCurrent value: {3}.",
    'assert_element_value_is_date' : "We expect that element's {0} value will be dateattribute {0}.\nCurrent value: {1}.",
    'assert_value_is_greater_then' : "We expect that value {0} will be greater than {1}.\nCurrent value: {0}."
}

def _default_assertion_message(method_name):
    return DEFAULT_ASSERION_MESSAGES[method_name]

def assertion_message(assertion_name, *args, msg=None):
    if msg == None:
        msg = _default_assertion_message(assertion_name).format(*args,)
    raise Exception(msg)


class SeleniumAssertionBasic:

    def assert_element_text_equal(self, element, excepted_value, msg=None):
        actual_text = element.get_text()
        if actual_text != excepted_value:
            assertion_message("assert_element_text_equal", element, excepted_value, actual_text, msg=msg)

    def assert_element_text_contains(self, element, excepted_value, msg=None):
        actual_text = element.get_text()
        if actual_text not in excepted_value:
            assertion_message("assert_element_text_equal", element, excepted_value, actual_text, msg=msg)

    def assert_element_value_equal(self, element, excepted_value, msg=None):
        actual_value = element.get_value()
        if actual_value != excepted_value:
            assertion_message("assert_element_value_equal", element, excepted_value, actual_value, msg=msg)

    def assert_element_value_contains(self, element, contained_value, msg=None):
        actual_value = element.get_value()
        if contained_value not in actual_value:
            assertion_message("assert_element_value_contains", element, contained_value, actual_value, msg=msg)

    def assert_element_value_starts(self, element, excepted_value, msg=None):
        actual_value = element.get_value()
        if actual_value.startswith(excepted_value) == False:
            assertion_message("assert_element_value_starts", element, excepted_value, actual_value, msg=msg)

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
            assertion_message("assert_element_css_attribute_equal", attribute, element, excepted_value, actual_value, msg=msg)

    def assert_element_value_is_date(self, element, msg=None):
        actual_value = element.get_value()
        if re.search(regex["DATE"], actual_value) == None:
            assertion_message("assert_element_value_is_date", element, actual_value, msg=msg)

    def assert_date_earlier(self, element, date_to_compare, msg=None):
        actuale_value = element.get_value()
        y, m, d = [x for x in actuale_value.split("-")]
        actuale_date = y + m + d
        y, m, d = [x for x in date_to_compare.split("-")]
        compare_date = y + m + d
        if actuale_date > compare_date:
            assertion_message("assert_date_earlier", element, date_to_compare, actuale_value, msg=msg)

    def assert_date_later(self, element, date_to_compare, msg=None):
        actuale_value = element.get_value()
        y, m, d = [x for x in actuale_value.split("-")]
        actuale_date = y + m + d
        y, m, d = [x for x in date_to_compare.split("-")]
        compare_date = y + m + d
        if actuale_date < compare_date:
            assertion_message("assert_date_later", element, date_to_compare, actuale_value, msg=msg)

    def assert_value_is_greater_then(self, value_greater, value_lower, msg=None):
        if value_greater <= value_lower:
            assertion_message("assert_value_is_greater_then", value_greater, value_lower, msg=msg)

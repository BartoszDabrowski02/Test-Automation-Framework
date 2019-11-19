DEFAULT_ASSERION_MESSAGES = {
    'assert_element_text_equal' : 'Oczekiwana treść elementu »%s« to »%s« a jest »%s«.',
    'assert_element_value_equal' : 'Oczekiwana wartość elementu »%s« to »%s« a jest »%s«.',
    'assert_element_value_contains' : 'Wartość elementu »%s« nie zawiera »%s«.',
    'assert_element_value_starts' : 'Wartość elementu »%s« nie zaczyna się od »%s«.',
    'assert_element_is_visible' : 'Element »%s« jest niewidoczny.',
    'assert_element_css_attribute_equal': 'Oczekiwana wartość atrybutu »%s« pola »%s« to »%s« a jest »%s«.',
}

def _default_assertion_message(method_name):
    return DEFAULT_ASSERION_MESSAGES[method_name]

def assertion_message(assertion_name, *args, msg=None):
    if msg is None:
        msg = _default_assertion_message(assertion_name) % (*args,)
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

    def assert_element_css_attribute_equal(self, element, attribute, excepted_value, msg=None):
        actual_value = element.get_attribute(attribute)
        if excepted_value != actual_value:
            assertion_message("assert_element_css_attribute_equal", attribute, element, excepted_value, actual_value)

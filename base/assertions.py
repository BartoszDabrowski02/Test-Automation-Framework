# -*- coding: utf-8 -*-


DEFAULT_ASSERION_MESSAGES = {
    'assert_element_text_equal' : 'Oczekiwana treść elementu »%s« to »%s« a jest »%s«.',
    'assert_element_value_equal' : 'Oczekiwana wartość elementu »%s« to »%s« a jest »%s«.',
    'assert_element_value_contains' : 'wartość elementu »%s« nie zawiera »%s«.',
}

def _default_assertion_message(method_name):
    return DEFAULT_ASSERION_MESSAGES[method_name]

class SeleniumAssertionBasic:

    def assert_element_text_equal(self, element, excepted_text, msg=None):
        actual_text = element.get_text()
        if actual_text != excepted_text:
            if msg is None:
                msg = _default_assertion_message('assert_element_text_equal') % (element, excepted_text, actual_text)
            raise Exception(msg)

    def assert_element_value_equal(self, element, excepted_value, msg=None):
        actual_value = element.get_value()
        if actual_value != excepted_value:
            if msg is None:
                msg = _default_assertion_message('assert_element_value_equal') % (element, excepted_value, actual_value)
            raise Exception(msg)

    def assert_element_value_contains(self, element, contained_value, msg=None):
        actual_value = element.get_value()
        if contained_value not in actual_value:
            if msg is None:
                msg = _default_assertion_message('assert_element_value_contains') % (element, contained_value)
            raise Exception(msg)

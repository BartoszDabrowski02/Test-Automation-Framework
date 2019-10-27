# -*- coding: utf-8 -*-


DEFAULT_ASSERION_MESSAGES = {
    'assert_element_text_equal': u'Oczekiwana treść elementu »%s« to »%s« a jest »%s«.',
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

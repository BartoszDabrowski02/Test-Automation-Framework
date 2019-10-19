import re, datetime, inspect, logging


DEFAULT_ASSERION_MESSAGES = {
    'assert_element_text_equal': u'Oczekiwana treść elementu »%s« to »%s« a jest »%s«.',
}


def _default_assertion_message():
    method_name = inspect.stack()[1][3]
    return DEFAULT_ASSERION_MESSAGES[method_name]
# Jak to kurfa działa?


class SeleniumAssertionBasic(object):
    # TO-DO dodać opis

    def assert_element_text_equal(self, element, excepted_text, msg=None):
        actual_text = element.text
        if actual_text != excepted_text:
            if msg is None:
                msg = _default_assertion_message() % (element, excepted_text, actual_text)
            raise Exception(msg)  # ???
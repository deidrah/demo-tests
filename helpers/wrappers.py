from helpers.screenshot_listener import make_screenshot
from selenium.common.exceptions import TimeoutException


def screenshot_decorator(test_fun):
    def wrapper(self):
        try:
            return test_fun(self)
        except AssertionError as ex:
            make_screenshot(self.ef_driver, 'assert')
            raise ex
        except TimeoutException as ex:
            make_screenshot(self.ef_driver, 'timeout')
            raise ex

    return wrapper

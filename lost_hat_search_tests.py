from selenium.webdriver.common.keys import Keys
from BaseTestClass import BaseTestClass
from helpers.wrappers import screenshot_decorator


class LostHatSearchTests(BaseTestClass):

    @screenshot_decorator
    def test_sanity_search_on_main_page(self):
        search_phase = 'Hummingbird'
        expected_element_name = 'Hummingbird Printed T-shirt'
        search_input_xpath = '//*[@name="s"]'
        result_element_xpath = '//*[@class="product-miniature js-product-miniature"]'
        self.ef_driver.get(self.base_url)
        search_input_element = self.ef_driver.find_element_by_xpath(search_input_xpath)
        search_input_element.send_keys(search_phase)
        search_input_element.send_keys(Keys.ENTER)
        result_elements = self.ef_driver.find_elements_by_xpath(result_element_xpath)
        found_elements_number = 0
        for element in result_elements:
            if expected_element_name in element.text:
                found_elements_number = found_elements_number + 1
        self.assertEqual(1, found_elements_number,
                         f"We expect 1 and actual number of found items is {found_elements_number}")
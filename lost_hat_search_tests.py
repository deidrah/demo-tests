import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LostHatSearchTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.base_url = 'http://autodemo.testoneo.com/en/'
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Dominika\Downloads\chromedriver_win32("
                                                       r"1)\chromedriver.exe")

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_sanity_search_on_main_page(self):
        search_phase = 'Hummingbird'
        expected_element_name = 'Hummingbird Printed T-shirt'
        search_input_xpath = '//*[@name="s"]'
        result_element_xpath = '//*[@class="product-miniature js-product-miniature"]'
        self.driver.get(self.base_url)
        search_input_element = self.driver.find_element_by_xpath(search_input_xpath)
        search_input_element.send_keys(search_phase)
        search_input_element.send_keys(Keys.ENTER)
        result_elements = self.driver.find_elements_by_xpath(result_element_xpath)
        found_elements_number = 0
        for element in result_elements:
            if expected_element_name in element.text:
                found_elements_number = found_elements_number + 1
        self.assertEqual(1, found_elements_number,
                         f"We expect 1 and actual number of found items is {found_elements_number}")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.events import EventFiringWebDriver

from BaseTestClass import BaseTestClass
from helpers.screenshot_listener import ScreenshotListener
from helpers.wrappers import screenshot_decorator


class LostHatSmokeTests(BaseTestClass):
    @classmethod
    def setUpClass(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.clothes_product_url = self.base_url + '3-clothes'
        self.accessories_product_url = self.base_url + '6-accessories'
        self.art_product_url = self.base_url + '9-art'
        driver = webdriver.Chrome(executable_path=r"C:\Users\Dominika\Downloads\chromedriver_win32("
                                                  r"1)\chromedriver.exe")
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())

    @classmethod
    def tearDownClass(self):
        self.ef_driver.quit()

    @screenshot_decorator
    def test_base_page_title(self):
        expected_title = 'Lost Hat'
        self.assert_title(self.base_url, expected_title)

    @screenshot_decorator
    def test_product_clothes_page_title(self):
        expected_title = 'Clothes'
        self.assert_title(self.clothes_product_url, expected_title)

    @screenshot_decorator
    def test_product_accessories_page_title(self):
        expected_title = 'Accessories'
        self.assert_title(self.accessories_product_url, expected_title)

    @screenshot_decorator
    def test_product_art_page_title(self):
        expected_title = 'Art'
        self.assert_title(self.art_product_url, expected_title)

    @screenshot_decorator
    def test_login_page_title(self):
        expected_title = 'Login'
        self.assert_title(self.login_url, expected_title)

    @screenshot_decorator
    def get_page_title(self, url):
        self.ef_driver.get(url)
        return self.ef_driver.title

    @screenshot_decorator
    def test_smoke_search_on_main_page(self):
        search_phase = 'mug'
        search_input_xpath = '//*[@name="s"]'
        result_element_xpath = '//*[@class="product-miniature js-product-miniature"]'
        minimum_expected_elements = 5
        self.ef_driver.get(self.base_url)
        search_input_element = self.ef_driver.find_element_by_xpath(search_input_xpath)
        search_input_element.send_keys(search_phase)
        search_input_element.send_keys(Keys.ENTER)
        result_elements = self.ef_driver.find_elements_by_xpath(result_element_xpath)
        self.assertLessEqual(minimum_expected_elements, len(result_elements),
                             f'Expected number {minimum_expected_elements} isn\'t less or equal than actual number of '
                             f'elements found: {len(result_elements)}')

    def get_page_title(self, url):
        self.ef_driver.get(url)
        return self.ef_driver.title

    def assert_title(self, url, expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(expected_title, actual_title,
                         f'Expected {expected_title} differ from actual title {actual_title} on page: {url}')

import unittest
from selenium import webdriver


class LostHatFrontPageTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Dominika\Downloads\chromedriver_win32("
                                                       r"1)\chromedriver.exe")

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_slider_presention(self):
        slider_xpath = '//*[@id="carousel"]'
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath(slider_xpath)

    def test_slider_minimum_size(self):
        expected_min_height = 300
        expected_min_width = 600
        slider_xpath = '//*[@id="carousel"]'
        driver = self.driver
        driver.get(self.base_url)
        slider_element = driver.find_element_by_xpath(slider_xpath)
        actual_slider_height = slider_element.size['height']
        actual_slider_width = slider_element.size['width']
        with self.subTest('Element height'):
            self.assertLess(expected_min_height, actual_slider_height,
                            'Element height found by xpath {} on page {} is smaller than expected {}px'.format(slider_xpath, driver.current_url, expected_min_height))
        with self.subTest('Element width'):
            self.assertLess(expected_min_width, actual_slider_width,
                            'Element width found by xpath {} on page {} is smaller than expected {}px'.format(slider_xpath, driver.current_url, expected_min_width))

    def test_slider_contain_exact_number_of_slides(self):
        expected_number_of_slides = 3
        slides_xpath = '//*[@id="carousel"]/ul/li'
        driver = self.driver
        driver.get(self.base_url)
        slider_elements = driver.find_elements_by_xpath(slides_xpath)
        actual_number_of_slides = len(slider_elements)
        self.assertEqual(expected_number_of_slides, actual_number_of_slides,
                         'Slides number differ for page {}'.format(self.base_url))

    def test_slides_required_title_text(self):
        expected_text_included_in_slide = 'sample'
        slides_titles_xpath = '//*[@id="carousel"]/ul/li//*[contains(@class, "text-uppercase")]'
        driver = self.driver
        driver.get(self.base_url)
        title_elements = driver.find_elements_by_xpath(slides_titles_xpath)
        for title_element in title_elements:
            title_element_text = title_element.get_attribute("textContent")
            title_element_text_lower = title_element_text.lower()
            with self.subTest(title_element_text_lower):
                self.assertIn(expected_text_included_in_slide, title_element_text_lower,
                              "Slides does not contain expected text for page {}".format(self.base_url))

    def test_number_of_featured_products(self):
        expected_number_of_products = 8
        product_xpath = '//*[@class="product-miniature js-product-miniature"]'
        driver = self.driver
        driver.get(self.base_url)
        product_elements = driver.find_elements_by_xpath(product_xpath)
        actual_number_of_products = len(product_elements)
        self.assertEqual(expected_number_of_products, actual_number_of_products,
                         'Products number differ for page {}'.format(self.base_url))

import unittest

from selenium import webdriver


class LostHatFrontPageTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.base_url = 'http://autodemo.testoneo.com/en/'
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
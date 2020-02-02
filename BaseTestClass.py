import unittest

from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from helpers.screenshot_listener import ScreenshotListener


class BaseTestClass(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.subpage_art_url = self.base_url + '9-art'
        driver = webdriver.Chrome(executable_path=r"C:\Users\Dominika\Downloads\chromedriver_win32("
                                                  r"1)\chromedriver.exe")
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())

    @classmethod
    def tearDown(self):
        self.ef_driver.quit()
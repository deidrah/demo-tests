import unittest
from selenium import webdriver
from helpers import operational_helpers as oh


class LostHatShoppingCartTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.subpage_art_url = 'https://autodemo.testoneo.com/en/9-art'
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Dominika\Downloads\chromedriver_win32("
                                                       r"1)\chromedriver.exe")
        self.driver.implicitly_wait(10)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_adding_item_to_shopping_cart(self):
        expected_confirmation_modal_text = '\ue876Product successfully added to your shopping cart'
        item_xpath = '//*[@alt="Mountain fox - Vector graphics"]'
        shopping_cart_button_xpath = '//*[@class="btn btn-primary add-to-cart"]'
        confirmation_modal_title_xpath = '//*[@id="myModalLabel"]'
        driver = self.driver
        driver.get(self.subpage_art_url)
        item_element = driver.find_element_by_xpath(item_xpath)
        item_element.click()
        shopping_cart_button_element = driver.find_element_by_xpath(shopping_cart_button_xpath)
        shopping_cart_button_element.click()
        confirmation_modal_element = oh.visibility_of_element_wait(driver, confirmation_modal_title_xpath)
        self.assertEqual(expected_confirmation_modal_text, confirmation_modal_element.text)

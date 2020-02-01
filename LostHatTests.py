import unittest
from selenium import webdriver


class LostHatTests(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Dominika\Downloads\chromedriver_win32("
                                                       r"1)\chromedriver.exe")

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_login_text_header(self):
        expected_text = 'Log in to your account'
        driver = self.driver
        driver.get(self.login_url)
        header_element = driver.find_element_by_xpath('//header[@class="page-header"]')
        header_element_text = header_element.text
        self.assertEqual(expected_text, header_element_text,
                         f'Expected text differ from actual for page url: {self.login_url}')

    def test_correct_login(self):
        # expected_text is a user name and user surname used during registration
        expected_text = 'Adam Testowy'
        user_email = 'adam@testowy.pl'
        user_pass = 'test123'
        driver = self.driver
        driver.get(self.login_url)
        # finding login input box and sending value
        login_input_element = driver.find_element_by_xpath('//*[@type="email"]')
        login_input_element.send_keys(user_email)
        # finding password input box and sending value
        login_input_element = driver.find_element_by_xpath('//*[@type="password"]')
        login_input_element.send_keys(user_pass)
        # finding button 'sign in'
        button_next_element = driver.find_element_by_xpath('//*[@id="submit-login"]')
        button_next_element.click()
        header_element = driver.find_element_by_xpath('//a[@class="account"]/*[@class="hidden-sm-down"]')
        header_element_text = header_element.text
        self.assertEqual(expected_text, header_element_text,
                         f'Expected title differ from actual title for page url: {self.login_url}')

    def test_check_product_name_and_price(self):
        expected_product_name = 'HUMMINGBIRD PRINTED T-SHIRT'
        expected_product_price = 'PLN23.52'
        driver = self.driver
        driver.get(self.sample_product_url)
        name_element = driver.find_element_by_xpath('//*[@class="col-md-6"]//*[@itemprop="name"]')
        name_element_text = name_element.text
        self.assertEqual(expected_product_name, name_element_text,
                         f'Expected text differ from actual for page url: {self.sample_product_url}')
        price_element = driver.find_element_by_xpath('//*[@class="current-price"]//*[@itemprop="price"]')
        price_element_text = price_element.text
        self.assertEqual(expected_product_price, price_element_text,
                         f'Expected text differ from actual for page url: {self.sample_product_url}')
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_elements(driver, xpath, max_seconds_to_wait=5, number_of_expected_elements=1):
    """Checking every second if list of elements under specified xpath was found
          :param driver: webdriver instance
          :param xpath: xpath of web element
          :param max_seconds_to_wait: maximum time in seconds to wait for element (default: 5)
          :param number_of_expected_elements: specifies minimum number of  elements to be found
          :return: list of found elements
       """
    for seconds in range(max_seconds_to_wait):
        elements = driver.find_elements_by_xpath(xpath)
        print(f'Total waiting {seconds}s')
        if len(elements) >= number_of_expected_elements:
            return elements
        if seconds == (max_seconds_to_wait - 1):
            print('Wait end')
            assert len(elements) >= number_of_expected_elements, \
                f'Expected {number_of_expected_elements} elements but found {len(elements)} for xpath {xpath}'
        time.sleep(1)


def visibility_of_element_wait(driver, xpath, timeout=10):
    """Checking if element specified by xpath is visible on page
              :param driver: webdriver instance
              :param xpath: xpath of web element
              :param timeout: time after looking for element will be stopped (default: 10)
              :return: first element in list of found elements
           """
    timeout_message = f"Element for xpath: '{xpath}' and url: {driver.current_url} not found in {timeout} seconds"
    locator = (By.XPATH, xpath)
    element_located = EC.visibility_of_element_located(locator)
    wait = WebDriverWait(driver, timeout)
    return wait.until(element_located, timeout_message)

import time


def wait_for_elements(driver, xpath):
    """Checking every second if list of elements under specified xpath is greater than 0
          :param driver: webdriver instance
          :param xpath: xpath of web element
          :return: None
       """
    for seconds in range(5):
        elements = driver.find_elements_by_xpath(xpath)
        number_of_found_elements = len(elements)
        print(f'Total waiting {seconds}s')
        print(f'Found {number_of_found_elements}')
        if number_of_found_elements > 0:
            print('Element found')
            break
        time.sleep(1)

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from Basics.test_framework.utilities.logger import InfoLogger
from datetime import datetime


class MyDriverMethods:

    log = InfoLogger('debug').info_logger()

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title

    def take_screenshot(self, result_msg):
        dir_loc = r'H:\Softwares\Python files\Extras\Selenium_Automation\Basics\test_framework\screenshots and logs'
        time = str(datetime.today().replace(microsecond=0))
        time_str = ''.join(filter(str.isalnum, time))
        try:
            self.driver.save_screenshot(f'{dir_loc}\\SS-{result_msg}-{time_str}.png')
            self.log.info(f'Screenshot saved "SS-{result_msg}-{time_str}.png"')
        except:
            self.log.error(f'Exception occurred while taking screenshot - "SS-{result_msg}-{time_str}.png"')

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "class_name":
            return By.CLASS_NAME
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css_selector":
            return By.CSS_SELECTOR
        elif locator_type == "link_text":
            return By.LINK_TEXT
        else:
            self.log.error(f"Locator type {locator_type} not correct/supported")
        return False

    def get_element(self, locator, locator_type="id"):
        """
        available 'locator' types:
        id = By.ID, class_name = By.CLASS_NAME, name = By.CLASS_NAME, xpath = By.XPATH, css_selector = By.CSS_SELECTOR
        default_value = "id"
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info(f"Element {locator} found")
        except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException):
            self.log.error(f"Element {locator} not found")
        return element

    def get_element_list(self, locator, locator_type="id"):
        """
        available 'locator' types:
        id = By.ID, class_name = By.CLASS_NAME, name = By.CLASS_NAME, xpath = By.XPATH, css_selector = By.CSS_SELECTOR
        default_value = "id"
        :outparam = Returns list if elements
        """
        element_list = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element_list = self.driver.find_elements(by_type, locator)
            self.log.info(f"Element list {locator} found e.g {element_list[2].text}")
        except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException):
            self.log.error(f"Element list {locator} not found")
        return element_list

    def element_click(self, locator=None, locator_type="id", element=None):
        # pytest.set_trace()
        """
        available 'locator' types:
        id = By.ID, class_name = By.CLASS_NAME, name = By.CLASS_NAME, xpath = By.XPATH, css_selector = By.CSS_SELECTOR
        default_value = "id"
        """
        if element is None and locator is not None:
            try:
                self.get_element(locator, locator_type).click()
                self.log.info(f"Clicked on element with locator:{locator} with locator_type: {locator_type}")
            except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException):
                self.log.error(f"locator:{locator} with locator_type: {locator_type} is not clickable")
        else:
            try:
                element.click()
                self.log.info(f"Clicked on element with locator:{locator} with element: {element}")
            except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException):
                self.log.error(f"locator:{locator} with element: {element} is not clickable")

    def element_send_keys(self, data, locator, locator_type="id"):
        """
        available 'locator' types:
        id = By.ID, class_name = By.CLASS_NAME, name = By.CLASS_NAME, xpath = By.XPATH, css_selector = By.CSS_SELECTOR
        default_value = "id"
        """
        try:
            if data is None:
                raise ElementNotSelectableException
            self.get_element(locator, locator_type).send_keys(data)
            self.log.info(f"Data: {data} sent to element with locator:{locator} and locator_type: {locator_type}")
        except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException):
            self.log.error(f"Cannot send data: {data} to locator:{locator} and locator_type: {locator_type} is not "
                           f"clickable")

    def is_element_enabled(self, locator, locator_type="id"):
        """
        :returns bool
        """
        try:
            if self.get_element(locator, locator_type).is_enabled():
                self.log.info(f"Element at locator {locator}-({locator_type}) is enabled!")
                return True
            else:
                return False
        except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException):
            self.log.error(f"Element at locator {locator}-({locator_type}) is not enabled!")

    def get_value(self, locator, locator_type="id", attr_type="value"):
        _value_of_element = None
        try:
            _element = self.get_element(locator, locator_type)
            _value_of_element = _element.get_attribute(attr_type)
            self.log.info(f"Value of Element {_value_of_element} at locator {locator}-({locator_type}) is returned")
        except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException):
            self.log.error(f"Cannot get value of Element at locator {locator}-({locator_type})")
        return _value_of_element

    def select_element(self, data, locator, locator_type="id", select_by="index"):
        """
        available 'locator' types:
        id = By.ID, class_name = By.CLASS_NAME, name = By.CLASS_NAME, xpath = By.XPATH, css_selector = By.CSS_SELECTOR
        default_value = "id"
        -----------------------------------
        available 'select_by' options:
        value = select_by_value
        text = select_by_visible_text
        "default" = select_by_index
        -----------------------------------
        data:
            e.g. select_by('data')
        """
        try:
            element = self.get_element(locator, locator_type)
            select_by = select_by.lower()
            if select_by == "value":
                self.log.info(f'Selecting element at {locator} by value - {data}')
                return Select(element).select_by_value(data)
            elif select_by == "text":
                self.log.info(f'Selecting element at {locator} by text - {data}')
                return Select(element).select_by_visible_text(data)
            else:
                self.log.info(f'Selecting element at {locator} by index - {data}')
                return Select(element).select_by_index(data)
        except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException):
            self.log.error(f"Not able to Select value {data} at element {locator} by {locator_type}")

    def is_element_present(self, locator, locator_type="id"):
        element = None
        element = self.get_element(locator, locator_type)
        if element is not None:
            self.log.info(f'Element at location {locator} is present')
            return True
        else:
            self.log.error(f'Element at location {locator} is not present')
            return False

    def get_text_of_element(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            self.log.info(f'Text at Element {locator} is {element.text}')
            return element.text
        except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException):
            self.log.error(f'Element at {locator} does not exists')

    def scroll_page(self, direction='down', pixels='1000'):

        if direction.lower() == 'down':
            self.driver.execute_script(f"window.scrollBy(0, {pixels});")
            self.log.info(f'Page scrolled {direction} {pixels} pixels')
        else:
            self.driver.execute_script(f"window.scrollBy(0, -{pixels});")
            self.log.info(f'Page scrolled {direction} {pixels} pixels')

    def hover_element(self, locator=None, locator_type="id", element=None):
        try:
            self.log.info(f'Starting hover operation with {locator} - {locator_type} - {element}')
            if element is None and locator is not None:
                hov_element = self.get_element(locator, locator_type)
                self.log.info(f'Got element at {locator} to hover')
                hover = ActionChains(self.driver).move_to_element(hov_element)
                hover.perform()
                self.log.info(f'Hovered over element at {locator} by {locator_type}')
            else:
                self.log.info(f'Got element {element} to hover')
                hover = ActionChains(self.driver).move_to_element(element)
                hover.perform()
                self.log.info(f'Hovered over element {element}')
        except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException):
            self.log.error(f"Not able to hover at element {locator} by {locator_type} or element {element}")

from Basics.test_framework.base.common_operations import CommonOperations
import Basics.test_framework.pages.locators as lc
from Basics.test_framework.utilities.logger import InfoLogger
from time import sleep

class HomePageToCart(CommonOperations):

    log = InfoLogger('debug').info_logger()

    def __init__(self, driver):
        super(CommonOperations, self).__init__(driver)
        self.driver = driver

    def add_to_cart_home_page(self):
        product_list = self.get_element_list(lc.quick_cart_prod_list, 'xpath')
        product_view_list = self.get_element_list(lc.home_prod_list, 'xpath')
        self.scroll_page('down', '800')

        for elm in range(0, (len(product_list))):
            self.hover_element(element=product_view_list[elm])
            sleep(2)
            self.element_click(element=product_list[elm])
            self.element_click(locator=lc.continue_shopp, locator_type='xpath')
        cart_num_items = self.get_text_of_element(lc.home_cart_quantity, 'xpath')
        return cart_num_items

    def add_to_cart_home_view(self):
        product_view_list = self.get_element_list(lc.quick_cart_prod_view_list, 'xpath')

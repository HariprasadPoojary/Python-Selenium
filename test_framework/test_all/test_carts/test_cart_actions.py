import pytest
from unittest import TestCase
from Basics.test_framework.pages.cart_operation.home_page_to_cart import HomePageToCart
from Basics.test_framework.utilities.test_status import TestStatus

@pytest.mark.usefixtures("class_setup")
class TestAddToCartActions(TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, class_setup):
        self.hc = HomePageToCart(self.driver)
        self.test_stat = TestStatus()

    def test_add_tocart_homepage(self):
        num_items_cart = self.hc.add_to_cart_home_page()
        if num_items_cart == '7':
            self.test_stat.mark_final('test_add_tocart_homepage', True, 'Cart Number Verified')
        else:
            self.test_stat.mark_final('test_add_tocart_homepage', False, 'Cart Number Verified')

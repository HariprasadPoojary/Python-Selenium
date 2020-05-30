from Basics.test_framework.base.my_selenium_methods import MyDriverMethods
from Basics.test_framework.utilities.logger import InfoLogger

class CommonOperations(MyDriverMethods):

    log_co = InfoLogger('debug').info_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_title(self, title_name):
        actual_name = self.get_page_title()
        if actual_name == title_name:
            self.log_co.info(f'Page title {actual_name} matches to {title_name}')
            return True
        else:
            self.log_co.error(f'Page title {actual_name} does not matches to {title_name}')
            return False

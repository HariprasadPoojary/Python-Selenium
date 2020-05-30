import pytest
from unittest import TestCase
from Basics.test_framework.pages.account_operation.account import CreateAccount
from Basics.test_framework.utilities.test_status import TestStatus
from Basics.test_framework.utilities.utilities import Utilities
from Basics.test_framework.utilities.logger import InfoLogger
from Basics.test_framework.pages.locators import regist_signout
from ddt import ddt, data, unpack

@ddt
@pytest.mark.usefixtures("class_setup")
class TestCreateAccount(TestCase):

    log = InfoLogger('debug').info_logger()

    # Create an object of utility class by initializing excel sheet
    test_data_path = r'H:\Softwares\Python files\Extras\Selenium_Automation\Basics\test_framework\configfiles'
    excel_util = Utilities(excel_file=f'{test_data_path}\\test_data.xlsx', excel_sheet='CreateAccount')
    no_rows = excel_util.excel_rowcount()
    no_cols = excel_util.excel_columncount()

    # Get values of personal info and address info from excel
    personal_info = excel_util.excel_getlist_cellvalues(min_row=2, max_row=no_rows, min_col=1, max_col=8)
    address_info = excel_util.excel_getlist_cellvalues(min_row=2, max_row=no_rows, min_col=11, max_col=no_cols)
    log.info(personal_info)
    log.info(address_info)

    @pytest.fixture(autouse=True)
    def class_setup(self, class_setup):
        self.ca = CreateAccount(self.driver)
        self.test_stat = TestStatus()

    @pytest.mark.run(order=1)
    def test_already_registered_account(self):
        acc_name = self.ca.already_registered('bruce@wayne.com', 'HariPassword')
        self.test_stat.mark_final('test_already_registered_account', acc_name == 'Hariprasad Poojary', 'Verified')

    @pytest.mark.run(order=2)
    # @data((personal_info[0], address_info[0]), (personal_info[1], address_info[1]))
    @data(*(lambda x, y: [(x, y) for x, y in zip(x, y)])(personal_info, address_info))
    @unpack
    def test_create_account(self, personal_info, address_info):
        result_email, result_username = self.ca.create_account(personal_info, address_info)
        self.driver.find_element_by_xpath(regist_signout).click()
        self.test_stat.mark_final('test_create_account', result_email is True and result_username is True, 'Verified')

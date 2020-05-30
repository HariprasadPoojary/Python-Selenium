from Basics.test_framework.base.common_operations import CommonOperations
import Basics.test_framework.pages.locators as lc
from Basics.test_framework.utilities.logger import InfoLogger
import pdb
import time
from random import randint


class CreateAccount(CommonOperations):

    log = InfoLogger('debug').info_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def reach_signup(self, email):
        self.element_click(lc.sign_up, "xpath")
        self.element_send_keys(email, lc.create_email_add, "xpath")
        self.element_click(lc.create_acc_btn, "xpath")
        time.sleep(2)
        error = self.is_element_present(lc.register_error, "xpath")
        if error:
            self.scroll_page(pixels='500')
            self.take_screenshot('reach_signup')
        self.log.info('Reach Sign-up completed')
        return error

    def fill_details(self, personal, address):
        """
        accepts personal and address as list
        """
        time.sleep(1)
        if personal[0] == 'Mr.':
            self.element_click(lc.title_mr)
        else:
            self.element_click(lc.title_mrs)
        # Optional check boxes
        if personal[6] == 'Y':
            self.element_click(lc.check_newsletter)
        elif personal[7] == 'Y':
            self.element_click(lc.offers)
        else:
            pass
        same_email = self.get_value(lc.email)
        # personal_list
        self.element_send_keys(personal[1], lc.firstname)
        self.element_send_keys(personal[2], lc.lastname)
        self.element_send_keys(personal[4], lc.password)
        # Date of Birth
        day = personal[5].day
        month = personal[5].month
        year = personal[5].year
        self.select_element(f'{day}  ', lc.dob_day, select_by="text")
        self.select_element(month, lc.dob_month, select_by="index")
        self.select_element(f'{year}  ', lc.dob_year, select_by="text")
        # Address_list
        if self.get_value(lc.firstname) == self.get_value(lc.a_firstname) and \
                self.get_value(lc.lastname) == self.get_value(lc.a_lastname):
            self.log.info(f"Personal Info Name = {self.get_value(lc.firstname)} is equal to "
                          f"{self.get_value(lc.a_firstname)}")
        else:
            self.log.info(f"Personal Info Name = {self.get_value(lc.firstname)} is not equal to "
                          f"{self.get_value(lc.a_firstname)}")

        for value in range(0, len(address)):
            if value == 4:
                self.select_element(address[value], lc.address_details_list[value], 'id', select_by='text')
                continue
            self.element_send_keys(address[value], lc.address_details_list[value])

        self.take_screenshot('fill_details')
        self.element_click(lc.register_button)
        time.sleep(5)
        same_username = self.get_text_of_element(lc.register_name, 'xpath')

        return same_email, same_username

    def create_account(self, personal_addr, address):
        email = 'bruce@wayne.com'
        while self.reach_signup(email):
            email = f"bruce{randint(1, 201)}@wayne.com"

        correct_email, correct_username = self.fill_details(personal_addr, address)
        return email == correct_email, f'{personal_addr[1]} {personal_addr[2]}' == correct_username

    def already_registered(self, email, password):
        self.element_click(lc.sign_up, "xpath")
        self.element_send_keys(email, lc.regist_email, "id")
        self.element_send_keys(password, lc.regist_pass, "id")
        self.element_click(lc.regist_submit, "id")
        acc_name = self.get_text_of_element(lc.regist_acc_name, "xpath")
        self.take_screenshot('already_registered')
        self.element_click(lc.regist_signout, "xpath")
        return acc_name

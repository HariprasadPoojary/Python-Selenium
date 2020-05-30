from Basics.test_framework.utilities.logger import InfoLogger

class TestStatus:

    log_ts = InfoLogger('info').info_logger()

    def __init__(self):
        self.results = []

    def set_result(self, result=None, result_msg="Not defined"):
        try:
            if result is not None:
                if result:
                    self.results.append("PASS")
                    self.log_ts.info(f"** TEST VERIFICATION PASS:: {result_msg}")
                else:
                    self.results.append("FAIL")
                    self.log_ts.error(f"** TEST VERIFICATION FAIL:: {result_msg}")
            else:
                self.results.append("FAIL")
                self.log_ts.error(f"** TEST VERIFICATION FAIL:: {result_msg}")
        except:
            self.results.append("FAIL")
            self.log_ts.error(f"** EXCEPTION:: {result_msg}")

    def mark(self, result=None, result_msg='Not defined'):
        """
        :param result: TRUE or FALSE
        :param result_msg: Generic statement for better logging
        :return: None
        Mark the result of the verification point in a test case
        """
        self.set_result(result, result_msg)

    def mark_final(self, test_name='Not defined', result=None, result_msg='Not defined'):
        """
        :param test_name: Name of the test case which is calling this method
        :param result: TRUE or FALSE
        :param result_msg: Generic statement for better logging
        :return: None
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.set_result(result, result_msg)

        if "FAIL" in self.results:
            self.log_ts.error(f'Test {test_name} execution has been failed!!')
            self.results.clear()
            assert False
        else:
            self.log_ts.info(f'Test {test_name} execution has been passed!!')
            self.results.clear()
            assert True

import logging
import inspect
from datetime import datetime

class InfoLogger:

    def __init__(self, log_level):
        log_levels = {'debug': logging.DEBUG, 'info': logging.INFO, 'warning': logging.WARNING,
                      'error': logging.ERROR, 'critical': logging.CRITICAL}
        try:
            self.log_level = log_levels.get(log_level.lower()) or log_levels['none']
        except KeyError:
            self.log_level = log_levels.get('debug')

    def info_logger(self):

        # Get the name of the class / method from where this method is called
        logger_name = inspect.stack()[1][3]

        # Create logger
        logger = logging.getLogger(logger_name)  # or .getLogger('some name') or .getLogger('__name__')

        # Set log level for logger
        logging.basicConfig(level=self.log_level)

        # Create File handler object
        time = str(datetime.today().replace(microsecond=0))
        time_str = ''.join(filter(str.isalnum, time))
        path = r'H:\Softwares\Python files\Extras\Selenium_Automation\Basics\test_framework\screenshots and logs'
        file_handler = logging.FileHandler(f'{path}\\automation-{time_str}.log', mode='a')

        # Create a formatter
        log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
        file_handler.setFormatter(log_format)

        # Add logger
        logger.addHandler(file_handler)

        return logger

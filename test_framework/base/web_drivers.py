from selenium import webdriver

class WebDrivers:

    def __init__(self, browser):
        self.browser = browser

    def get_webdriver_instance(self):

        base_url = 'http://automationpractice.com/index.php'
        driver_path = r'H:\Softwares\Python files\Extras\web_drivers'
        if self.browser.lower() == 'opera':
            driver = webdriver.Opera(f"{driver_path}\\operadriver.exe")
        elif self.browser.lower() == 'ie':
            driver = webdriver.Ie(f"{driver_path}\\IEDriverServer.exe")
        else:
            driver = webdriver.Chrome(f"{driver_path}\\chromedriver.exe")

        driver.get(base_url)
        driver.implicitly_wait(3)
        driver.maximize_window()

        return driver

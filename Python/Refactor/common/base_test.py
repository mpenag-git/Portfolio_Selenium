import unittest

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from Refactor.common.config import Configuration as Config


class BaseTest(unittest.TestCase):
    URL_BASE = "http://opencart.abstracta.us"
    URL_LOGIN = URL_BASE + "/index.php?route=account/login"
    URL_LOGOUT = URL_BASE + "/index.php?route=account/logout"
    EMAIL = "test_automon_01@yopmail.com"
    PASS = "test1234"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__driver = None

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, driver_instance):
        self.__driver = driver_instance

    def setUp(self):

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        self.driver = Config.create_chrome_driver(options)
        self.wait = WebDriverWait(self.driver, 60)
        self.driver.get(self.URL_LOGIN)
        self.driver.maximize_window()

    def tearDown(self):
        # Logout
        self.driver.get(self.URL_LOGOUT)
        # Kill driver
        self.driver.quit()

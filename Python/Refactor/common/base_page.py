from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Refactor.common.config import Configuration as Config

class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except Exception as e:
            target_path = Config.get_screenshot_file_path("dashboard")
            self.driver.save_screenshot(target_path)
            raise e

    def find_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            target_path = Config.get_screenshot_file_path("dashboard")
            self.driver.save_screenshot(target_path)
            raise e

    def click_BTN_PAYMENT_METHOD(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator)).click()
        except Exception as e:
            target_path = Config.get_screenshot_file_path("dashboard")
            self.driver.save_screenshot(target_path)
            raise e

    def click(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except Exception as e:
            target_path = Config.get_screenshot_file_path("dashboard")
            self.driver.save_screenshot(target_path)
            raise e

    def send_keys(self, locator, text):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_visible(locator).text

    def is_displayed(self, locator):
        return self.find_visible(locator).is_displayed()
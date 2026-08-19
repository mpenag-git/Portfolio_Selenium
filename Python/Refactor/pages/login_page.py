from Refactor.common.base_page import BasePage
from Refactor.common.locators import Locators

class LoginPage(BasePage):
    def login(self, email, password):
        self.send_keys(Locators.TXT_EMAIL, email)
        self.send_keys(Locators.TXT_PASSWORD, password)
        self.click(Locators.BTN_SIGN_IN)

    def is_my_account_displayed(self):
        return self.is_displayed(Locators.LBL_MY_ACCOUNT)
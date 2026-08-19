from Refactor.common.base_page import BasePage
from Refactor.common.locators import Locators

class OrderSuccessPage(BasePage):
    def get_success_header(self):
        return self.get_text(Locators.LBL_SUCCESS_HEADER)

    def get_success_message_1(self):
        return self.get_text(Locators.LBL_SUCCESS_MSG_1)

    def get_success_message_2(self):
        return self.get_text(Locators.LBL_SUCCESS_MSG_2)

    def click_continue(self):
        self.click(Locators.BTN_CONTINUE)
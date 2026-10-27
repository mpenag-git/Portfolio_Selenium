from Refactor.common.base_page import BasePage
from Refactor.common.locators import Locators

class OrderSuccessPage(BasePage):

    def get_success_header(self):
        return self.get_text(Locators.LBL_SUCCESS_HEADER)

    def get_success_processed(self):
        return self.get_text(Locators.LBL_SUCCESS_PROCESSED)

    def get_success_thanks(self):
        return self.get_text(Locators.LBL_SUCCESS_THANKS)

    def click_continue(self):
        self.click(Locators.BTN_CONTINUE)

    """
    def get_success_text(self, text):
        if text == "Header":
                return self.get_text(Locators.LBL_SUCCESS_HEADER)
        elif text == "Processed":
                return self.get_text(Locators.LBL_SUCCESS_PROCESSED)
        elif text=="Thanks":
                return self.get_text(Locators.LBL_SUCCESS_THANKS)
        return None
    """
    #***********************
    """
    self.assertEqual('Your order has been placed!', success_page.get_success_text("Header"), "Order header mismatch")
    self.assertEqual('Your order has been successfully processed!', success_page.get_success_text("Processed"),
                     "Message success processed mismatch")
    self.assertEqual('Thanks for shopping with us online!', success_page.get_success_text("Thanks"),
                     "Message success thanks mismatch")
    """
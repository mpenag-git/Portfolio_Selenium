from Refactor.common.base_page import BasePage
from Refactor.common.locators import Locators

class CheckoutPage(BasePage):
    def complete_checkout_steps(self):
        self.click(Locators.BTN_PAYMENT_ADDRESS)
        self.click(Locators.BTN_SHIPPING_ADDRESS)
        self.click(Locators.BTN_SHIPPING_METHOD)
        self.click(Locators.CHK_AGREE)
        self.click(Locators.BTN_PAYMENT_METHOD)

    def get_confirmed_item_name(self):
        return self.get_text(Locators.CONFIRM_ITEM_NAME)

    def get_confirmed_total_price(self, total):
        return self.get_text(Locators.confirm_total_price(total))

    def confirm_order(self):
        self.click(Locators.BTN_CONFIRM_ORDER)
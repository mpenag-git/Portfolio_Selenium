from Refactor.common.base_page import BasePage
from Refactor.common.locators import Locators as lctrs

class CheckoutPage(BasePage):
    def complete_checkout_steps(self):
        self.click(lctrs.BTN_PAYMENT_ADDRESS)
        self.click(lctrs.BTN_SHIPPING_ADDRESS)
        self.click(lctrs.BTN_SHIPPING_METHOD)
        self.click(lctrs.CHK_AGREE)
        self.click_BTN_PAYMENT_METHOD(lctrs.BTN_PAYMENT_METHOD)

    def get_confirmed_item_name(self):
        return self.get_text(lctrs.CONFIRM_ITEM_NAME)

    def get_confirmed_total_price(self, total):
        return self.get_text(lctrs.confirm_total_price(total))

    def confirm_order(self):
        self.click(lctrs.BTN_CONFIRM_ORDER)
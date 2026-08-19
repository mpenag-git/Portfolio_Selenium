from Refactor.common.base_page import BasePage
from Refactor.common.locators import Locators

class CartPage(BasePage):
    def get_cart_item_price(self, price):
        return self.get_text(Locators.item_price_checkout(price))

    def proceed_to_checkout(self):
        self.click(Locators.BTN_CHECKOUT)
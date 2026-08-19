from Refactor.common.base_page import BasePage
from Refactor.common.locators import Locators

class PhonesPDAsPage(BasePage):
    def go_to_phones_category(self):
        self.click(Locators.LINK_PHONES_PDAS)

    def select_item(self, item_name):
        self.click(Locators.item_img_by_name(item_name))

    def get_item_name(self, item_name):
        return self.get_text(Locators.item_by_name(item_name))

    def get_detail_item_name(self, item_name):
        return self.get_text(Locators.item_name_detail(item_name))

    def get_item_price(self):
        return self.get_text(Locators.PRICE_WEB)

    def add_to_cart(self):
        self.click(Locators.BTN_ADD_TO_CART)

    def is_success_message_displayed(self):
        return self.is_displayed(Locators.MSG_SUCCESS)

    def open_cart(self):
        self.click(Locators.BTN_CART_CONTAINER)
        self.click(Locators.LINK_VIEW_CART)
from Refactor.common.base_page import BasePage
from Refactor.common.locators import Locators
from selenium.webdriver.support.select import Select

class CartPage(BasePage):
    def get_cart_item_price(self, price):
        return self.get_text(Locators.item_price_checkout(price))

    def proceed_to_checkout(self):
        self.click(Locators.BTN_CHECKOUT)

    def estimate_shipping_taxes(self, country, state):
        Zip_code=35601

        self.click(Locators.BTN_SHIPPING_TAXES)

        sl_opcion= self.find_visible(Locators.CBO_COUNTRY)
        lista_country = Select(sl_opcion)
        lista_country.select_by_visible_text(country)

        self.find(Locators.item_combo_selector(state))

        sl_2nd_opcion= self.find(Locators.CBO_STATE_LIST)
        lista_state = Select(sl_2nd_opcion)
        lista_state.select_by_visible_text(state)

        self.send_keys(Locators.CBO_ZIP,Zip_code)
        self.click(Locators.BTN_QUOTES)
        self.click(Locators.RDO_RATE)
        self.click(Locators.BTN_SHIPPING)

    def get_success_shipping_msg(self):
        msg_txt = self.get_text(Locators.LBL_SUCCESS_SHIPPING)
        clean_txt = msg_txt.replace("\n×", "")
        return clean_txt


        '''
        for opcion in Select(sl_2nd_opcion).options:
            print(
                f"Texto: '{opcion.text}' | "
                f"Value: '{opcion.get_attribute('value')}'"
            )
        '''

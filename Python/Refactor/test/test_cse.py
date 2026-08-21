import unittest
import HtmlTestRunner
from Refactor.common.CSVReader import CSV_Reader
from Refactor.common.base_test import BaseTest
from Refactor.pages.login_page import LoginPage
from Refactor.pages.phones_pdas_page import PhonesPDAsPage
from Refactor.pages.cart_page import CartPage
from Refactor.pages.checkout_page import CheckoutPage
from Refactor.pages.order_success_page import OrderSuccessPage
from Refactor.common.config import Configuration as Config


class CSETest(BaseTest):

    def test_buy_item(self):
        # Data Setup / DATA SET items.csv
        # Possible
        reader = CSV_Reader(Config.FileCSV)
        field = reader.read_random_row()

        item_name_list = field["item"]
        price = f"{(field['price']):.2f}"
        rate = f"{(field['rate']):.2f}"
        total_price = f"{(float(price) + float(rate)):.2f}"

        # Page Objects Initialization
        login_page = LoginPage(self.driver)
        phones_page = PhonesPDAsPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        success_page = OrderSuccessPage(self.driver)

        # 1. Login
        login_page.login(BaseTest.EMAIL, BaseTest.PASS)
        self.assertTrue(login_page.is_my_account_displayed(), "Assert My Account page es visible")

        # 2. Web Page: Phones & PDAs
        phones_page.go_to_phones_category()
        self.assertEqual(item_name_list, phones_page.get_item_name(item_name_list), "Verify name item")

        phones_page.select_item(item_name_list)
        self.assertEqual(item_name_list, phones_page.get_detail_item_name(item_name_list), "Verify name item detail")
        self.assertEqual(f'${price}', phones_page.get_item_price(), "Verify price item detail")

        phones_page.add_to_cart()
        self.assertTrue(phones_page.is_success_message_displayed(), "Success message not visible")
        phones_page.open_cart()

        # 3. Web Page: checkout/cart
        self.assertEqual(f'${price}', cart_page.get_cart_item_price(price), "Verify price item in cart")
        cart_page.proceed_to_checkout()

        # 4. Web Page: checkout/checkout
        checkout_page.complete_checkout_steps()
        self.assertEqual(item_name_list, checkout_page.get_confirmed_item_name(), "Verify name item in summary")
        self.assertEqual(f'${total_price}', checkout_page.get_confirmed_total_price(total_price), "Verify total price")
        checkout_page.confirm_order()

        # 5. Order Success Validation
        self.assertEqual('Your order has been placed!', success_page.get_success_header(), "Order header mismatch")
        self.assertEqual('Your order has been successfully processed!', success_page.get_success_message_1(),
                         "Message 1 mismatch")
        self.assertEqual('Thanks for shopping with us online!', success_page.get_success_message_2(),
                         "Message 2 mismatch")

        target_path = Config.get_screenshot_file_path("dashboard")
        self.driver.save_screenshot(target_path)
        success_page.click_continue()


if __name__ == '__main__':
    #unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'\reportHtmlRunner'))
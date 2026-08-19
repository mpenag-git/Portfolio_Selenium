import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from common.base_test import BaseTest
from Test.login import Login


class CSETest(BaseTest):
    def test_buy_item(self):

        # *** Web Page: Login ***
        login_ok = Login.do_login(self.driver, self.wait, BaseTest.EMAIL, BaseTest.PASS)
        # Validar que el login fue exitoso
        self.assertTrue(login_ok, "Assert My Account page es visible")

        # *** Web Page: Phones & PDAs ***
            #select phone
        self.driver.find_element(By.LINK_TEXT, "Phones & PDAs").click()
        itemNameList = 'iPhone'
        price =f"{101.00:.2f}"
        rate=f"{5.00:.2f}"
        item_name = self.driver.find_element(By.XPATH, f"//div[@class='caption']//a[contains(text(),'{itemNameList}')]")
            #Validate name item
        self.assertEqual(itemNameList, item_name.text, "Verify name item")
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, f"//div[@class='image']//img[@title='{itemNameList}']"))).click()
            # Validate name item
        item_name_detail = self.driver.find_element(By.XPATH, f"(//h1[normalize-space()='{itemNameList}'])[1]")
        self.assertEqual(itemNameList, item_name_detail.text, "Verify name item detail")
            # Validate price name item
        price_web = self.driver.find_element(By.XPATH,"//ul[@class='list-unstyled']//h2")
        self.assertEqual('$'+str(price), price_web.text, "Verify name item detail")
            # Click on Add to Cart
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID, "button-cart"))).click()
            # Validate success message
        self.assertTrue(
            self.wait.until(expected_conditions.visibility_of_element_located(
                    (By.XPATH, "//*[starts-with(text(), 'Success: You have added ')]")
                )).is_displayed(),"Success")
            #Click on Cart Button
        self.driver.find_element(By.XPATH, "//div[@id='cart']").click()
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//strong[normalize-space()='View Cart']"))).click()

        # *** Web Page: checkout/cart ***
            #validate price
        price_check = self.driver.find_element(By.XPATH, f"(//td[contains(text(),'{price}')])[7]")
        self.assertEqual('$'+str(price), price_check.text, "Verify price item detail")
            # Click on "Checkout" Button
        self.driver.find_element(By.CSS_SELECTOR, "a[class='btn btn-primary']").click()

        # *** Web Page: checkout/checkout ***
            #Step 2
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID, "button-payment-address"))).click()
            #Step 3
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID, "button-shipping-address"))).click()
            #Step 4
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID, "button-shipping-method"))).click()
            #Step 5
        self.wait.until(expected_conditions.element_to_be_clickable((By.NAME, "agree"))).click()
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID, "button-payment-method"))).click()
            #Step 6
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "(//td[@class='text-left']/a)[2]")))
            # Validate name item
        self.assertEqual(itemNameList, self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "(//td[@class='text-left']/a)[2]"))).text,
                         "Verify name item")
            # Validate price item
        calculo= float(price)+float(rate)
        Calc = f"{calculo:.2f}"

        self.assertEqual('$'+str(Calc), self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, f"(//td[normalize-space() = '${Calc}'])[1]"))).text,
                         "Verify price item")
            # Click on "Confirm Order" Button
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID, "button-confirm"))).click()

        # *** Web Page: checkout/checkout ***
        self.assertEqual('Your order has been placed!', self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "(//h1[normalize-space()='Your order has been placed!'])"))).text,
                         "Order successfull")
        self.assertEqual('Your order has been successfully processed!', self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//p[normalize-space()='Your order has been successfully processed!']"))).text,
                         "Order successfull")
        self.assertEqual('Thanks for shopping with us online!', self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//p[normalize-space()='Thanks for shopping with us online!']"))).text,
                         "Order successfull")
             # Click on "Continue" Button
        self.wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))).click()

if __name__ == '__main__':
    unittest.main()

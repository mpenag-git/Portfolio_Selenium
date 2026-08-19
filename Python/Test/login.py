import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

class Login(unittest.TestCase):
    @staticmethod
    def do_login(driver, wait, email, password):
        txt_email = wait.until(expected_conditions.presence_of_element_located((By.ID, "input-email")))
        txt_email.send_keys(email)

        txt_password = wait.until(expected_conditions.visibility_of_element_located((By.ID, "input-password")))
        txt_password.send_keys(password)

        btn_sign_in = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@type='submit' and @value='Login']")))
        btn_sign_in.click()

        lbl_my_account = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'My Account')]")))

        return lbl_my_account.is_displayed()

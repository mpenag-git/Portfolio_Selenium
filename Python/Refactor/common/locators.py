from selenium.webdriver.common.by import By

class Locators:
    # Login Page
    TXT_EMAIL = (By.ID, "input-email")
    TXT_PASSWORD = (By.ID, "input-password")
    BTN_SIGN_IN = (By.XPATH, "//*[@type='submit' and @value='Login']")
    LBL_MY_ACCOUNT = (By.XPATH, "//h2[contains(text(), 'My Account')]")

    # Navigation Header
    LINK_PHONES_PDAS = (By.LINK_TEXT, "Phones & PDAs")

    # Phones & PDAs / Item Detail
    @staticmethod
    def item_by_name(name):
        return (By.XPATH, f"//div[@class='caption']//a[contains(text(),'{name}')]")

    @staticmethod
    def item_img_by_name(name):
        return (By.XPATH, f"//div[@class='image']//img[@title='{name}']")

    @staticmethod
    def item_name_detail(name):
        return (By.XPATH, f"(//h1[normalize-space()='{name}'])[1]")

    PRICE_WEB = (By.XPATH, "//ul[@class='list-unstyled']//h2")
    BTN_ADD_TO_CART = (By.ID, "button-cart")
    MSG_SUCCESS = (By.XPATH, "//*[starts-with(text(), 'Success: You have added ')]")
    BTN_CART_CONTAINER = (By.XPATH, "//div[@id='cart']")
    LINK_VIEW_CART = (By.XPATH, "//strong[normalize-space()='View Cart']")

    # Cart Page
    @staticmethod
    def item_price_checkout(price):
        return (By.XPATH, f"(//td[contains(text(),'{price}')])[7]")

    BTN_CHECKOUT = (By.CSS_SELECTOR, "a[class='btn btn-primary']")

    # Checkout Page
    BTN_PAYMENT_ADDRESS = (By.ID, "button-payment-address")
    BTN_SHIPPING_ADDRESS = (By.ID, "button-shipping-address")
    BTN_SHIPPING_METHOD = (By.ID, "button-shipping-method")
    CHK_AGREE = (By.NAME, "agree")
    BTN_PAYMENT_METHOD = (By.ID, "button-payment-method")
    CONFIRM_ITEM_NAME = (By.XPATH, "(//td[@class='text-left']/a)[2]")

    @staticmethod
    def confirm_total_price(price):
        return (By.XPATH, f"(//td[normalize-space() = '${price}'])[1]")

    BTN_CONFIRM_ORDER = (By.ID, "button-confirm")

    # Order Success Page
    LBL_SUCCESS_HEADER = (By.XPATH, "(//h1[normalize-space()='Your order has been placed!'])")
    LBL_SUCCESS_MSG_1 = (By.XPATH, "//p[normalize-space()='Your order has been successfully processed!']")
    LBL_SUCCESS_MSG_2 = (By.XPATH, "//p[normalize-space()='Thanks for shopping with us online!']")
    BTN_CONTINUE = (By.CLASS_NAME, "btn-primary")
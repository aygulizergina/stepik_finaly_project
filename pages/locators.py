from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_ADD = (By.CSS_SELECTOR, "div.alertinner")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
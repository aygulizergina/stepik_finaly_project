from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is presented"

    def should_be_login_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_form"), "Login form is presented"

    def should_be_register_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#register_form"), "Register form is presented"

    def register_new_user(self, email, password = "12abc345cdf"):
        self.browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()


        

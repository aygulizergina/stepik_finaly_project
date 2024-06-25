from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def add_product_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        login_link.click()

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), "Product name is not presented"
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD), "Message about adding is not presented"

        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        message_add = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD).text

        assert name_product == message_add, "No product name in the message"

    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), "Product price is not presented"
        assert self.is_element_present(*ProductPageLocators.PRICE_BASKET), "Message basket total is not presented"

        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text

        assert price_product == price_basket, "No product price in the message" 

    
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
    
    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "The element has not disappeared"

        
        

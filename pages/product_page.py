from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        login_link.click()

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), "Product name is not presented"
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD), "Message about adding is not presented"

        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        message_add = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD).text

        assert name_product in message_add, "No product name in the message"

    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), "Product price is not presented"
        assert self.is_element_present(*ProductPageLocators.PRICE_BASKET), "Message basket total is not presented"

        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text

        assert price_product in price_basket, "No product price in the message" 
    


        
        

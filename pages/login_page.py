from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректность url адреса
        assert "login" in browser.current_url, "Login link is presented"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(By.CSS_SELECTOR, "#login_form"), "Login form is presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(By.CSS_SELECTOR, "#register_form"), "Register form is presented"
import allure

from data import User
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage

class LoginPage(BasePage):
    @allure.step('Загрузка драйвера')
    def __init__(self, driver):
        super().__init__(driver)  # Вызов конструктора родительского класса

    @allure.step('Авторизация под действующим пользователем')
    def authorization_under_current_user(self):
        self.send_keys(LoginPageLocators.EMAIL, val=User.EMAIL)
        self.send_keys(LoginPageLocators.PASSWORD, val=User.PASSWORD)
        self.click_by_element(LoginPageLocators.BUTTON_ENTER)

    @allure.step('Клик на ссылку "Восстановить пароль"')
    def click_link(self):
        self.click_by_element(LoginPageLocators.LINK_RECOVER_PASSWORD)

    @allure.step('Отражение формы авторизации')
    def form_authorization_visible(self):
        return self.wait_and_find_element(LoginPageLocators.FORM_AUTHORIZATION)
import allure

from data import User
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    @allure.step('Загрузка драйвера')
    def __init__(self, driver):
        super().__init__(driver)  # Вызов конструктора родительского класса

    @allure.step('Клик на кнопку "Восстановить" в окне "Восстановление пароля"')
    def click_button_recovery(self):
        self.click_by_element(ForgotPasswordPageLocators.BUTTON_RECOVERY)

    @allure.step('Ввод пароля в окне "Восстановление пароля"')
    def input_email(self):
        self.send_keys(ForgotPasswordPageLocators.PASSWORD, val=User.PASSWORD)

    @allure.step('Клик по кнопке "показать/скрыть пароль" в окне "Восстановление пароля"')
    def click_button_show_hide_password(self):
        self.click_by_element(ForgotPasswordPageLocators.BUTTON_PASSWORD_SHOW)

    @allure.step('В поле "Пароль" становится виден введенный пароль')
    def password_visible(self):
        return self.is_displayed(ForgotPasswordPageLocators.PASSWORD_SHOW)
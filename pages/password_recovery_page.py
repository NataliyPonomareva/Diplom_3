import allure

from data import User
from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):
    @allure.step('Загрузка драйвера')
    def __init__(self, driver):
        super().__init__(driver)  # Вызов конструктора родительского класса

    @allure.step('Клик на кнопку "Личный кабинет"')
    def click_button_personal_account(self):
        self.click_by_element(PasswordRecoveryLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик на ссылку "Восстановить пароль"')
    def click_link(self):
        self.click_by_element(PasswordRecoveryLocators.LINK_RECOVER_PASSWORD)

    @allure.step('Ввод почты в окне "Восстановление пароля"')
    def input_email(self):
       self.send_keys(PasswordRecoveryLocators.EMAIL, val=User.EMAIL)

    @allure.step('Клик на кнопку "Восстановить" в окне "Восстановление пароля"')
    def click_button_recovery(self):
        self.click_by_element(PasswordRecoveryLocators.BUTTON_RECOVERY)

    @allure.step('Ввод пароля в окне "Восстановление пароля"')
    def input_email(self):
        self.send_keys(PasswordRecoveryLocators.PASSWORD, val=User.PASSWORD)

    @allure.step('Клик по кнопке "показать/скрыть пароль" в окне "Восстановление пароля"')
    def click_button_show_hide_password(self):
        self.click_by_element(PasswordRecoveryLocators.BUTTON_PASSWORD_SHOW)

    @allure.step('В поле "Пароль" становится виден введенный пароль')
    def password_visible(self):
        return self.is_displayed(PasswordRecoveryLocators.PASSWORD_SHOW)

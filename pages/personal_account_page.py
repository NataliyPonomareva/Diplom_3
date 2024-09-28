import allure

from data import User
from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage

class PersonalAccountPage(BasePage):
    @allure.step('Загрузка драйвера')
    def __init__(self, driver):
        super().__init__(driver)  # Вызов конструктора родительского класса

    @allure.step('Клик на кнопку "Личный кабинет"')
    def click_button_personal_account(self):
        self.click_by_element(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Авторизация под действующим пользователем')
    def authorization_under_current_user(self):
        self.send_keys(PersonalAccountLocators.EMAIL, val=User.EMAIL)
        self.send_keys(PersonalAccountLocators.PASSWORD, val=User.PASSWORD)
        self.click_by_element(PersonalAccountLocators.BUTTON_ENTER)

    @allure.step('Дождаться загрузки конструктора')
    def wait_and_find_form_constructor(self):
        self.wait_and_find_element(PersonalAccountLocators.FORM_CONSTRUCTOR)

    @allure.step('Клик на поле "История заказов"')
    def click_order_history(self):
        self.click_by_element(PersonalAccountLocators.ORDER_HISTORY)

    @allure.step('Дождаться загрузки списка заказов')
    def wait_and_find_order_history(self):
        self.wait_and_find_element(PersonalAccountLocators.LIST_ORDER_HISTORY)

    @allure.step('Клик на кнопку "Выход"')
    def click_button_exit(self):
        self.click_by_element(PersonalAccountLocators.BUTTON_EXIT)

    @allure.step('Отражение формы авторизации')
    def form_authorization_visible(self):
        return self.is_displayed(PersonalAccountLocators.LIST_ORDER_HISTORY)


import allure

from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage

class ProfilePage(BasePage):
    @allure.step('Загрузка драйвера')
    def __init__(self, driver):
        super().__init__(driver)  # Вызов конструктора родительского класса

    @allure.step('Клик на поле "История заказов"')
    def click_order_history(self):
        self.click_by_element(ProfilePageLocators.ORDER_HISTORY)

    @allure.step('Дождаться загрузки списка заказов')
    def wait_and_find_order_history(self):
        self.wait_and_find_element(ProfilePageLocators.LIST_ORDER_HISTORY)

    @allure.step('Клик на кнопку "Выход"')
    def click_button_exit(self):
        self.click_by_element(ProfilePageLocators.BUTTON_EXIT)

    @allure.step('Отражение "История заказов"')
    def order_history_visible(self):
        return self.is_displayed(ProfilePageLocators.LIST_ORDER_HISTORY)

import allure


from data import User, Urls
from locators.order_history_page_locators import OrderHistoryPageLocators
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):
    @allure.step('Загрузка драйвера')
    def __init__(self, driver):
        super().__init__(driver)  # Вызов конструктора родительского класса

    @allure.step('Получить id заказа в Истории заказов авторизованного пользователя')
    def get_id_orders_from_history(self, order_id):
        return self.check_order_id(order_id, locator=OrderHistoryPageLocators.ALL_ORDERS_USERS_IN_HISTORY)


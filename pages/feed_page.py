import allure


from data import Urls
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    @allure.step('Загрузка драйвера')
    def __init__(self, driver):
        super().__init__(driver)  # Вызов конструктора родительского класса

    @allure.step('Перейти на страницу "Лента Заказов"')
    def open_page_order_feed(self):
        self.open_page(Urls.BASE_URL + Urls.ORDER_FEED_URL)

    @allure.step('Отражение формы "Лента заказов"')
    def visible_order_feed(self):
        self.wait_and_find_element(FeedPageLocators.FORM_ORDER_FEED)
        return self.is_displayed(FeedPageLocators.FORM_ORDER_FEED)

    @allure.step('Клик на карточку заказа')
    def click_card_order(self):
        self.click_by_element(FeedPageLocators.CARD_ORDER)

    @allure.step('Появилось окно с деталями заказа')
    def open_window_with_details_order(self):
        self.wait_and_find_element(locator=FeedPageLocators.WINDOW_WITH_DETAILS_ORDER)
        return self.is_displayed(locator=FeedPageLocators.WINDOW_WITH_DETAILS_ORDER)

    @allure.step('Найти номер заказа в ленте заказов')
    def is_number_order_users_in_feed(self, order_id):
        return self.check_order_id(order_id, locator=FeedPageLocators.ALL_ORDERS_USERS_IN_FEED)

    @allure.step('Проверяем отражение закозов из "Истории заказов" пользователя в "Ленте заказов"')
    def check_orders_in_order_feed(self, list1, list2):
        return all(value in list2 for value in list1)

    @allure.step('Посмотреть сколько зaказов отражается на счетчике "Выполненно сегодня"')
    def get_counter_completed_today(self):
        return self.wait_and_find_element(locator=FeedPageLocators.COUNTER_COMPLETED_TODAY).text

    @allure.step('Посмотреть скользоказов отражается на счетчике "Выполненно за все время"')
    def get_counter_completed_for_all_time(self):
        return self.wait_and_find_element(locator=FeedPageLocators.COUNTER_COMPLETED_FOR_ALL_TIME).text

    @allure.step('Созданный заказ находится в разделе "В работе"')
    def get_order_numbers_in_progress(self):
        elements = self.wait_and_find_element(FeedPageLocators.ORDER_IN_PROGRESS)
        return elements
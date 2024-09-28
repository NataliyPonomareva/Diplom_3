import allure


from data import User, Urls
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step('Загрузка драйвера')
    def __init__(self, driver):
        super().__init__(driver)  # Вызов конструктора родительского класса

    @allure.step('Клик на кнопку "Личный кабинет"')
    def click_button_personal_account(self):
        self.click_by_element(OrderFeedLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик на кнопку "Лента заказов"')
    def click_button_order_feed(self):
        #self.click_by_remote_element(OrderFeedLocators.BUTTON_ORDER_FEED)
        self.wait_until_element_visibility(OrderFeedLocators.BUTTON_ORDER_FEED)
        self.move_to_element_and_click(OrderFeedLocators.BUTTON_ORDER_FEED)
        self.wait_until_element_visibility(OrderFeedLocators.TITLE_ORDER_FEED)

    @allure.step('Клик на карточку заказа')
    def click_card_order(self):
        self.click_by_element(OrderFeedLocators.CARD_ORDER)

    @allure.step('Появилось окно с деталями заказа')
    def open_window_with_details_order(self):
        self.wait_and_find_element(locator=OrderFeedLocators.WINDOW_WITH_DETAILS_ORDER)
        return self.is_displayed(locator=OrderFeedLocators.WINDOW_WITH_DETAILS_ORDER)

    @allure.step('Авторизация под действующим пользователем')
    def authorization_under_current_user(self):
        self.send_keys(locator=OrderFeedLocators.EMAIL, val=User.EMAIL)
        self.send_keys(locator=OrderFeedLocators.PASSWORD, val=User.PASSWORD)
        self.click_by_element(locator=OrderFeedLocators.BUTTON_ENTER)

    @allure.step('Клик на кнопку "Конструктор"')
    def click_button_constructor(self):
        self.click_by_element(locator=OrderFeedLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Добавление булки для заказа бургера')
    def add_bun(self):
        bun = self.wait_and_find_element(locator=OrderFeedLocators.INGREDIENT_ICON)
        burger_constructor = self.wait_and_find_element(locator=OrderFeedLocators.BURGER_CONSTRUCTOR)
        self.drag_and_drop_element(element_to_drag=bun, target_location=burger_constructor)

    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_button_create_order(self):
        self.click_by_remote_element(locator=OrderFeedLocators.BUTTON_CREATE_ORDER)

    @allure.step('Закрыть окно, подтверждащее оформление заказа')
    def closing_window_create_order(self):
        self.wait_and_find_element(locator=OrderFeedLocators.CLOSE_WINDOW_CREATE_ORDER)
        self.click_by_element(locator=OrderFeedLocators.CLOSE_WINDOW_CREATE_ORDER)

    @allure.step('Подождать закрытия окна, подтверждащего оформление заказа')
    def wait_closing_window_create_order(self):
        self.wait_closing_element(locator=OrderFeedLocators.CLOSE_WINDOW_CREATE_ORDER)

    @allure.step('Клик на поле "История заказов"')
    def click_order_history(self):
        self.click_by_remote_element(locator=OrderFeedLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Нажатие кнопки "Личный кабинет" после оформления заказа')
    def click_account_button(self):
        self.wait_and_find_element(locator=OrderFeedLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_by_element(locator=OrderFeedLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_new_url(data=Urls.PROFILE_URL)

    @allure.step('Запомнить номер заказа, отраженный в окне с подтверждением оформления ')
    def get_order_id(self):
        self.wait_until_element_visibility(locator=OrderFeedLocators.ORDER_IDENTIFICATOR)
        order_id = self.get_text_on_element(locator=OrderFeedLocators.ORDER_ID)
        while order_id == '9999':
            order_id = self.get_text_on_element(locator=OrderFeedLocators.ORDER_ID)
        return f"{order_id}"

    @allure.step('Получить id заказа в Истории заказов авторизованного пользователя')
    def get_id_orders_from_history(self, order_id):
        return self.check_order_id(order_id, locator=OrderFeedLocators.ALL_ORDERS_USERS_IN_HISTORY)

    @allure.step("Получить id заказов в ленте заказов")
    def get_orders_from_orders_feed(self):
        elements = self.find_elements(locator=OrderFeedLocators.ALL_ORDERS_USERS_IN_FEED)
        orders_feed = [element.text for element in elements]
        return orders_feed

    @allure.step('Перейти на страницу "Лента Заказов"')
    def open_page_order_feed(self):
        self.open_page(Urls.ORDER_FEED_URL)

    @allure.step('Найти номер заказа в ленте заказов')
    def is_number_order_users_in_feed(self, order_id):
        return self.check_order_id(order_id, locator=OrderFeedLocators.ALL_ORDERS_USERS_IN_FEED)

    @allure.step('Проверяем отражение закозов из "Истории заказов" пользователя в "Ленте заказов"')
    def check_orders_in_order_feed(self, list1, list2):
        return all(value in list2 for value in list1)

    @allure.step('Посмотреть скользоказов отражается на счетчике "Выполненно сегодня"')
    def get_counter_completed_today(self):
        return self.wait_and_find_element(locator=OrderFeedLocators.COUNTER_COMPLETED_TODAY).text

    @allure.step('Посмотреть скользоказов отражается на счетчике "Выполненно за все время"')
    def get_counter_completed_for_all_time(self):
        return self.wait_and_find_element(locator=OrderFeedLocators.COUNTER_COMPLETED_FOR_ALL_TIME).text

    @allure.step('Созданный заказ находится в разделе "В работе"')
    def get_order_numbers_in_progress(self):
        elements = self.wait_and_find_element(OrderFeedLocators.ORDER_IN_PROGRESS)
        return elements
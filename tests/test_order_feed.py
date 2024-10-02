import allure

from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from pages.profile_page import ProfilePage


class TestOrderFeed:
    @allure.title('Открытие всплывающего окна с деталями заказа')
    def test_open_window_with_details_order(self, driver):
        window_with_details_order = MainPage(driver) # Открытие стартовой странице сервиса
        window_with_details_order.click_button_order_feed() # Клик на поле "Лента заказов"
        window_with_details_order = FeedPage(driver)
        window_with_details_order.click_card_order() # Клик на карточку заказа

        assert window_with_details_order.open_window_with_details_order() # Появилось окно с деталями заказа

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_users_in_feed(self, driver):
        order_users = MainPage(driver)  # Открытие стартовой странице сервиса
        order_users.click_button_personal_account() # Клик на кнопку "Личный кабинет"
        order_users = LoginPage(driver)
        order_users.authorization_under_current_user()  # Авторизация под действующим пользователем
        order_users = MainPage(driver)
        order_users.add_bun()  # Добавление булки для заказа бургера
        order_users.click_button_create_order()  # Клик на кнопку "Оформить заказ"
        order_id = order_users.get_order_id() # Запомнить номер заказа, отраженный в окне с подтверждением оформления
        order_users.closing_window_create_order()  # Закрыть окно, подтверждащее оформление заказа
        order_users.wait_closing_window_create_order() # Подождать закрытия окна, подтверждащего оформление заказа
        order_users.click_account_button()  # Клик на кнопку "Личный кабинет"
        order_users = ProfilePage(driver)
        order_users.click_order_history()  # Клик на поле "История заказов"
        order_users = OrderHistoryPage(driver)
        id_in_history_orders = order_users.get_id_orders_from_history(order_id) # Получить id заказа в Истории заказов авторизованного пользователя
        order_users = MainPage(driver)
        order_users.click_button_order_feed() # Клик на кнопку "Лента заказов"
        order_users = FeedPage(driver)
        id_in_feed_orders = order_users.is_number_order_users_in_feed(order_id) # Получить id заказа в Ленте заказов
        assert id_in_history_orders and id_in_feed_orders

    @allure.title('Проверка обновления счетчика "Выполненно сегодня"')
    def test_update_counter_competed_today(self, driver):
        counter_competed_today = MainPage(driver)  # Открытие стартовой странице сервиса
        counter_competed_today.click_button_order_feed()  # Клик на кнопку "Лента заказов"
        counter_competed_today = FeedPage(driver)
        old_counter = counter_competed_today.get_counter_completed_today()  # Посмотреть сколько заказов отражается на счетчике "Выполненно сегодня"
        counter_competed_today = MainPage(driver)
        counter_competed_today.click_button_personal_account() # Клик на кнопку "Личный кабинет"
        counter_competed_today = LoginPage(driver)
        counter_competed_today.authorization_under_current_user()  # Авторизация под действующим пользователем
        counter_competed_today = MainPage(driver)
        counter_competed_today.add_bun() # Добавление булки для заказа бургера
        counter_competed_today.click_button_create_order()  # Клик на кнопку "Оформить заказ"
        counter_competed_today.closing_window_create_order()  # Закрыть окно, подтверждащее оформление заказа
        counter_competed_today.wait_closing_window_create_order()  # Подождать закрытия окна, подтверждащего оформление заказа
        counter_competed_today.click_button_order_feed() # Клик на кнопку "Лента заказов"
        counter_competed_today = FeedPage(driver)
        new_counter = counter_competed_today.get_counter_completed_today() # Посмотреть сколько заказов отражается на счетчике "Выполненно сегодня"
        assert int(new_counter) > int(old_counter)

    @allure.title('Проверка обновления счетчика "Выполненно за все время"')
    def test_update_counter_competed_for_all_time(self, driver):
        counter_competed_today = MainPage(driver)  # Открытие стартовой странице сервиса
        counter_competed_today.click_button_order_feed()  # Клик на кнопку "Лента заказов"
        counter_competed_today = FeedPage(driver)
        old_counter = counter_competed_today.get_counter_completed_for_all_time()  # Посмотреть сколько заказов отражается на счетчике "Выполненно за все время"
        counter_competed_today = MainPage(driver)
        counter_competed_today.click_button_personal_account() # Клик на кнопку "Личный кабинет"
        counter_competed_today = LoginPage(driver)
        counter_competed_today.authorization_under_current_user()  # Авторизация под действующим пользователем
        counter_competed_today = MainPage(driver)
        counter_competed_today.add_bun() # Добавление булки для заказа бургера
        counter_competed_today.click_button_create_order()  # Клик на кнопку "Оформить заказ"
        counter_competed_today.closing_window_create_order()  # Закрыть окно, подтверждащее оформление заказа
        counter_competed_today.wait_closing_window_create_order()  # Подождать закрытия окна, подтверждащего оформление заказа
        counter_competed_today.click_button_order_feed() # Клик на кнопку "Лента заказов"
        counter_competed_today = FeedPage(driver)
        new_counter = counter_competed_today.get_counter_completed_for_all_time() # Посмотреть сколько заказов отражается на счетчике "Выполненно за все время"
        assert int(new_counter) > int(old_counter)

    @allure.title('При создании нового заказа,номер заказа появляется в разделе "В работе"')
    def test_take_order_to_work(self, driver):
        order_to_work = MainPage(driver)  # Открытие стартовой странице сервиса
        order_to_work.click_button_personal_account() # Клик на кнопку "Личный кабинет"
        order_to_work = LoginPage(driver)
        order_to_work.authorization_under_current_user()  # Авторизация под действующим пользователемtton()
        order_to_work = MainPage(driver)
        order_to_work.add_bun()  # Добавление булки для заказа бургера
        order_to_work.click_button_create_order()  # Клик на кнопку "Оформить заказ"
        order_id = order_to_work.get_order_id()  # Запомнить номер заказа, отраженный в окне с подтверждением оформления
        order_to_work.closing_window_create_order() # Закрыть окно, подтверждащее оформление заказа
        order_to_work.wait_closing_window_create_order()  # Подождать закрытия окна, подтверждащего оформление заказа
        order_to_work.click_button_order_feed()  # Клик на кнопку "Лента заказов"
        order_in_progress = order_to_work.get_order_numbers_in_progress() # Запомнить номер заказа, отраженный в окне с подтверждением оформления
        assert order_id in order_in_progress

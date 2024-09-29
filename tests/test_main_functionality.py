import allure

from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainFunctionality:
    @allure.title('Переход по клику на «Конструктор»')
    def test_convertion_form_constructor(self, driver):
        password_recovery = MainPage(driver)
        password_recovery.click_button_personal_account()  # Клик на кнопку "Личный кабинет"
        password_recovery.click_button_constructor()  # Клик на кнопку "Конструктор"

        assert password_recovery.form_constructor_visible() # Отражение формы "Конструктор"

    @allure.title('Переход по клику на «Лента заказов»')
    def test_convertion_order_feed(self, driver):
        convertion_order_feed = MainPage(driver)
        convertion_order_feed.click_button_order_feed() # Клик на кнопку "Лента заказов"
        convertion_order_feed = FeedPage(driver)

        assert convertion_order_feed.visible_order_feed() # Отражение формы "Лента заказов"

    @allure.title('Открытие/закрытие окна с деталями ингредиента')
    def test_opening_closing_window_with_ingredient_details(self, driver):
        ingredient_details= MainPage(driver)
        ingredient_details.click_ingredient_icon()
        ingredient_details.closing_window_with_ingredient_details()

        assert ingredient_details.really_closing_window()

    @allure.title('При добавлении ингредиента в заказ - счётчик этого ингридиента увеличивается')
    def test_number_ingredients_rising(self, driver):
        number_ingredients= MainPage(driver)
        number_ingredients.add_bun()

        assert number_ingredients.get_count_of_ingredients() == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_create_order_by_authorized_user(self, driver):
        create_order= MainPage(driver)
        create_order.click_button_personal_account()  # Клик на кнопку "Личный кабинет"
        create_order = LoginPage(driver)
        create_order.authorization_under_current_user()  # Авторизация под действующим пользователем
        create_order = MainPage(driver)
        create_order.click_button_constructor() # Клик на кнопку "Конструктор"
        create_order.add_bun() # Добавление булки для заказа бургера
        create_order.click_button_create_order() # Клик на кнопку "Оформить заказ"

        assert create_order.open_window_with_id_order() # Проверка отражения окна с идентификатором заказа
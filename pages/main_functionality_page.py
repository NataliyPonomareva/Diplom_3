import allure

from data import User
from locators.main_functionality_locators import MainFunctionalityLocators
from pages.base_page import BasePage


class MainFunctionalityPage(BasePage):
    @allure.step('Загрузка драйвера')
    def __init__(self, driver):
        super().__init__(driver)  # Вызов конструктора родительского класса

    @allure.step('Клик на кнопку "Личный кабинет"')
    def click_button_personal_account(self):
        self.click_by_element(MainFunctionalityLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик на кнопку "Конструктор"')
    def click_button_constructor(self):
        self.click_by_element(MainFunctionalityLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Отражение формы "Конструктор"')
    def form_constructor_visible(self):
        return self.is_displayed(MainFunctionalityLocators.FORM_CONSTRUCTOR)

    @allure.step('Клик на кнопку "Лента заказов"')
    def click_button_order_feed(self):
        self.click_by_remote_element(MainFunctionalityLocators.BUTTON_ORDER_FEED)

    @allure.step('Отражение формы "Лента заказов"')
    def visible_order_feed(self):
        self.wait_and_find_element(MainFunctionalityLocators.FORM_ORDER_FEED)
        return self.is_displayed(MainFunctionalityLocators.FORM_ORDER_FEED)

    @allure.step('Клик на название "Флюоресцентная булка R2-D3"')
    def click_ingredient_icon(self):
        self.click_by_remote_element(MainFunctionalityLocators.INGREDIENT_ICON)

    @allure.step('Закрыть окно с деталями ингредиента')
    def closing_window_with_ingredient_details(self):
        self.click_by_element(MainFunctionalityLocators.CLOSING_WINDOW_INGREDIENT_DETAILS)

    @allure.step('Проверка закрытия окна с деталями ингредиента')
    def really_closing_window(self):
        self.wait_closing_element(MainFunctionalityLocators.WINDOW_WITH_INGREDIENT_DETAILS)
        if not self.is_displayed(MainFunctionalityLocators.WINDOW_WITH_INGREDIENT_DETAILS):
            return True

    @allure.step('Добавление булки для заказа бургера')
    def add_bun(self):
        bun = self.wait_and_find_element(MainFunctionalityLocators.INGREDIENT_ICON)
        burger_constructor = self.wait_and_find_element(MainFunctionalityLocators.BURGER_CONSTRUCTOR)
        self.drag_element(bun, burger_constructor)

    @allure.step('Получить число ингредиентов')
    def get_count_of_ingredients(self):
        return self.get_text_from_element(MainFunctionalityLocators.NUMBER_INGREDIENTS)

    @allure.step('Авторизация под действующим пользователем')
    def authorization_under_current_user(self):
        self.send_keys(MainFunctionalityLocators.EMAIL, val=User.EMAIL)
        self.send_keys(MainFunctionalityLocators.PASSWORD, val=User.PASSWORD)
        self.click_by_element(MainFunctionalityLocators.BUTTON_ENTER)

    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_button_create_order(self):
        self.click_by_remote_element(MainFunctionalityLocators.BUTTON_CREATE_ORDER)

    @allure.step('Появилось окно с идентификатором заказа')
    def open_window_with_id_order(self):
        self.wait_and_find_element(MainFunctionalityLocators.WINDOW_WITH_ID_ORDER)
        return self.is_displayed(MainFunctionalityLocators.WINDOW_WITH_ID_ORDER)
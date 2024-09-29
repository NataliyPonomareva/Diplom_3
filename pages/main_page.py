import allure

from data import Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Загрузка драйвера')
    def __init__(self, driver):
        super().__init__(driver)  # Вызов конструктора родительского класса

    @allure.step('Клик на кнопку "Личный кабинет"')
    def click_button_personal_account(self):
        self.click_by_element(locator=MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Нажатие кнопки "Личный кабинет" после оформления заказа')
    def click_account_button(self):
        self.wait_and_find_element(locator=MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_by_element(locator=MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_new_url(data=Urls.BASE_URL + Urls.PROFILE_URL)

    @allure.step('Клик на кнопку "Лента заказов"')
    def click_button_order_feed(self):
        self.wait_and_find_element(MainPageLocators.BUTTON_ORDER_FEED)
        self.move_to_element_and_click(MainPageLocators.BUTTON_ORDER_FEED)
        self.wait_and_find_element(MainPageLocators.TITLE_ORDER_FEED)

    @allure.step('Клик на кнопку "Конструктор"')
    def click_button_constructor(self):
        self.click_by_element(locator=MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Отражение формы "Конструктор"')
    def form_constructor_visible(self):
        return self.is_displayed(MainPageLocators.FORM_CONSTRUCTOR)

    @allure.step('Добавление булки для заказа бургера')
    def add_bun(self):
        bun = self.wait_and_find_element(locator=MainPageLocators.INGREDIENT_ICON)
        burger_constructor = self.wait_and_find_element(locator=MainPageLocators.BURGER_CONSTRUCTOR)
        self.drag_and_drop_element(element_to_drag=bun, target_location=burger_constructor)

    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_button_create_order(self):
        self.click_by_remote_element(locator=MainPageLocators.BUTTON_CREATE_ORDER)

    @allure.step('Появилось окно с идентификатором заказа')
    def open_window_with_id_order(self):
        self.wait_and_find_element(MainPageLocators.WINDOW_WITH_ID_ORDER)
        return self.is_displayed(MainPageLocators.WINDOW_WITH_ID_ORDER)

    @allure.step('Закрыть окно, подтверждащее оформление заказа')
    def closing_window_create_order(self):
        self.wait_and_find_element(locator=MainPageLocators.CLOSE_WINDOW_CREATE_ORDER)
        self.click_by_element(locator=MainPageLocators.CLOSE_WINDOW_CREATE_ORDER)

    @allure.step('Подождать закрытия окна, подтверждащего оформление заказа')
    def wait_closing_window_create_order(self):
        self.wait_closing_element(locator=MainPageLocators.CLOSE_WINDOW_CREATE_ORDER)

    @allure.step('Дождаться загрузки конструктора')
    def wait_and_find_form_constructor(self):
        self.wait_and_find_element(MainPageLocators.FORM_CONSTRUCTOR)

    @allure.step('Запомнить номер заказа, отраженный в окне с подтверждением оформления ')
    def get_order_id(self):
        self.wait_and_find_element(locator=MainPageLocators.ORDER_IDENTIFICATOR)
        order_id = self.get_text_on_element(locator=MainPageLocators.ORDER_ID)
        while order_id == '9999':
            order_id = self.get_text_on_element(locator=MainPageLocators.ORDER_ID)
        return f"{order_id}"

    @allure.step('Клик на название "Флюоресцентная булка R2-D3"')
    def click_ingredient_icon(self):
        self.click_by_remote_element(MainPageLocators.INGREDIENT_ICON)

    @allure.step('Закрыть окно с деталями ингредиента')
    def closing_window_with_ingredient_details(self):
        self.click_by_element(MainPageLocators.CLOSING_WINDOW_INGREDIENT_DETAILS)

    @allure.step('Проверка закрытия окна с деталями ингредиента')
    def really_closing_window(self):
        self.wait_closing_element(MainPageLocators.WINDOW_WITH_INGREDIENT_DETAILS)
        if not self.is_displayed(MainPageLocators.WINDOW_WITH_INGREDIENT_DETAILS):
            return True

    @allure.step('Получить число ингредиентов')
    def get_count_of_ingredients(self):
        return self.get_text_from_element(MainPageLocators.NUMBER_INGREDIENTS)

    @allure.step('Созданный заказ находится в разделе "В работе"')
    def get_order_numbers_in_progress(self):
        elements = self.wait_and_find_element(MainPageLocators.ORDER_IN_PROGRESS)
        return elements

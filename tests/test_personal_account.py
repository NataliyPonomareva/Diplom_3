import allure

from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:
    @allure.title('Тестирование входа в Личный кабинет, перехода на вкладку "История заказов" и выход из аккаунта"')
    def test_personal_account(self, driver):
        personal_account = PersonalAccountPage(driver)
        personal_account.click_button_personal_account()  # Клик на кнопку "Личный кабинет"
        personal_account.authorization_under_current_user() # Авторизация под действующим пользователем
        personal_account.wait_and_find_form_constructor() # Дождаться загрузки конструктора
        personal_account.click_button_personal_account()  # Клик на кнопку "Личный кабинет"
        personal_account.click_order_history() # Клик на поле "История заказов"
        personal_account.wait_and_find_order_history() # Дожидаемся загрузки списка заказов
        personal_account.click_button_exit() # Клик на кнопку "Выход"

        assert personal_account.form_authorization_visible() # отражается форма авторизации
import allure

from pages.password_recovery_page import PasswordRecoveryPage



class TestRecoveryPassword:
    @allure.title('Восстановление пароля')
    def test_password_recovery(self, driver): #
        password_recovery = PasswordRecoveryPage(driver)
        password_recovery.click_button_personal_account()  # Клик на кнопку "Личный кабинет"
        password_recovery.click_link() # Клик на ссылку «Восстановить пароль»
        password_recovery.click_button_recovery() # Клик на кнопку "Восстановить"
        password_recovery.input_email() # Ввод пароля в окне "Восстановление пароля"
        password_recovery.click_button_show_hide_password() # клик по кнопке показать/скрыть пароль

        assert password_recovery.password_visible() # введенное значение "пароля" становится видимым

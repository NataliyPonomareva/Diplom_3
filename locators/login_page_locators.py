from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL = (By.XPATH, "//input[(@class = 'text input__textfield text_type_main-default') and (@type = 'text')]")  # поле "Email"
    PASSWORD = (By.XPATH,"//input[(@class = 'text input__textfield text_type_main-default') and (@type = 'password')]")  # поле "Пароль"
    BUTTON_ENTER = (By.XPATH, "//button[text() = 'Войти']")  # кнопка 'Войти'
    LINK_RECOVER_PASSWORD = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # ссылка "Восстановить пароль"

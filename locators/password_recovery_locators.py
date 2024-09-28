from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # кнопка "Личный кабинет"
    LINK_RECOVER_PASSWORD = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # ссылка "Восстановить пароль"
    EMAIL = (By.XPATH, '//label[text() = "Email"]/following-sibling::input') # поле "Email" в окне "Восстановления пароля"
    BUTTON_RECOVERY = (By.XPATH, "//button[text() = 'Восстановить']")  # кнопка "Восстановить"
    PASSWORD  = (By.XPATH, '//label[text() = "Пароль"]/following-sibling::input')  # поле "Пароль" в окне "Восстановления пароля
    BUTTON_PASSWORD_SHOW = (By.XPATH,
                            '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')  # кнопка "показать/скрыть пароль"
    PASSWORD_SHOW = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, ''"input_status_active")]') # пароль становится видимым в поле "Пароль"

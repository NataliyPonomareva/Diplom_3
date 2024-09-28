from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # кнопка "Личный кабинет"
    EMAIL = (By.XPATH, "//input[(@class = 'text input__textfield text_type_main-default') and (@type = 'text')]") # поле "Email"
    PASSWORD = (By.XPATH, "//input[(@class = 'text input__textfield text_type_main-default') and (@type = 'password')]") # поле "Пароль"
    BUTTON_ENTER = (By.XPATH, "//button[text() = 'Войти']") # кнопка 'Войти'
    FORM_CONSTRUCTOR = (By.XPATH, "//h1[text() = 'Соберите бургер']")  # форма Конструктор
    ORDER_HISTORY = (By.XPATH, "//a[(@class = 'Account_link__2ETsJ text text_type_main-medium text_color_inactive') and text()='История заказов']") # поле "История заказов"
    LIST_ORDER_HISTORY = (By.XPATH, '//div[contains(@class, "Account_contentBox")]') # список "История заказов"
    BUTTON_EXIT = (By.XPATH, "//button[text() = 'Выход']")
    FORM_AUTHORIZATION = (By.XPATH, "//h2[text() = 'Вход']")  # форма авторизации
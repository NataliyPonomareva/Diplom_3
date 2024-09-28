from selenium.webdriver.common.by import By

class MainFunctionalityLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # кнопка "Личный кабинет"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text() = 'Конструктор']") # кнопка 'Конструктор'
    FORM_CONSTRUCTOR = (By.XPATH, "//h1[text() = 'Соберите бургер']")  # форма 'Конструктор'
    BUTTON_ORDER_FEED = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li') # кнопка 'Лента заказов'
    FORM_ORDER_FEED = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')  # форма 'Лента заказов'

    INGREDIENT_ICON = (By.XPATH, './/*[@alt="Краторная булка N-200i"]') # 'Краторная булка N-200i'

    CLOSING_WINDOW_INGREDIENT_DETAILS = (By.XPATH, '//section[contains(@class, ''"Modal_modal_opened")]//button[contains(@class, "close")]') # знак "Х" в окне с деталями ингредиента
    WINDOW_WITH_INGREDIENT_DETAILS = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]') # Окно с деталями выбранного ингредиента
    NUMBER_INGREDIENTS = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p['
                                    '@class="counter_counter__num__3nue1"][1]')  # Счетчик у ингредиента

    BURGER_CONSTRUCTOR = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]') # Макет бургера, для индивидуального заказа

    EMAIL = (By.XPATH, "//input[(@class = 'text input__textfield text_type_main-default') and (@type = 'text')]") # поле "Email"
    PASSWORD = (By.XPATH, "//input[(@class = 'text input__textfield text_type_main-default') and (@type = 'password')]") # поле "Пароль"
    BUTTON_ENTER = (By.XPATH, "//button[text() = 'Войти']") # кнопка 'Войти'

    BUTTON_CREATE_ORDER= (By.XPATH, "//button[text() = 'Оформить заказ']")  # кнопка 'Оформить заказ'

    WINDOW_WITH_ID_ORDER = (By.XPATH, '//p[text() = "идентификатор заказа"]') # окно с идентификатором заказа
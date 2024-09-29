from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # кнопка "Личный кабинет"
    BUTTON_ORDER_FEED = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')  # кнопка 'Лента заказов'
    TITLE_ORDER_FEED = (By.XPATH, "//h1[text()='Лента заказов']")  # Заголовок раздела Лента заказов
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text() = 'Конструктор']")  # кнопка 'Конструктор'
    FORM_CONSTRUCTOR = (By.XPATH, "//h1[text() = 'Соберите бургер']")  # форма 'Конструктор'

    INGREDIENT_ICON = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")  # Булка
    BURGER_CONSTRUCTOR = (By.XPATH, ".//ul[@class='BurgerConstructor_basket__list__l9dp_']")  # Макет бургера, для индивидуального заказа

    BUTTON_CREATE_ORDER = (By.XPATH, "//button[text() = 'Оформить заказ']")  # кнопка 'Оформить заказ'
    WINDOW_WITH_ID_ORDER = (By.XPATH, '//p[text() = "идентификатор заказа"]')  # окно с идентификатором заказа

    CLOSE_WINDOW_CREATE_ORDER = (By.XPATH,
                                 ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")  # знак Х для закрытия окна с подтверждением сформированного заказа

    ORDER_IDENTIFICATOR = (By.XPATH, '//p[text()="идентификатор заказа"]')  # заголовок "Идентификатор заказа"
    ORDER_ID = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")  # "Номер заказа" в окне в подтверждением оформления

    INGREDIENT_ICON = (By.XPATH, './/*[@alt="Краторная булка N-200i"]')  # 'Краторная булка N-200i'

    CLOSING_WINDOW_INGREDIENT_DETAILS = (By.XPATH,
                                         '//section[contains(@class, ''"Modal_modal_opened")]//button[contains(@class, "close")]')  # знак "Х" в окне с деталями ингредиента

    WINDOW_WITH_INGREDIENT_DETAILS = (By.XPATH,
                                      '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]')  # Окно с деталями выбранного ингредиента

    NUMBER_INGREDIENTS = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p['
                                    '@class="counter_counter__num__3nue1"][1]')  # Счетчик у ингредиента

    ORDER_IN_PROGRESS = (By.CSS_SELECTOR, '.OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi li')
from selenium.webdriver.common.by import By

from data import User


class OrderFeedLocators:
    BUTTON_ORDER_FEED = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')  # кнопка 'Лента заказов'
    TITLE_ORDER_FEED = (By.XPATH, "//h1[text()='Лента заказов']") # Заголовок раздела Лента заказов
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//a[@href='/account']") # кнопка "Личный кабинет"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text() = 'Конструктор']")  # кнопка 'Конструктор'
    CARD_ORDER = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]') # карточка заказа
    WINDOW_WITH_DETAILS_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains'
                                 '(@class, "Modal_orderBox")]') # Окно "Детали заказа"

    EMAIL = (By.XPATH, "//input[(@class = 'text input__textfield text_type_main-default') and (@type = 'text')]") # поле "Email"
    PASSWORD = (By.XPATH, "//input[(@class = 'text input__textfield text_type_main-default') and (@type = 'password')]") # поле "Пароль"
    BUTTON_ENTER = (By.XPATH, "//button[text() = 'Войти']") # кнопка 'Войти'

    INGREDIENT_ICON = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")  # Булка
    BURGER_CONSTRUCTOR = (By.XPATH, ".//ul[@class='BurgerConstructor_basket__list__l9dp_']") # Макет бургера, для индивидуального заказа

    #BURGER_CONSTRUCTOR = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')  # Макет бургера, для индивидуального заказа
    BUTTON_CREATE_ORDER = (By.XPATH, "//button[text() = 'Оформить заказ']")  # кнопка 'Оформить заказ'


    ORDER_IDENTIFICATOR = (By.XPATH, '//p[text()="идентификатор заказа"]') # заголовок "Идентификатор заказа"
    ORDER_ID = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq") # "Номер заказа" в окне в подтверждением оформления

    CLOSE_WINDOW_CREATE_ORDER = (By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']") # знак Х для закрытия окна с подтверждением сформированного заказа
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")   # поле "История заказов"
    ALL_ORDERS_USERS_IN_HISTORY = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, "
                                       "'text_type_digits-default')]") # id заказа пользователя в разделе 'История заказов'
    ALL_ORDERS_USERS_IN_FEED = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text "
                                    "text_type_digits-default']")   # все заказы пользователя в разделе 'Лента заказов'

    NUMBER_ORDER_USERS = (By.XPATH, './/*[text()="{order_id}"]')
    ID_NUMBER_ORDER_USERS = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]''/p[contains(@class, "text_type_digits-default")])[1]') # Id заказа
    FIRST_ORDER_IN_FEED = (By.XPATH, "//a[contains(@class,'OrderHistory_link')]")

    MODAL_CLOSE_BUTTON = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS")

    COUNTER_COMPLETED_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[1]") # счетчик 'Выполнено за сегодня'
    COUNTER_COMPLETED_FOR_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[1]") # счетчик 'Выполненно за все время'
    ORDER_IN_PROGRESS = (By.CSS_SELECTOR, '.OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi li')
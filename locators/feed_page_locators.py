from selenium.webdriver.common.by import By

class FeedPageLocators:
    FORM_ORDER_FEED = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')  # форма 'Лента заказов'
    CARD_ORDER = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')  # карточка заказа

    WINDOW_WITH_DETAILS_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains'
                                 '(@class, "Modal_orderBox")]') # Окно "Детали заказа"

    ALL_ORDERS_USERS_IN_FEED = (By.XPATH, "//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text "
                                    "text_type_digits-default']")   # все заказы пользователя в разделе 'Лента заказов'

    COUNTER_COMPLETED_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[1]")  # счетчик 'Выполнено за сегодня'
    COUNTER_COMPLETED_FOR_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[1]")  # счетчик 'Выполненно за все время'
    ORDER_IN_PROGRESS = (By.CSS_SELECTOR, 'OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi li')
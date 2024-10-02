from selenium.webdriver.common.by import By

class OrderHistoryPageLocators:
    ALL_ORDERS_USERS_IN_HISTORY = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, "
                                       "'text_type_digits-default')]") # id заказа пользователя в разделе 'История заказов'

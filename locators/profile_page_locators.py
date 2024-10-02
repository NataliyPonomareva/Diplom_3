from selenium.webdriver.common.by import By

class ProfilePageLocators:
    ORDER_HISTORY = (By.XPATH,"//a[contains(@class,'Account_link') and text()='История заказов']")  # поле "История заказов"
    LIST_ORDER_HISTORY = (By.XPATH, "//div[contains(@class, 'OrderHistory_orderHistory')]")  # список "История заказов"
    BUTTON_EXIT = (By.XPATH, "//button[@type='button' and text()='Выход']") # кнопка "Выход"
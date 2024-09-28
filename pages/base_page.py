import allure
from selenium.common import NoSuchElementException

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains



class BasePage:
    @allure.step('Загрузка драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Загружаем страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Поиск элементов на странице')
    def find_elements(self, locator, wait_time=10):
        return WebDriverWait(self.driver, wait_time).until(expected_conditions.presence_of_all_elements_located(locator))

    @allure.step('Дождаться видимости элемента')
    def wait_until_element_visibility(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Получить текст на элементе')
    def get_text_on_element(self, locator):
        self.wait_until_element_visibility(locator)
        return self.driver.find_element(*locator).text

    @allure.step('Поиск элемента на странице и ожидание загрузки')
    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 50).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик на элемент')
    def click_by_element(self, locator): # Найти элемент и кликнуть по нему
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Переместиться до элемента и кликнуть')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step('Клик на отдаленный элемент')
    def click_by_remote_element(self, locator):
        element = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
        ActionChains(self.driver).move_to_element(element).click().perform()

    @allure.step('Заполнение поля')
    def send_keys(self, locator, val=None) -> WebElement:
        self.wait_and_find_element(locator).send_keys(val)

    @allure.step('Проверка отражения элемента на странице')
    def is_displayed(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    @allure.step('Подождать закрытия элемента')
    def wait_closing_element(self, locator):
        WebDriverWait(self.driver, 100).until_not(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, element_to_drag, target_location):
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element_to_drag, target_location).perform()

    @allure.step('Получить текст элемента')
    def get_text_from_element(self, locator):
        self.is_displayed(locator)
        self.wait_and_find_element(locator)
        return self.wait_and_find_element(locator).text

    @allure.step('Скролл страницы до нужного элемента')
    def scroll_and_find_element(self, locator) -> WebElement: # Скролл страницы до элемента и клик по нему
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Ожидание перехода на новый Url")
    def wait_new_url(self, url):
        WebDriverWait(self.driver, 15).until(expected_conditions.url_to_be(url))

    @allure.step("Нахождение нескольких элементов")
    def find_until_all_elements_located(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_all_elements_located(locator))

import allure
import pytest
from selenium import webdriver

from data import Urls


@allure.step("Запуск браузера. Переход на главную страницу Stellar Burgers. После выполнения тесте - закрыть браузер.")
@pytest.fixture(params=['firefox', 'chrome'], scope='function')
def driver(request):
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome()

    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()
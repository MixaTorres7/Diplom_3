import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from utils.wait import wait_until


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем ссылку')
    def open_link(self, url):
        return self.driver.get(url)

    @allure.step('Кликаем по элементу {locator}')
    def click_on_element(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    @allure.step('Получить текущий текст')
    def get_element_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    @allure.step('Проверить невидимость элемента')
    def check_invisibility(self, locator):
        result = wait_until(self.driver, 10, EC.invisibility_of_element_located(locator))
        return result

    @allure.step('Дождаться видимости элемента')
    def wait_until_element_visibility(self, locator):
        element = wait_until(self.driver, 10, EC.visibility_of_element_located(locator))
        return element

    @allure.step('Получить текущую ссылку')
    def get_current_url(self):
        url = self.driver.current_url
        return url

    @allure.step('Перетащить элемент')
    def drag_and_drop_on_element(self, locator_one, locator_two):
        element_from = wait_until(self.driver, 10, EC.presence_of_element_located(locator_one))
        element_to = wait_until(self.driver, 10, EC.presence_of_element_located(locator_two))
        ActionChains(self.driver).drag_and_drop(element_from, element_to).perform()

    @allure.step('Переместиться до элемента и кликнуть')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step('Дождаться кликабельности элемента')
    def wait_for_element_to_be_clickable(self, locator):
        wait_until(self.driver, 10, EC.element_to_be_clickable(locator))

    @allure.step('Дождаться появления текста в элементе')
    def wait_for_text_to_be_present_in_element(self, locator, text):
        wait_until(self.driver, 10, EC.text_to_be_present_in_element(locator, text))

import time

import allure
from selenium.webdriver.support import expected_conditions as EC

from data.urls import Urls
from utils.wait import wait_until
from web_pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Переход на страницу Лента заказов')
    def click_orders_list_button(self):
        self.driver.get(Urls.url_feed)
        wait_until(self.driver, 15, EC.url_contains('/feed'))

    @allure.step('Переход в "Конструктор"')
    def click_constructor_button(self):
        self.click_on_element(self.locators.CONSTRUCTOR_BUTTON)
        self.wait_until_element_visibility(self.locators.MAIN_LIST_TITLE)

    @allure.step('Кликаем на ингредиент')
    def click_on_ingredient(self):
        self.wait_for_element_to_be_clickable(self.locators.BUN_INGREDIENT)
        self.click_on_element(self.locators.BUN_INGREDIENT)

    @allure.step('Проверяем, что появилось всплывающее окно с деталями ингредиента')
    def check_show_window_with_details(self):
        self.wait_until_element_visibility(self.locators.INGREDIENT_DETAILS_POPUP)
        return self.get_element_text(self.locators.INGREDIENT_DETAILS_POPUP)

    @allure.step('Закрываем попап крестиком')
    def click_cross_button(self):
        self.wait_for_element_to_be_clickable(self.locators.CROSS_BUTTON)
        self.move_to_element_and_click(self.locators.CROSS_BUTTON)

    @allure.step('Проверить скрытость деталей ингредиентов')
    def invisibility_ingredient_details(self):
        self.check_invisibility(self.locators.INGREDIENT_DETAILS_POPUP)

    @allure.step('Получаем значение счетчика ингредиента')
    def get_count_value(self):
        counters = self.driver.find_elements(*self.locators.INGREDIENT_COUNTER)
        if counters:
            value = counters[0].text
        else:
            value = '0'
        if value == '':
            value = '0'
        return int(value)

    def drag_until_order_ready(self):
        for _ in range(3):
            self.drag_and_drop_on_element(self.locators.BUN_INGREDIENT, self.locators.ORDER_BASKET)
            time.sleep(1)
            try:
                wait_until(self.driver, 5, EC.element_to_be_clickable(self.locators.CREATE_ORDER_BUTTON))
                return
            except Exception:
                pass

    @allure.step('Добавить ингредиент в заказ')
    def add_filling_to_order(self):
        self.wait_until_element_visibility(self.locators.MAIN_LIST_TITLE)
        self.wait_until_element_visibility(self.locators.ORDER_BASKET)
        self.wait_for_element_to_be_clickable(self.locators.BUN_INGREDIENT)
        self.drag_until_order_ready()
        wait_until(self.driver, 15, EC.element_to_be_clickable(self.locators.CREATE_ORDER_BUTTON))

    @allure.step('Нажать на кнопку Оформить заказ')
    def click_order_button(self):
        wait_until(self.driver, 15, EC.element_to_be_clickable(self.locators.CREATE_ORDER_BUTTON))
        self.move_to_element_and_click(self.locators.CREATE_ORDER_BUTTON)

    @allure.step('Проверяем, что заказ оформлен')
    def check_show_window_with_order_id(self):
        self.wait_until_element_visibility(self.locators.ORDER_IDENTIFICATE)
        return self.get_element_text(self.locators.ORDER_IDENTIFICATE)

    def order_id_ready(self, driver):
        text = driver.find_element(*self.locators.ORDER_ID).text
        return text if text != '9999' else False

    @allure.step('Получение ORDER_ID')
    def get_with_order_id(self):
        self.wait_until_element_visibility(self.locators.ORDER_IDENTIFICATE)
        return wait_until(self.driver, 15, self.order_id_ready)

    @allure.step('Закрыть модальное окно после создания заказа')
    def click_close_modal_order(self):
        time.sleep(5)
        wait_until(self.driver, 10, EC.element_to_be_clickable(self.locators.CLOSE_MODAL_ORDER))
        self.move_to_element_and_click(self.locators.CLOSE_MODAL_ORDER)

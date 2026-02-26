import allure

from web_pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step('Получение количества заказов')
    def get_total_order_count_daily(self, locator):
        self.wait_until_element_visibility(locator)
        return self.get_element_text(locator)

    @allure.step('Получаем номер заказа')
    def get_user_order(self, orders_numbers):
        order_refactor = f'0{orders_numbers}'
        self.wait_for_text_to_be_present_in_element(self.locators.NUMBER_IN_PROGRESS, orders_numbers)
        return order_refactor

    @allure.step('Получаем номер заказа в работе')
    def get_user_order_in_progress(self):
        return self.get_element_text(self.locators.NUMBER_IN_PROGRESS_FIRST)

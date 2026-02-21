import allure

from web_locators.locators import OrdersPageLocators


class TestOrderFeed:
    @allure.title('Счётчик «Выполнено за всё время» увеличивается при создании заказа')
    def test_total_counter_increases(self, pages, login):
        pages.click_orders_list_button()
        prev = pages.get_total_order_count_daily(OrdersPageLocators.TOTAL_ORDER_COUNT)
        pages.click_constructor_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_modal_order()
        pages.click_orders_list_button()
        curr = pages.get_total_order_count_daily(OrdersPageLocators.TOTAL_ORDER_COUNT)
        assert int(curr) > int(prev)

    @allure.title('Счётчик «Выполнено за сегодня» увеличивается при создании заказа')
    def test_daily_counter_increases(self, pages, login):
        pages.click_orders_list_button()
        prev = pages.get_total_order_count_daily(OrdersPageLocators.DAILY_ORDER_COUNT)
        pages.click_constructor_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_modal_order()
        pages.click_orders_list_button()
        curr = pages.get_total_order_count_daily(OrdersPageLocators.DAILY_ORDER_COUNT)
        assert int(curr) > int(prev)

    @allure.title('Номер заказа появляется в разделе «В работе»')
    def test_order_in_progress_section(self, pages, login):
        pages.click_constructor_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        order_number = pages.get_with_order_id()
        pages.click_close_modal_order()
        pages.click_orders_list_button()
        order_refactor = pages.get_user_order(order_number)
        order_in_progress = pages.get_user_order_in_progress()
        assert order_refactor == order_in_progress

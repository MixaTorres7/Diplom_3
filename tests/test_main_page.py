import allure

from data.urls import Urls


class TestMainPage:
    @allure.title('Переход по клику на «Лента заказов»')
    def test_click_order_feed(self, pages):
        pages.click_orders_list_button()
        assert pages.get_current_url() == Urls.url_feed

    @allure.title('Переход по клику на «Конструктор»')
    def test_click_constructor(self, pages):
        pages.click_orders_list_button()
        pages.click_constructor_button()
        assert pages.get_current_url() == Urls.url_main

    @allure.title('Клик на ингредиент — появляется попап с деталями')
    def test_ingredient_popup(self, pages):
        pages.click_on_ingredient()
        text = pages.check_show_window_with_details()
        assert text == "Детали ингредиента"

    @allure.title('Попап закрывается кликом по крестику')
    def test_close_popup_by_cross(self, pages):
        pages.click_on_ingredient()
        pages.click_cross_button()
        pages.invisibility_ingredient_details()

    @allure.title('При добавлении ингредиента счётчик увеличивается')
    def test_ingredient_counter_increases(self, pages, login):
        prev = pages.get_count_value()
        pages.add_filling_to_order()
        assert pages.get_count_value() > prev

from web_pages.auth_user_page import AuthUserPage
from web_pages.base_page import BasePage
from web_pages.main_page import MainPage
from web_pages.order_feed_page import OrderFeedPage


class UIWorkerWeb(MainPage, AuthUserPage, OrderFeedPage):
    def __init__(self, driver, locators):
        super().__init__(driver)
        self.locators = locators

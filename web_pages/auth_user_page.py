import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from data.urls import Urls
from utils.wait import wait_until
from web_pages.base_page import BasePage


class AuthUserPage(BasePage):
    @allure.step('Заполняем поле "email"')
    def set_email_field(self, user_email):
        el = wait_until(self.driver, 10, EC.visibility_of_element_located(self.locators.EMAIL_FIELD))
        el.clear()
        el.send_keys(user_email)

    @allure.step('Заполняем поле "Пароль"')
    def set_password_field(self, user_password):
        el = wait_until(self.driver, 10, EC.visibility_of_element_located(self.locators.PASSWORD_FIELD))
        el.clear()
        el.send_keys(user_password)

    @allure.step('Нажимаем кнопку «Войти»')
    def click_login_button(self):
        btn = wait_until(self.driver, 10, EC.element_to_be_clickable(self.locators.LOGIN_BUTTON))
        ActionChains(self.driver).move_to_element(btn).click().perform()
        wait_until(self.driver, 15, self.redirected_from_login)
        wait_until(self.driver, 10, EC.element_to_be_clickable(self.locators.PROFILE_BUTTON))

    def redirected_from_login(self, driver):
        return '/login' not in driver.current_url

    @allure.step('Авторизация')
    def login(self, email, password):
        self.driver.get(Urls.url_login)
        self.set_email_field(email)
        self.set_password_field(password)
        self.click_login_button()

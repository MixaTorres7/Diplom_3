import allure
import pytest
from selenium import webdriver

from api.auth_api import register_user, get_token, delete_user
from data.urls import Urls
from data.user_data import get_user_for_register
from web_locators import UIWorkerLocators
from web_pages import UIWorkerWeb


@allure.step('Открытие браузера')
@pytest.fixture
def driver_do():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.get(Urls.url_main)

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def pages(driver_do):
    return UIWorkerWeb(driver_do, UIWorkerLocators())


@pytest.fixture(scope='function')
def user_data(request):
    data = get_user_for_register()
    register_user(data['name'], data['email'], data['password'])

    def cleanup():
        token = get_token(data['email'], data['password'])
        delete_user(token)

    request.addfinalizer(cleanup)
    return data


@pytest.fixture(scope='function')
def login(pages, user_data):
    pages.login(user_data['email'], user_data['password'])

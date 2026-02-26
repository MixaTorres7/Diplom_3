import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_until(driver, timeout, condition):
    return WebDriverWait(driver, timeout).until(condition)

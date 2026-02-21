from selenium.webdriver.common.by import By


class MainPageLocators:
    PROFILE_BUTTON = (By.XPATH, ".//p[contains(text(),'Личный')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]/parent::a')
    MAIN_LIST_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    BUN_INGREDIENT = (By.XPATH, "//img[contains(@alt,'булка')]/ancestor::a")
    INGREDIENT_DETAILS_POPUP = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    CROSS_BUTTON = (By.XPATH, '//button[contains(@class,"close")]')
    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class,"num") or contains(@class,"digits")]')
    ORDER_BASKET = (By.CSS_SELECTOR, "div.constructor-element_pos_top")
    CREATE_ORDER_BUTTON = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')
    ORDER_IDENTIFICATE = (By.XPATH, '//p[text()="идентификатор заказа"]')
    ORDER_ID = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
    CLOSE_MODAL_ORDER = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]")


class AuthLoginLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@type='text']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[class*='button_button_type_primary']")


class OrdersPageLocators:
    TOTAL_ORDER_COUNT = (By.XPATH, "//p[contains(text(),'Выполнено за все')]/following-sibling::p")
    DAILY_ORDER_COUNT = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p")
    NUMBER_IN_PROGRESS = (By.XPATH, "//p[contains(text(),'В работе')]/following-sibling::ul")
    NUMBER_IN_PROGRESS_FIRST = (By.XPATH, "//p[contains(text(),'В работе')]/following-sibling::ul/li[1]")

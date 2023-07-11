from selenium.webdriver.common.by import By

class Locators:
    # Главная страница
    INTO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    LK_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
    PUSH_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ"
    SOUCE_BUTTON = (By.XPATH, ".//span[text()='Соусы']")  # Кнопка "Соусы"
    STUFFING_BUTTON = (By.XPATH, ".//span[text()='Начинки']")  # Кнопка "Начинки"
    AREA_BAKERY = (By.XPATH, ".//div[contains(@class,'current')]/span[text()='Булки']")  # Раздел с булками
    AREA_SOUCE = (By.XPATH, ".//div[contains(@class,'current')]/span[text()='Соусы']")  # Раздел с соусами
    AREA_STUFFING = (By.XPATH, ".//div[contains(@class,'current')]/span[text()='Начинки']")  # Раздел с начинками
    # Страница с формой авторизации /login
    EMAIL = (By.XPATH, ".//input[contains(@type,'text')]")  # Поле "Почта"
    PASSWORD = (By.XPATH, ".//input[contains(@type,'password')]")  # Поле "Пароль"
    ENTER_BUTTON_A = (By.XPATH, ".//button[text()='Войти']")  # Кнопка "Войти"
    FORM_ENTER = (By.XPATH, ".//h2[text()='Вход']")  # Надпись "Вход"
    # Страница с формой регистрации /register
    REG_NAME = (By.XPATH, "//label[text() = 'Имя']/parent::div/input")  # Поле "Имя"
    REG_EMAIL = (By.XPATH, "//label[text() = 'Email']/parent::div/input")  # Поле "Почта"
    REG_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/parent::div/input")  # Поле "Пароль"
    REG_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    INCORRECT_PASS = (By.XPATH, ".//p[text()='Некорректный пароль']")  # Сообщение "Некорректный пароль"
    ENTER_BUTTON = (By.CSS_SELECTOR, ".Auth_link__1fOlj")  # Кнопка "Войти"
    # Страница с формой восстановления /forgot-password
    ENTER_BUTTON_REC = (By.CSS_SELECTOR, ".Auth_link__1fOlj")  # Кнопка "Войти"
    RECOVERY_BUTTON = (By.XPATH, ".//button[text()='Восстановить']") # Кнопка "Восстановить"
    # Страница с личным кабинетом /account/profile
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка "Конструктор"
    LOGO_BUTTON = (By.XPATH, ".//div[contains(@class,'2D0X2')]/a")  # Кнопка логотипа
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # Кнопка "Выход"
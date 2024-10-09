from selenium.webdriver.common.by import By

# Локаторы для формы регистрации
NAME_INPUT_FIELD = (By.XPATH, '//label[text()="Имя"]/parent::div/input')  # Поле ввода имени в форме регистрации
EMAIL_INPUT_FIELD = (By.XPATH, '//label[text()="Email"]/parent::div/input')  # Поле ввода email в форме регистрации
PASSWORD_INPUT_FIELD = (By.XPATH, '//label[text()="Пароль"]/parent::div/input') # Пароль при регистрации
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка для отправки формы регистрации
REGISTER_ERROR = (By.XPATH, "//*[text()='Некорректный пароль']") # Сообщение об ошибке при некорректном пароле

# Локаторы для входа в аккаунт
LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")  # Заголовок страницы входа в аккаунт
USERNAME_INPUT_FIELD = (By.XPATH, '//input[@name="name" and @type="text"]') # Поле для ввода email на странице входа
PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@name="Пароль" and @type="password"]') # Поле для ввода пароля на странице входа
LOGIN_BUTTON = (By.XPATH,"//button[text()='Войти']")  # Кнопка для входа в аккаунт
LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]') # Кнопка войти в аккаунт
PLACE_AN_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')  # Кнопка для входа в аккаунт с главной страницы
REGISTER_AND_FORGOT_PASSWORD_LOGIN_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj") # Кнопка войти

# Локаторы для оформления заказа
ORDER_BUTTON = (By.XPATH,"//button[text()='Оформить заказ']")  # Кнопка для оформления заказа

# Локаторы для личного кабинета
PERSONAL_CABINET_LINK = (By.XPATH, '//p[contains(@class, "AppHeader_header__linkText__3q_va") and text()="Личный Кабинет"]') # Ссылка для перехода в личный кабинет
LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]') # Кнопка для выхода из аккаунта

# Локаторы для входа с разных страниц
LOGIN_FROM_REGISTRATION_BUTTON = (By.XPATH,"//a[contains(@class, 'Auth_link__1fOlj')]")  # Кнопка для входа на страницах регистрации и восстановления пароля

# Локаторы для конструктора бургера
CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")  # Ссылка для перехода в конструктор бургера
SVG_ICON = (By.CSS_SELECTOR, "svg[xmlns='http://www.w3.org/2000/svg']")  # Логотип для перехода на главную страницу

# Локаторы для разделов конструктора
BUNS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Булки']]") # Раздел "Булки"
SAUCES_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Соусы']]")   # Раздел "Соусы"
FILLINGS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Начинки']]") # Раздел "Начинки"

# Локаторы для активных разделов конструктора
BUNS_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current') and .//span[text()='Булки']]") # Активный раздел "Булки"
SAUCES_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current') and .//span[text()='Соусы']]")  # Активный раздел "Соусы"
FILLINGS_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current') and .//span[text()='Начинки']]")  # Активный раздел "Начинки"

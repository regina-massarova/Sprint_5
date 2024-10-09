from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import (
    LOGIN_EMAIL_INPUT,
    LOGIN_PASSWORD_INPUT,
    LOGIN_BUTTON,
    LOGIN_FROM_ACCOUNT_PAGE_BUTTON,
    PLACE_ORDER_BUTTON,
    PERSONAL_CABINET_LINK,
    REGISTER_AND_FORGOT_PASSWORD_LOGIN_BUTTON
)
class TestLoginMethod:
    def test_login_via_account_button_on_main_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*LOGIN_FROM_ACCOUNT_PAGE_BUTTON).click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("regina_massarova_14_123@yandex.ru")
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123Regina!")
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(PLACE_ORDER_BUTTON))
        login_header = driver.find_element(*PLACE_ORDER_BUTTON).text
        assert login_header == 'Оформить заказ'

    def test_login_via_personal_cabinet_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*PERSONAL_CABINET_LINK).click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("regina_massarova_14_123@yandex.ru")
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123Regina!")
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(PLACE_ORDER_BUTTON))
        login_header = driver.find_element(*PLACE_ORDER_BUTTON).text
        assert login_header == 'Оформить заказ'

    def test_login_via_registration_form_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*REGISTER_AND_FORGOT_PASSWORD_LOGIN_BUTTON).click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("regina_massarova_14_123@yandex.ru")
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123Regina!")
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(PLACE_ORDER_BUTTON))
        login_header = driver.find_element(*PLACE_ORDER_BUTTON).text
        assert login_header == 'Оформить заказ'

    def test_login_via_password_recovery_form_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.find_element(*REGISTER_AND_FORGOT_PASSWORD_LOGIN_BUTTON).click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("regina_massarova_14_123@yandex.ru")
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123Regina!")
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(PLACE_ORDER_BUTTON))
        login_header = driver.find_element(*PLACE_ORDER_BUTTON).text
        assert login_header == 'Оформить заказ'


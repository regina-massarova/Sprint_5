from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import (
    USERNAME_INPUT_FIELD,
    PASSWORD_INPUT_FIELD,
    LOGIN_BUTTON,
    LOGIN_TO_ACCOUNT_BUTTON,
    PLACE_AN_ORDER,
    PERSONAL_CABINET_LINK,
    REGISTER_AND_FORGOT_PASSWORD_LOGIN_BUTTON
)
class TestLoginMethod:
    def test_login_via_account_button_on_main_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*USERNAME_INPUT_FIELD).send_keys("regina-massarova_14_123@yandex.ru")
        driver.find_element(*PASSWORD_INPUT_FIELD).send_keys("123Regina!")
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PLACE_AN_ORDER))
        login_header = driver.find_element(*PLACE_AN_ORDER).text
        assert login_header == 'Оформить заказ'

    def test_login_via_personal_cabinet_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*PERSONAL_CABINET_LINK).click()
        driver.find_element(*USERNAME_INPUT_FIELD).send_keys("regina-massarova_14_123@yandex.ru")
        driver.find_element(*PASSWORD_INPUT_FIELD).send_keys("123Regina!")
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PLACE_AN_ORDER))
        login_header = driver.find_element(*PLACE_AN_ORDER).text
        assert login_header == 'Оформить заказ'

    def test_login_via_registration_form_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*REGISTER_AND_FORGOT_PASSWORD_LOGIN_BUTTON).click()
        driver.find_element(*USERNAME_INPUT_FIELD).send_keys("regina-massarova_14_123@yandex.ru")
        driver.find_element(*PASSWORD_INPUT_FIELD).send_keys("123Regina!")
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PLACE_AN_ORDER))
        login_header = driver.find_element(*PLACE_AN_ORDER).text
        assert login_header == 'Оформить заказ'

    def test_login_via_password_recovery_form_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.find_element(*REGISTER_AND_FORGOT_PASSWORD_LOGIN_BUTTON).click()
        driver.find_element(*USERNAME_INPUT_FIELD).send_keys("regina-massarova_14_123@yandex.ru")
        driver.find_element(*PASSWORD_INPUT_FIELD).send_keys("123Regina!")
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PLACE_AN_ORDER))
        login_header = driver.find_element(*PLACE_AN_ORDER).text
        assert login_header == 'Оформить заказ'


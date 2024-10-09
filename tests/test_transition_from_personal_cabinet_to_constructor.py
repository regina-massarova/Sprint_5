from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import (
    USERNAME_INPUT_FIELD,
    PASSWORD_INPUT_FIELD,
    LOGIN_BUTTON,
    LOGIN_TO_ACCOUNT_BUTTON,
    PLACE_AN_ORDER,
    PERSONAL_CABINET_LINK,
    LOGOUT_BUTTON,
    CONSTRUCTOR_LINK,
    SVG_ICON
)

class TestTransitionFromPersonalCabinetToConstructor:

    def test_transition_to_constructor_via_personal_cabinet(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*USERNAME_INPUT_FIELD).send_keys("regina-massarova_14_123@yandex.ru")
        driver.find_element(*PASSWORD_INPUT_FIELD).send_keys("123Regina!")
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PLACE_AN_ORDER))
        driver.find_element(*PERSONAL_CABINET_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGOUT_BUTTON))
        driver.find_element(*CONSTRUCTOR_LINK).click()
        login_header = driver.find_element(*PLACE_AN_ORDER).text
        assert login_header == 'Оформить заказ'

    def test_transition_to_constructor_via_logo(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*USERNAME_INPUT_FIELD).send_keys("regina-massarova_14_123@yandex.ru")
        driver.find_element(*PASSWORD_INPUT_FIELD).send_keys("123Regina!")
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PLACE_AN_ORDER))
        driver.find_element(*PERSONAL_CABINET_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGOUT_BUTTON))
        driver.find_element(*SVG_ICON).click()
        login_header = driver.find_element(*PLACE_AN_ORDER).text
        assert login_header == 'Оформить заказ'

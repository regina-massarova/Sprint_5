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
    LOGOUT_BUTTON
)

class TestOpenPersonalAccount:
    def test_open(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*USERNAME_INPUT_FIELD).send_keys("regina-massarova_14_123@yandex.ru")
        driver.find_element(*PASSWORD_INPUT_FIELD).send_keys("123Regina!")
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PLACE_AN_ORDER))
        driver.find_element(*PERSONAL_CABINET_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGOUT_BUTTON))
        logout_button = driver.find_element(*LOGOUT_BUTTON).text
        assert logout_button == 'Выход'
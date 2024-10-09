from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import generate_random_email

from locators import (
    NAME_INPUT_FIELD,
    EMAIL_INPUT_FIELD,
    PASSWORD_INPUT_FIELD,
    REGISTER_BUTTON,
    REGISTER_ERROR,
    LOGIN_HEADER
)

class TestRegistration:
    def test_registration_with_incorrect_password(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*NAME_INPUT_FIELD).send_keys("NameTest1")
        driver.find_element(*EMAIL_INPUT_FIELD).send_keys("name_test_14_123@yandex.ru")
        driver.find_element(*PASSWORD_INPUT_FIELD).send_keys("8766")
        driver.find_element(*REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(REGISTER_ERROR))
        error_message = driver.find_element(*REGISTER_ERROR).text
        assert error_message == 'Некорректный пароль'

    def test_registration_with_correct_password(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*NAME_INPUT_FIELD).send_keys("Test")
        unique_email = generate_random_email()
        driver.find_element(*EMAIL_INPUT_FIELD).send_keys(unique_email)
        driver.find_element(*PASSWORD_INPUT_FIELD).send_keys("1237865454")
        driver.find_element(*REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGIN_HEADER))
        login_header = driver.find_element(*LOGIN_HEADER).text
        assert login_header == 'Вход'
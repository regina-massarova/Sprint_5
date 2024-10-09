from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from locators import (
    BUNS_SECTION,
    SAUCES_SECTION,
    FILLINGS_SECTION,
    BUNS_SECTION_ACTIVE,
    SAUCES_SECTION_ACTIVE,
    FILLINGS_SECTION_ACTIVE
)

class TestNavigationToSections:
    def test_navigate_to_fillings_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*FILLINGS_SECTION).click()
        updated_button_fillings = driver.find_element(*FILLINGS_SECTION_ACTIVE)
        updated_class_fillings = updated_button_fillings.get_attribute("class")
        assert "tab_tab_type_current" in updated_class_fillings

    def test_navigate_to_sauces_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*SAUCES_SECTION).click()
        updated_button_sauses = driver.find_element(*SAUCES_SECTION_ACTIVE)
        updated_class_sauses = updated_button_sauses.get_attribute("class")
        assert "tab_tab_type_current" in updated_class_sauses

    def test_navigate_to_buns_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*SAUCES_SECTION).click()
        driver.find_element(*BUNS_SECTION).click()
        updated_button_buns = driver.find_element(*BUNS_SECTION_ACTIVE)
        updated_class_buns = updated_button_buns.get_attribute("class")
        assert "tab_tab_type_current" in updated_class_buns

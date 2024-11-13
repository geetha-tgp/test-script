import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from password_generator_page import PasswordGeneratorPage

@pytest.mark.parametrize("length", [6, 12, 20, 32])
def test_password_length(browser, length):
    page = PasswordGeneratorPage(browser)
    page.load()
    page.set_password_length(length)
    page.select_character_type("lowercase")
    page.select_character_type("uppercase")
    page.generate_password()
    password = page.get_generated_password()
    assert len(password) == length, f"Expected password length {length}, got {len(password)}"

def test_only_numbers(browser):
    page = PasswordGeneratorPage(browser)
    page.load()
    page.set_password_length(10)
    page.clear_character_types()
    page.select_character_type("numbers")
    page.generate_password()
    password = page.get_generated_password()
    assert password.isdigit(), "Password should contain only numbers"

def test_no_character_type_selected(browser):
    page = PasswordGeneratorPage(browser)
    page.load()
    page.set_password_length(10)
    page.clear_character_types()
    page.generate_password()
    password = page.get_generated_password()
    assert password == "", "Expected no password to be generated when no options are selected"

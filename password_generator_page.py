from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PasswordGeneratorPage:
    def __init__(self, browser):
        self.browser = browser
        self.password_length_input = (By.ID, "passwordLength")
        self.password_length_slider = (By.ID, "passwordLengthRange")
        self.option_lowercase = (By.ID, "option-lowercase")
        self.option_uppercase = (By.ID, "option-uppercase")
        self.option_numbers = (By.ID, "option-numbers")
        self.option_symbols = (By.ID, "option-symbols")
        self.generate_button = (By.ID, "generate")  # Assuming there's an ID for the generate button
        self.generated_password_field = (By.ID, "generatedPassword")  # Assuming there's an ID for the generated password

    def set_password_length(self, length):
        # Set the length using the input box
        length_input = self.browser.find_element(*self.password_length_input)
        length_input.clear()
        length_input.send_keys(str(length))

    def select_character_type(self, option):
        options = {
            "lowercase": self.option_lowercase,
            "uppercase": self.option_uppercase,
            "numbers": self.option_numbers,
            "symbols": self.option_symbols
        }
        checkbox = self.browser.find_element(*options[option])
        if not checkbox.is_selected():
            checkbox.click()

    def clear_character_types(self):
        # Deselect all character types
        for option in ["lowercase", "uppercase", "numbers", "symbols"]:
            checkbox = self.browser.find_element(*getattr(self, f"option_{option}"))
            if checkbox.is_selected():
                checkbox.click()

    def generate_password(self):
        self.browser.find_element(*self.generate_button).click()

    def get_generated_password(self):
        return self.browser.find_element(*self.generated_password_field).text

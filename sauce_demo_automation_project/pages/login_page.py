# pages/login_page.py
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def load(self):
        """Load the login page"""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def load(self):
        """Load the Sauce Demo login page"""
        self.driver.get("https://www.saucedemo.com/")

    def is_login_page_displayed(self):
        """Check if the login page is displayed after logout"""
        return self.driver.find_element(*self.username_field).is_displayed()
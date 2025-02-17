import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url

def test_invalid_login_incorrect_username(driver):
    login_page = LoginPage(driver)
    login_page.login("standard", "secret_sauce")
    assert "inventory.html" in driver.current_url

def test_invalid_login_incorrect_password(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "nonsecret_sauce")
    assert "inventory.html" in driver.current_url

def test_invalid_login_empty_credentials(driver):
    login_page = LoginPage(driver)
    login_page.login("", "")
    assert "inventory.html" in driver.current_url

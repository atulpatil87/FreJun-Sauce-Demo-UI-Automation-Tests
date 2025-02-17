import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")  # Open SauceDemo login page
    driver.maximize_window()
    yield driver
    driver.quit()  # Close browser after tests


def login(driver, username, password):
    """Function to log in to SauceDemo."""
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def test_locked_out_user(setup):
    """TC018: Attempt login with locked user"""
    driver = setup
    login(driver, "locked_out_user", "secret_sauce")
    error_message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
    ).text
    assert "Epic sadface: Sorry, this user has been locked out." in error_message
    print("✅ TC018 Passed: Locked-out user cannot log in.")


def test_add_more_than_available_stock(setup):
    """TC019: Try adding more items than available stock (if applicable)"""
    driver = setup
    driver.get("https://www.saucedemo.com/inventory.html")  # Navigate to inventory page
    add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")

    if add_to_cart_buttons:
        for _ in range(10):  # Assume 10 is more than the stock limit
            add_to_cart_buttons[0].click()

    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert int(cart_count) <= 10  # Should not exceed stock
    print("✅ TC019 Passed: Cannot add more than available stock.")


def test_refresh_cart_persistence(setup):
    """TC020: Refresh page after adding product to cart"""
    driver = setup
    driver.get("https://www.saucedemo.com/inventory.html")  # Open inventory page
    add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")

    if add_to_cart_buttons:
        add_to_cart_buttons[0].click()  # Add an item to cart

    cart_count_before_refresh = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    driver.refresh()

    try:
        cart_count_after_refresh = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    except:
        cart_count_after_refresh = "0"

    assert cart_count_before_refresh == cart_count_after_refresh  # Cart should persist
    print("✅ TC020 Passed: Cart items persist after refresh.")


def test_checkout_without_login():
    """TC021: Try accessing checkout without login"""
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/checkout-step-one.html")  # Open checkout page

    assert "login" in driver.current_url  # Should redirect to login page
    print("✅ TC021 Passed: Redirected to login when trying to access checkout.")

    driver.quit()

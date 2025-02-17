import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCheckout:

    def test_complete_checkout_successfully(self, driver):
        """Test completing checkout successfully"""
        # Step 1: Login
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        # Step 2: Add product and go to cart
        home_page = HomePage(driver)
        home_page.add_product_to_cart(0)
        home_page.open_cart()

        # Step 3: Start checkout process
        cart_page = CartPage(driver)
        cart_page.click_checkout()

        # Step 4: Enter checkout details and complete order
        checkout_page = CheckoutPage(driver)
        checkout_page.enter_checkout_details("John", "Doe", "12345")
        checkout_page.click_continue()
        checkout_page.click_finish()

        # Step 5: Verify success message
        assert checkout_page.is_order_successful(), "Order confirmation message not displayed!"

    def test_attempt_checkout_with_empty_cart(self, driver):
        """Test attempting to checkout with an empty cart"""
        # Step 1: Login
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        # Step 2: Open empty cart and attempt checkout
        home_page = HomePage(driver)
        home_page.open_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        # Step 3: Verify checkout button is disabled or error message appears
        checkout_page = CheckoutPage(driver)
        assert checkout_page.is_checkout_blocked(), "Checkout proceeded with an empty cart!"

    def test_checkout_with_missing_details(self, driver):
        """Test attempting checkout with missing details"""
        # Step 1: Login
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        # Step 2: Add product and go to cart
        home_page = HomePage(driver)
        home_page.add_product_to_cart(0)
        home_page.open_cart()

        # Step 3: Start checkout process
        cart_page = CartPage(driver)
        cart_page.click_checkout()

        # Step 4: Leave fields empty and continue
        checkout_page = CheckoutPage(driver)
        checkout_page.enter_checkout_details("", "", "")
        checkout_page.click_continue()

        # Step 5: Verify error message appears
        assert checkout_page.get_checkout_error_message() == "Error: First Name is required", "Error message not displayed!"

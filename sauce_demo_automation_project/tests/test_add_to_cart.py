import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage


@pytest.mark.usefixtures("driver")
class TestAddToCart:
    def test_add_single_product_to_cart(self, driver):
        """Test adding a single product to the cart"""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        home_page = HomePage(driver)
        home_page.add_product_to_cart(0)  # Add first product
        home_page.open_cart()

        cart_page = CartPage(driver)
        cart_items = cart_page.get_cart_items()

        assert len(cart_items) == 1, "Cart does not contain exactly one product!"

    def test_add_multiple_products_to_cart(self, driver):
        """Test adding multiple products to the cart"""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        home_page = HomePage(driver)
        home_page.add_multiple_products_to_cart([0, 1])  # Add first two products
        home_page.open_cart()

        cart_page = CartPage(driver)
        cart_items = cart_page.get_cart_items()

        assert len(cart_items) == 2, "Cart does not contain the correct number of products!"

    def test_verify_total_price_in_cart(self, driver):
        """Test if the total price in the cart matches product prices"""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        home_page = HomePage(driver)
        home_page.add_multiple_products_to_cart([0, 1])  # Add first two products
        home_page.open_cart()

        cart_page = CartPage(driver)
        cart_items = cart_page.get_cart_items()
        assert len(cart_items) == 2, "Cart does not contain the correct number of products!"

        # Verify total price
        total_price = cart_page.get_total_price()
        item_prices = home_page.get_item_prices()
        expected_total = item_prices[0] + item_prices[1]

        assert total_price == expected_total, f"Expected total price: {expected_total}, but found: {total_price}"

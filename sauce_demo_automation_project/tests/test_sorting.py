import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.usefixtures("driver")
class TestSorting:
    def test_sort_items_low_to_high(self, driver):
        """Test sorting items from Low to High Price"""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        home_page = HomePage(driver)
        home_page.sort_items("lohi")

        sorted_prices = home_page.get_item_prices()
        assert sorted_prices == sorted(sorted_prices), "Items are NOT sorted from Low to High"

    def test_sort_items_high_to_low(self, driver):
        """Test sorting items from High to Low Price"""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        home_page = HomePage(driver)
        home_page.sort_items("hilo")

        sorted_prices = home_page.get_item_prices()
        assert sorted_prices == sorted(sorted_prices, reverse=True), "Items are NOT sorted from High to Low"

    def test_sort_items_name_a_to_z(self, driver):
        """Test sorting items by Name A to Z"""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        home_page = HomePage(driver)
        home_page.sort_items("az")

        sorted_names = home_page.get_item_names()
        assert sorted_names == sorted(sorted_names), "Items are NOT sorted alphabetically (A to Z)"

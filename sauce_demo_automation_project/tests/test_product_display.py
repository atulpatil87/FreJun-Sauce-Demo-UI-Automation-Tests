import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage

@pytest.mark.usefixtures("driver")
class TestProductDisplay:
    def test_verify_product_images_and_names(self, driver):
        """Test if product images and names are displayed"""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        product_page = ProductPage(driver)
        images, names = product_page.get_all_products()

        assert len(images) > 0, "No product images found!"
        assert len(names) > 0, "No product names found!"
        for img, name in zip(images, names):
            assert img.is_displayed(), f"Product image not displayed for {name.text}"
            assert name.is_displayed(), f"Product name not displayed: {name.text}"

    def test_verify_product_details_accessible(self, driver):
        """Test if clicking a product name opens the details page"""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        product_page = ProductPage(driver)
        product_page.click_on_product(product_index=0)

        assert product_page.is_product_details_displayed(), "Product details page did not open!"

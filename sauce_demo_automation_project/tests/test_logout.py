import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.logout_page import LogoutPage


class TestLogout:
    def test_successful_logout(self, driver):
        """Test if the user is successfully logged out"""
        # Step 1: Login
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        # Step 2: Click Logout
        logout_page = LogoutPage(driver)
        logout_page.logout()

        # Step 3: Verify redirection to login page
        assert login_page.is_login_page_displayed(), "User was NOT redirected to the login page after logout!"

    def test_session_expiration_after_logout(self, driver):
        """Test if accessing inventory page after logout redirects to login"""
        # Step 1: Login
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        # Step 2: Logout
        logout_page = LogoutPage(driver)
        logout_page.logout()

        # Step 3: Try to access inventory page via back button
        driver.back()

        # Step 4: Verify user is still on login page
        assert login_page.is_login_page_displayed(), "User was able to access inventory page after logout!"

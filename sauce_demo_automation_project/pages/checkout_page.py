from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.finish_btn = (By.ID, "finish")
        self.success_message = (By.CLASS_NAME, "complete-header")
        self.error_message = (By.CLASS_NAME, "error-message-container")

    def enter_checkout_details(self, first_name, last_name, postal_code):
        """Enter first name, last name, and postal code during checkout"""
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)

    def click_continue(self):
        """Click the Continue button"""
        self.driver.find_element(*self.continue_btn).click()

    def click_finish(self):
        """Click the Finish button"""
        self.driver.find_element(*self.finish_btn).click()

    def is_order_successful(self):
        """Check if order confirmation message is displayed"""
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.success_message)
            )
        except:
            return False

    def is_checkout_blocked(self):
        """Check if checkout is blocked when cart is empty"""
        return "Your cart is empty" in self.driver.page_source  # Adjust if needed

    def get_checkout_error_message(self):
        """Get error message when checkout fails"""
        try:
            return self.driver.find_element(*self.error_message).text
        except:
            return None

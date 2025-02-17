from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.checkout_button = (By.ID, "checkout")
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.cart_total_price = (By.CLASS_NAME, "summary_subtotal_label")

    from selenium.webdriver.common.by import By

    class CartPage:
        def __init__(self, driver):
            self.driver = driver
            self.checkout_button = (By.ID, "checkout")

        def click_checkout(self):
            """Click the checkout button to proceed to checkout"""
            self.driver.find_element(*self.checkout_button).click()

    def get_cart_items(self):
        """Retrieve all cart items"""
        return self.driver.find_elements(*self.cart_items)

    def get_total_price(self):
        """Retrieve total cart price with better waiting strategy"""
        try:
            total_price_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.cart_total_price)
            )
            total_text = total_price_element.text  # Example: "Total: $43.18"
            total_price = float(total_text.split("$")[1])  # Extract numeric value
            return total_price
        except Exception as e:
            print(f"❌ ERROR: Failed to retrieve total price - {str(e)}")
            return None  # Return None for better debugging

    def click_checkout(self):
            """Click the checkout button to proceed to checkout"""
            self.driver.find_element(*self.checkout_button).click()

    def fill_user_info(self):
            self.driver.find_element(By.ID, "checkout").click()
            self.driver.find_element(By.ID, "first-name").send_keys("John")
            self.driver.find_element(By.ID, "last-name").send_keys("Doe")
            self.driver.find_element(By.ID, "postal-code").send_keys("12345")
            self.driver.find_element(By.ID, "continue").click()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_images = (By.CLASS_NAME, "inventory_item_img")
        self.product_names = (By.CLASS_NAME, "inventory_item_name")
        self.product_details_name = (By.CLASS_NAME, "inventory_details_name")  # FIXED selector
        self.product_description = (By.CLASS_NAME, "inventory_details_desc")
        self.product_price = (By.CLASS_NAME, "inventory_details_price")

    def get_all_products(self):
        """Retrieve all product elements"""
        images = self.driver.find_elements(*self.product_images)
        names = self.driver.find_elements(*self.product_names)
        return images, names

    def click_on_product(self, product_index=0):
        """Click on a product name to open details"""
        product_names = self.driver.find_elements(*self.product_names)
        if product_names:
            product_names[product_index].click()
        else:
            raise Exception("No products found on the page!")

    def is_product_details_displayed(self):
        """Wait for product details page to load and verify elements are displayed"""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.product_details_name)  # FIXED selector
            )
            name = self.driver.find_element(*self.product_details_name)  # FIXED selector
            description = self.driver.find_element(*self.product_description)
            price = self.driver.find_element(*self.product_price)
            return name.is_displayed() and description.is_displayed() and price.is_displayed()
        except Exception as e:
            print(f"Error in product details verification: {e}")
            return False

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.item_prices = (By.CLASS_NAME, "inventory_item_price")
        self.item_names = (By.CLASS_NAME, "inventory_item_name")

    def sort_items(self, sort_option):
        """Sort items using the given sorting option"""
        dropdown = Select(self.driver.find_element(*self.sort_dropdown))
        sort_mapping = {
            "lohi": "Price (low to high)",
            "hilo": "Price (high to low)",
            "az": "Name (A to Z)"
        }
        if sort_option in sort_mapping:
            dropdown.select_by_visible_text(sort_mapping[sort_option])
        else:
            raise ValueError(f"Invalid sort option: {sort_option}")

    def get_item_prices(self):
        """Retrieve product prices as a list of float values"""
        price_elements = self.driver.find_elements(*self.item_prices)
        return [float(price.text.replace("$", "")) for price in price_elements]

    def get_item_names(self):
        """Retrieve product names as a list of strings"""
        name_elements = self.driver.find_elements(*self.item_names)
        return [name.text for name in name_elements]

    def __init__(self, driver):
        self.driver = driver
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.item_prices = (By.CLASS_NAME, "inventory_item_price")
        self.add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self, product_index=0):
        """Click Add to Cart button for a given product"""
        add_buttons = self.driver.find_elements(*self.add_to_cart_buttons)
        if product_index < len(add_buttons):
            add_buttons[product_index].click()
        else:
            raise Exception("Product index out of range!")

    def add_multiple_products_to_cart(self, product_indices):
        """Add multiple products to the cart"""
        add_buttons = self.driver.find_elements(*self.add_to_cart_buttons)
        for index in product_indices:
            if index < len(add_buttons):
                add_buttons[index].click()
            else:
                raise Exception("Product index out of range!")

    def open_cart(self):
        """Navigate to the cart page"""
        self.driver.find_element(*self.cart_icon).click()

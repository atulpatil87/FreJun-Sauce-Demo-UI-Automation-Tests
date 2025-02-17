import time
from time import sleep

import self
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        # self.menu_button = (By.ID, "bm_burger_button")
        self.menu_button = (By.XPATH, "//*[@id='menu_button_container']/div/div[1]/div")
        self.logout_button = (By.ID, "logout_sidebar_link")


    def logout(self):
        """Click on the menu and select Logout"""
        self.driver.find_element(*self.menu_button).click()
        time.sleep(10)
        logout_button = self.driver.find_element(*self.logout_button)
        self.driver.execute_script("arguments[0].click();", logout_button)








import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    """Setup WebDriver fixture using pytest"""
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")  # Run in headless mode (optional)
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.maximize_window()
        yield driver
    except Exception as e:
        print(f"WebDriver setup failed: {e}")
    finally:
        driver.quit()

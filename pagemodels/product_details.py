from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from testdata.model.product import Product


class ProductDetails:
    def __init__(self, driver: webdriver):
        self._driver = driver

    # Locators
    _manufacturer_css = "dl.row dd:nth-child(2)"
    _model_css = "dl.row dd:nth-child(4)"
    _price_css = "dl.row dd:nth-child(6)"
    _number_in_stock_css = "dl.row dd:nth-child(8)"

    # Get
    def get_product(self) -> Product: 
        return Product(
            self._driver.find_element(By.CSS_SELECTOR, ProductDetails._manufacturer_css).text,
            self._driver.find_element(By.CSS_SELECTOR, ProductDetails._model_css).text,
            int(self._driver.find_element(By.CSS_SELECTOR, ProductDetails._price_css).text),
            int(self._driver.find_element(By.CSS_SELECTOR, ProductDetails._number_in_stock_css).text)
        )
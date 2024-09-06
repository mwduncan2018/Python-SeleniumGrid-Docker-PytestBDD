from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from testdata.model.product import Product


class ProductAdd:
    def __init__(self, driver: webdriver):
        self._driver = driver

    # Locators
    _manufacturer_id = "Manufacturer"
    _model_id = "Model"
    _price_id = "Price"
    _number_in_stock_id = "NumberInStock"
    _add_button_css = ".form-group input[value='Add']"

    # Action
    def add_product(self, product: Product):
        self._driver.find_element(By.ID, ProductAdd._manufacturer_id).send_keys(product.manufacturer)
        self._driver.find_element(By.ID, ProductAdd._model_id).send_keys(product.model)
        self._driver.find_element(By.ID, ProductAdd._price_id).send_keys(str(product.price))
        self._driver.find_element(By.ID, ProductAdd._number_in_stock_id).send_keys(str(product.number_in_stock))
        self._driver.find_element(By.CSS_SELECTOR, ProductAdd._add_button_css).submit()            
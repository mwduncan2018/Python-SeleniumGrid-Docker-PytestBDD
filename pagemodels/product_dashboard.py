from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from testdata.model.product import Product


class ProductDashboard:
    def __init__(self, driver: webdriver):
        self._driver = driver

    # Locators
    _add_new_product_link_text = "Add New Product"
    _fuzzy_matching_id = "fuzzFuzz"
    _table_rows_css = "tbody tr"
    _table_match_css = "td:nth-child(1) > input"
    _table_manufacturer_css = "td:nth-child(2)"
    _table_model_css = "td:nth-child(3)"
    _table_price_css = "td:nth-child(4)"
    _table_number_in_stock_css = "td:nth-child(5)"
    _table_edit_css = "td:nth-child(6) a:nth-child(1)"
    _table_details_css = "td:nth-child(6) a:nth-child(2)"
    _table_delete_css = "td:nth-child(6) a:nth-child(3)"
    _table_fuzzy_match_css = "td:nth-child(7) > input"

    # Actions
    def add_new_product(self):
        self._driver.find_element(By.LINK_TEXT, ProductDashboard._add_new_product_link_text).click()
    
    def enable_standard_matching(self):
        if self.is_fuzzy_matching_enabled():
            self._driver.find_element(By.ID, ProductDashboard._fuzzy_matching_id).click()

    def enable_fuzzy_matching(self):
        if not self.is_fuzzy_matching_enabled():
            self._driver.find_element(By.ID, ProductDashboard._fuzzy_matching_id).click()

    def edit(self, product: Product):
        for row in self._driver.find_elements(By.CSS_SELECTOR, ProductDashboard._table_rows_css):
            if " ".join([product.manufacturer, product.model]) in row.text:
                row.find_element(By.CSS_SELECTOR, ProductDashboard._table_edit_css).click()
                return

    def details(self, product: Product):
        for row in self._driver.find_elements(By.CSS_SELECTOR, ProductDashboard._table_rows_css):
            if " ".join([product.manufacturer, product.model]) in row.text:
                row.find_element(By.CSS_SELECTOR, ProductDashboard._table_details_css).click()
                return

    def delete(self, product: Product):
        for row in self._driver.find_elements(By.CSS_SELECTOR, ProductDashboard._table_rows_css):
            if " ".join([product.manufacturer, product.model]) in row.text:
                row.find_element(By.CSS_SELECTOR, ProductDashboard._table_delete_css).click()
                return

    # Conditional
    def is_fuzzy_matching_enabled(self) -> bool:
        return self._driver.find_element(By.ID, ProductDashboard._fuzzy_matching_id).text == "Disable Fuzzy Matching!"
    
    def is_product_displayed_in_table(self, product: Product) -> bool: 
        for row in self._driver.find_elements(By.CSS_SELECTOR, ProductDashboard._table_rows_css):
            if " ".join([product.manufacturer, product.model]) in row.text:
                return True
        return False

    def is_product_a_standard_match(self, product: Product) -> bool:
        index = self.get_row_index_of(product)
        if index == -1:
            return False
        if self._driver.find_elements(By.CSS_SELECTOR, ProductDashboard._table_match_css)[index].get_attribute("checked") == "true":
            return True
        return False

    def is_product_a_fuzzy_match(self, product: Product) -> bool:
        index = self.get_row_index_of(product)
        if index == -1:
            return False
        fuzzy_matches = self._driver.find_elements(By.CSS_SELECTOR, ProductDashboard._table_fuzzy_match_css)
        if len(fuzzy_matches) == 0:
            return False
        if fuzzy_matches[index].get_attribute("checked") == "true":
            return True
        return False

    # Get
    def get_row_index_of(self, product: Product) -> bool:
        rows = self._driver.find_elements(By.CSS_SELECTOR, ProductDashboard._table_rows_css)
        for i, row in enumerate(rows):
            if " ".join([product.manufacturer, product.model]) in row.text:
                return i
        return -1
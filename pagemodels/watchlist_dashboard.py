from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from testdata.model.watchlist_entry import WatchListEntry


class WatchListDashboard:
    def __init__(self, driver: webdriver):
        self._driver = driver

    # Locators
    _add_new_entry_link_text = "Add To Watch List"
    _table_rows_css = "tbody tr"
    _table_manufacturer_css = "td:nth-child(1)"
    _table_model_css = "td:nth-child(2)"
    _table_edit_css = "td:nth-child(3) a:nth-child(1)"
    _table_details_css = "td:nth-child(3) a:nth-child(2)"
    _table_delete_css = "td:nth-child(3) a:nth-child(3)"

    # Actions
    def add_new_entry(self):
        self._driver.find_element(By.LINK_TEXT, WatchListDashboard._add_new_entry_link_text).click()

    def edit(self, entry: WatchListEntry):
        for row in self._driver.find_elements(By.CSS_SELECTOR, WatchListDashboard._table_rows_css):
            if " ".join([entry.manufacturer, entry.model]) in row.text:
                row.find_element(By.CSS_SELECTOR, WatchListDashboard._table_edit_css).click()
                return

    def details(self, entry: WatchListEntry):
        for row in self._driver.find_elements(By.CSS_SELECTOR, WatchListDashboard._table_rows_css):
            if " ".join([entry.manufacturer, entry.model]) in row.text:
                row.find_element(By.CSS_SELECTOR, WatchListDashboard._table_details_css).click()
                return

    def delete(self, entry: WatchListEntry):
        for row in self._driver.find_elements(By.CSS_SELECTOR, WatchListDashboard._table_rows_css):
            if " ".join([entry.manufacturer, entry.model]) in row.text:
                row.find_element(By.CSS_SELECTOR, WatchListDashboard._table_delete_css).click()
                return

    # Conditional
    def is_entry_displayed_in_table(self, entry: WatchListEntry) -> bool: 
        for row in self._driver.find_elements(By.CSS_SELECTOR, WatchListDashboard._table_rows_css):
            if " ".join([entry.manufacturer, entry.model]) in row.text:
                return True
        return False

    # Get
    def get_row_index_of(self, entry: WatchListEntry) -> bool:
        rows = self._driver.find_elements(By.CSS_SELECTOR, WatchListDashboard._table_rows_css)
        for i, row in enumerate(rows):
            if " ".join([entry.manufacturer, entry.model]) in row.text:
                return i
        return -1
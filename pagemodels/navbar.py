from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from configprovider.config_provider import ConfigProvider


class Navbar:
    def __init__(self, driver: webdriver):
        self._driver = driver

    # Locators
    _product_dashboard_link_text = "Product List"
    _watchlist_dashboard_link_text = "Watch List"
    _contact_link_text = "Contact"

    # Actions
    def go_to_product_dashboard(self):
        self._driver.get(ConfigProvider.get_url() + "/ProductList")
    
    def go_to_watchlist_dashboard(self):
        self._driver.get(ConfigProvider.get_url() + "/WatchList")
    
    def go_to_contact(self):
        self._driver.get(ConfigProvider.get_url() + "/Home/Contact")
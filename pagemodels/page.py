from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from configprovider.config_provider import ConfigProvider

from pagemodels.contact import Contact
from pagemodels.navbar import Navbar
from pagemodels.product_add import ProductAdd
from pagemodels.product_dashboard import ProductDashboard
from pagemodels.product_delete import ProductDelete
from pagemodels.product_details import ProductDetails
from pagemodels.product_edit import ProductEdit
from pagemodels.watchlist_add import WatchListAdd
from pagemodels.watchlist_dashboard import WatchListDashboard
from pagemodels.watchlist_delete import WatchListDelete
from pagemodels.watchlist_details import WatchListDetails
from pagemodels.watchlist_edit import WatchListEdit


class Page:
    def __init__(self, driver: webdriver):
        """Initialize all page objects with the provided driver"""
        self._driver = driver
        self.contact = Contact(driver)
        self.navbar = Navbar(driver)
        self.product_add = ProductAdd(driver) 
        self.product_dashboard = ProductDashboard(driver) 
        self.product_delete = ProductDelete(driver) 
        self.product_details = ProductDetails(driver) 
        self.product_edit = ProductEdit(driver)
        self.watchlist_add = WatchListAdd(driver) 
        self.watchlist_dashboard = WatchListDashboard(driver)
        self.watchlist_details = WatchListDetails(driver) 
        self.watchlist_delete = WatchListDelete(driver) 
        self.watchlist_edit = WatchListEdit(driver) 

    def open_app(self):
        self._driver.get(ConfigProvider.get_url() + "/ProductList")
    
    def close_app(self):
        self._driver.close()
        self._driver.quit()
from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from testdata.model.watchlist_entry import WatchListEntry


class WatchListDetails:
    def __init__(self, driver: webdriver):
        self._driver = driver

    # Locators
    _manufacturer_css = "dl.row dd:nth-child(2)"
    _model_css = "dl.row dd:nth-child(4)"

    # Get
    def get_entry(self) -> WatchListEntry: 
        return WatchListEntry(
            self._driver.find_element(By.CSS_SELECTOR, WatchListDetails._manufacturer_css).text,
            self._driver.find_element(By.CSS_SELECTOR, WatchListDetails._model_css).text,
        )
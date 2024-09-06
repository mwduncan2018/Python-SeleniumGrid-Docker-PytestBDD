from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from testdata.model.watchlist_entry import WatchListEntry


class WatchListAdd:
    def __init__(self, driver: webdriver):
        self._driver = driver

    # Locators
    _manufacturer_id = "Manufacturer"
    _model_id = "Model"
    _add_button_css = ".form-group input[value='Add']"

    # Action
    def add_entry(self, entry: WatchListEntry):
        self._driver.find_element(By.ID, WatchListAdd._manufacturer_id).send_keys(entry.manufacturer)
        self._driver.find_element(By.ID, WatchListAdd._model_id).send_keys(entry.model)
        self._driver.find_element(By.CSS_SELECTOR, WatchListAdd._add_button_css).submit()

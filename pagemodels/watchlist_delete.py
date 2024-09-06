import time
from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from testdata.model.watchlist_entry import WatchListEntry


class WatchListDelete:
    def __init__(self, driver: webdriver):
        self._driver = driver

    # Locators
    _confirm_delete_css = "form input[value='Confirm Delete']"

    # Action
    def confirm_delete(self):
        time.sleep(2)
        for i in range(5):
            try:
                self._driver.find_element(By.CSS_SELECTOR, WatchListDelete._confirm_delete_css).click()
            except:
                self._driver.refresh()
                time.sleep(3)
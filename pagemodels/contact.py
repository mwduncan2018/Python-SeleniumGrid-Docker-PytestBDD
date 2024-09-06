from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException


class Contact:
    def __init__(self, driver: webdriver):
        self._driver = driver

    # Locators
    _secret_message_id = "secretMessage"
    _github_css = "#github a"
    _skills_list_css = "#skillList li"

    # Get
    def get_github_href(self) -> str:
        return self._driver.find_element(By.CSS_SELECTOR, Contact._github_css).get_attribute("href")

    def get_list_of_skills(self) -> List[str]:
        return map(lambda x: x.text, self._driver.find_elements(By.CSS_SELECTOR, Contact._skills_list_css))

    # Conditional
    def does_footer_text_contain(self, text: str, seconds: int) -> bool:
        """Returns True if the text appears in the footer within the provided seconds"""
        try:
            return text in WebDriverWait(self._driver, seconds).until(lambda x: x.find_element(By.ID, Contact._secret_message_id)).text
        except:
            return False
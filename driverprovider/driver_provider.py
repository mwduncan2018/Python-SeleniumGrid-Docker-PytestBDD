import random
from configprovider.config_provider import ConfigProvider

from selenium import webdriver
from selenium.webdriver.edge.options import Options


class DriverProvider:
    _implicit_wait: int = ConfigProvider.get_implicit_wait()
    _horizontal_pixels: int = ConfigProvider.get_horizontal_pixels()
    _vertical_pixels: int = ConfigProvider.get_vertical_pixels()
    _environment: str = ConfigProvider.get_environment()
    _driver_type: str = ConfigProvider.get_driver_type()
    _maximize: bool = ConfigProvider.get_maximize()
    _grid_ip: str = ConfigProvider.get_grid_ip()

    @classmethod
    def get_driver(cls) -> webdriver:
        if cls._environment == "REMOTE": driver: webdriver = cls.get_remote_driver()
        if cls._environment == "LOCAL": driver: webdriver = cls.get_local_driver()
        driver.maximize_window() if cls._maximize == True else driver.set_window_size(cls._horizontal_pixels, cls._vertical_pixels)
        driver.implicitly_wait(cls._implicit_wait)
        return driver

    @classmethod
    def get_local_driver(cls) -> webdriver:
        if cls._driver_type == "EDGE" : return webdriver.Edge()
        if cls._driver_type == "CHROME" : return webdriver.Chrome()
        if cls._driver_type == "FIREFOX" : return webdriver.Firefox()
        if cls._driver_type == "RANDOM":
            r = random.randint(0, 1)
            if r == 0:
                return webdriver.Edge()
            if r == 1:
                return webdriver.Chrome() 
            #else:
            #    return webdriver.Firefox()


    @classmethod
    def get_remote_driver(cls) -> webdriver:
        options = None
        if cls._driver_type == "EDGE": options = webdriver.EdgeOptions()
        if cls._driver_type == "CHROME": options = webdriver.ChromeOptions()
        if cls._driver_type == "FIREFOX": options = webdriver.FirefoxOptions()
        if cls._driver_type == "RANDOM":
            r = random.randint(0, 2)
            if r == 0:
                options = webdriver.EdgeOptions()
            if r == 1:
                options = webdriver.ChromeOptions()
            else:
                options = webdriver.FirefoxOptions()
        grid_url = ConfigProvider.get_grid_ip() + "/wd/hub"
        driver = webdriver.Remote(command_executor=grid_url, options=options)
        return driver
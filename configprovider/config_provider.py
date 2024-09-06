import configparser

class ConfigProvider:
    _config = configparser.ConfigParser()
    _config.read("./automation_config.ini")

    _environment: str = _config["AUTOMATION CONFIG"]["Environment"]
    _grid_ip: str = _config["AUTOMATION CONFIG"]["GridIp"]
    _driver_type: str = _config["AUTOMATION CONFIG"]["DriverType"]
    _maximize: bool = _config["AUTOMATION CONFIG"]["Maximize"] in ["TRUE", "True", "true"]
    _horizontal_pixels: int = int(_config["AUTOMATION CONFIG"]["HorizontalPixels"])
    _vertical_pixels: int = int(_config["AUTOMATION CONFIG"]["VerticalPixels"])
    _url: str = _config["AUTOMATION CONFIG"]["URL"]
    _implicit_wait: int = int(_config["AUTOMATION CONFIG"]["ImplicitWait"])
    _test_data_path: str = _config["AUTOMATION CONFIG"]["TestDataPath"]

    @classmethod
    def print_config(cls):
        print("ENVIRONMENT: " + cls.get_environment())
        print("GRID IP: " + cls.get_grid_ip())
        print("DRIVER TYPE: " + cls.get_driver_type())
        print("MAXIMIZE: " + str(cls.get_maximize()))
        print("HORIZONTAL PIXELS: " + str(cls.get_horizontal_pixels()))
        print("VERTICAL PIXELS: " + str(cls.get_vertical_pixels()))
        print("URL: " + cls.get_url())
        print("IMPLICIT WAIT: " + str(cls.get_implicit_wait()))
        print("TEST DATA PATH: " + cls.get_test_data_path())

    @classmethod
    def get_environment(cls) -> str:
        return cls._environment.upper()

    @classmethod
    def get_grid_ip(cls) -> str:
        return cls._grid_ip

    @classmethod
    def get_driver_type(cls) -> str:
        return cls._driver_type.upper()

    @classmethod 
    def get_maximize(cls) -> bool:
        return cls._maximize
    
    @classmethod 
    def get_horizontal_pixels(cls) -> int:
        return cls._horizontal_pixels

    @classmethod 
    def get_vertical_pixels(cls) -> int:
        return cls._vertical_pixels

    @classmethod 
    def get_url(cls) -> str:
        return cls._url

    @classmethod
    def get_implicit_wait(cls) -> int:
        return cls._implicit_wait

    @classmethod 
    def get_test_data_path(cls) -> str:
        return cls._test_data_path
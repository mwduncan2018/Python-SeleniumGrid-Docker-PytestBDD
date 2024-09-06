from typing import List
import json 
import threading 

from testdata.model.product import Product


class ProductProvider:
    _test_data: List[Product] = []

    @classmethod 
    def initialize_test_data(cls):
        _raw_test_data: List
        _lock = threading.Lock()
        with _lock:
            with open("./testdata/json/product-test-data.json") as _f:
                _raw_test_data = json.load(_f)
        for _i in _raw_test_data:
            cls._test_data.append(Product(_i["Manufacturer"], _i["Model"], _i["Price"], _i["NumberInStock"]))

    @classmethod
    def get_all_products(cls) -> List[Product]:
        return cls._test_data

    @classmethod
    def get_by_manufacturer_and_model(cls, manufacturer: str, model: str) -> Product:
        return list(filter(lambda x: (x.manufacturer == manufacturer and x.model == model), cls._test_data))[0]
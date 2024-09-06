from typing import List
import json 
import threading 

from testdata.model.watchlist_entry import WatchListEntry


class WatchListEntryProvider:
    _test_data: List[WatchListEntry] = []

    @classmethod 
    def initialize_test_data(cls):
        _raw_test_data: List
        _lock = threading.Lock()
        with _lock:
            with open("./testdata/json/watchlist-test-data.json") as _f:
                _raw_test_data = json.load(_f)
        for _i in _raw_test_data:
            cls._test_data.append(WatchListEntry(_i["Manufacturer"], _i["Model"]))

    @classmethod
    def get_all_entries(cls) -> List[WatchListEntry]:
        return cls._test_data
   
    @classmethod
    def get_by_manufacturer_and_model(cls, manufacturer: str, model: str):
        return list(filter(lambda x: (x.manufacturer == manufacturer and x.model == model), cls._test_data))[0]
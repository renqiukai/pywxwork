from loguru import logger
from ..base import base


class living(base):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def get_user_livingid(self, data):
        api_name = "living/get_user_livingid"
        response = self.request(api_name=api_name, method="post", json=data)
        
        return response

    def get_user_livingid_demo(self):
        api_name = "living/get_user_livingid"
        data = {
            "userid": "ZhangHongYing",
            "begin_time": 1586136317,
            "end_time": 1595396774,
            "next_key": "0",
            "limit": 100,
        }
        response = self.request(api_name=api_name, method="post", json=data)
        
        return response

    def get_living_info(self, livingid):
        api_name = "living/get_living_info"
        params = {
            "livingid": livingid,
        }
        response = self.request(api_name=api_name, method="get", params=params)
        
        return response

    def get_watch_stat(self, livingid):
        api_name = "living/get_watch_stat"
        data = {"livingid": "livingid1", "next_key": "NEXT_KEY"}
        response = self.request(api_name=api_name, method="post", json=data)
        
        return response

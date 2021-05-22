from loguru import logger
from .base import base


class menu(base):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def create(self, data):
        api_name = "menu/create"
        response = self.request(
            api_name=api_name, method="post", json=data)
        logger.debug(response)
        return response

    def get(self, agentid):
        api_name = "menu/get"
        params = {
            "agentid": agentid
        }
        response = self.request(
            api_name=api_name, method="get", params=params)
        logger.debug(response)
        return response

    def delete(self, agentid):
        api_name = "menu/delete"
        params = {
            "agentid": agentid
        }
        response = self.request(
            api_name=api_name, method="get", params=params)
        logger.debug(response)
        return response

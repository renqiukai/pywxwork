from loguru import logger
from ..base import base


class ticket(base):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def get(self):
        api_name = "ticket/get"
        params = {"type": "agent_config"}
        response = self.request(api_name=api_name, method="get", params=params)
        return response

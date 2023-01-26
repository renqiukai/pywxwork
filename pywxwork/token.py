from .base import base
from loguru import logger
import datetime


class token(base):
    def __init__(self, corpid: str, corpsecret: str) -> None:
        """init

        Args:
            corpid (str): 企微corpid
            corpsecret (str): 企微secret
        """
        self.corpid = corpid
        self.corpsecret = corpsecret
        response = self.get()
        self.token = response.get("access_token")
        self.expires_in = response.get("expires_in")
        logger.debug(dict(msg="请求的token", token=self.token))

    def get(self):
        api_name = "gettoken"
        params = {
            "corpid": self.corpid,
            "corpsecret": self.corpsecret,
        }
        response = self.request(api_name=api_name, params=params)
        return response

    def cache_in(self):
        pass

    def cache_out(self):
        pass

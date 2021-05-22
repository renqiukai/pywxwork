from loguru import logger
from .base import base


class agent(base):
    def __init__(self, token) -> None:
        super().__init__(token)

    def get(self, agentid):
        api_name = "agent/get"
        params = {
            "agentid": agentid,
        }
        response = self.request(
            api_name=api_name, method="get", params=params)
        logger.debug(response)
        return response

    def set(self, data):
        api_name = "agent/set"
        response = self.request(
            api_name=api_name, method="post", json=data)
        logger.debug(response)
        return response

    def set_demo(self):
        data = {
            "agentid": 1000005,
            "report_location_flag": 0,
            "logo_mediaid": "j5Y8X5yocspvBHcgXMSS6z1Cn9RQKREEJr4ecgLHi4YHOYP-plvom-yD9zNI0vEl",
            "name": "财经助手",
            "description": "内部财经服务平台",
            "redirect_domain": "open.work.weixin.qq.com",
            "isreportenter": 0,
            "home_url": "https://open.work.weixin.qq.com"
        }
        response = self.set(data)
        logger.debug(response)
        return response

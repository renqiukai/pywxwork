from loguru import logger
import datetime
import requests


class token:
    host_name = "https://qyapi.weixin.qq.com/cgi-bin"

    def __init__(self, corpid: str, corpsecret: str, debug=False) -> None:
        """init

        Args:
            corpid (str): 企微corpid
            corpsecret (str): 企微secret
        """
        self.corpid = corpid
        self.corpsecret = corpsecret
        self.debug = debug
        response = self.get()
        self.token = response.get("access_token")
        self.expires_in = response.get("expires_in")
        logger.debug(dict(msg="请求的token", token=self.token))
        self.token_info = response

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

    def request(self, api_name, method="GET", **kwargs):
        url = f"{self.host_name}/{api_name}"

        params = kwargs.get("params", {})
        if self.debug:
            params["debug"] = 1
        kwargs["params"] = params

        logger.debug(dict(msg="正在请求的url:", url=url))
        logger.debug(dict(msg="正在请求的参数:", kwargs=kwargs))

        response = requests.request(
            method=method,
            url=url,
            **kwargs,
        )
        if response.status_code == 200:
            return self.response(response.json())
        logger.error(
            {
                "msg": "请求错误",
                "data": response.json(),
            }
        )

    def response(self, data):
        logger.debug(dict(msg="返回值", response=data))
        return data

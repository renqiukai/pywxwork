from loguru import logger
from ..base import base


class batch(base):
    def __init__(self, token) -> None:
        super().__init__(token)

    def syncuser(self, data):
        api_name = "batch/syncuser"
        response = self.request(api_name=api_name, method="post", json=data)
        return response

    def replaceuser(self, data):
        """全量覆盖成员
        https://open.work.weixin.qq.com/api/doc/90000/90135/90981
        """
        api_name = "batch/replaceuser"
        response = self.request(api_name=api_name, method="post", json=data)
        return response

    def replaceparty(self, data):
        """全量覆盖部门
        https://open.work.weixin.qq.com/api/doc/90000/90135/90982
        """
        api_name = "batch/replaceparty"
        response = self.request(api_name=api_name, method="post", json=data)
        return response

    def getresult(self, data):
        """获取异步任务结果
        https://open.work.weixin.qq.com/api/doc/90000/90135/90983
        """
        api_name = "batch/getresult"
        response = self.request(api_name=api_name, method="get", params=data)
        return response

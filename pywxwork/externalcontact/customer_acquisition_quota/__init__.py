from loguru import logger
from ...base import base


class customerAcquisitionQuota(base):
    def __init__(self, token: str):
        """
        https://developer.work.weixin.qq.com/document/path/97375#%E6%9F%A5%E8%AF%A2%E5%89%A9%E4%BD%99%E4%BD%BF%E7%94%A8%E9%87%8F
        """
        super().__init__(token)


    # 查询剩余使用量
    def get_quota(self):
        api_name = "externalcontact/customer_acquisition_quota"
        response = self.request(api_name=api_name, method="get")
        return response

    # 查询链接使用详情
    def statistic(self, link_id, start_time=1688140800, end_time=1688140800):
        api_name = "externalcontact/customer_acquisition/statistic"
        data = {
            "link_id": link_id,
            "start_time": start_time,
            "end_time": end_time,
        }
        response = self.request(api_name=api_name, method="post", json=data)
        return response

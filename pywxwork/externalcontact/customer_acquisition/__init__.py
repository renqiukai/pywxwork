from loguru import logger
from ...base import base


class customerAcquisition(base):
    def __init__(self, token: str):
        """
        接口地址：https://developer.work.weixin.qq.com/document/path/97297#%E8%8E%B7%E5%8F%96%E8%8E%B7%E5%AE%A2%E9%93%BE%E6%8E%A5%E5%88%97%E8%A1%A8
        """
        super().__init__(token)

    def list_link(self, limit=100, cursor="CURSOR"):
        api_name = "externalcontact/customer_acquisition/list_link"
        data = {"limit": limit, "cursor": cursor}
        response = self.request(api_name=api_name, method="post", json=data)
        return response

    def get(self, link_id):
        api_name = "externalcontact/customer_acquisition/get"
        data = {"link_id": link_id}
        response = self.request(api_name=api_name, method="post", json=data)
        return response

    def delete_link(self, link_id):
        api_name = "externalcontact/customer_acquisition/delete_link"
        data = {"link_id": link_id}
        response = self.request(api_name=api_name, method="post", json=data)
        return response

    def create_link(self, link_id):
        api_name = "externalcontact/customer_acquisition/list_link"
        data = {
            "link_name": "获客链接1号",
            "range": {"user_list": ["zhangsan", "lisi"], "department_list": [2, 3]},
            "skip_verify": True,
            "priority_option": {
                "priority_type": 2,
                "priority_userid_list": ["tom", "lisi"],
            },
        }
        response = self.request(api_name=api_name, method="post", json=data)
        return response

    def update_link(self):
        api_name = "externalcontact/customer_acquisition/list_link"
        data = {
            "link_id": "LINK_ID",
            "link_name": "获客链接1号",
            "range": {"user_list": ["zhangsan", "lisi"], "department_list": [2, 3]},
            "skip_verify": True,
            "priority_option": {
                "priority_type": 2,
                "priority_userid_list": ["tom", "lisi"],
            },
        }
        response = self.request(api_name=api_name, method="post", json=data)
        return response

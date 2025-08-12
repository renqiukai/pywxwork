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

    def create_link(self, data):
        """创建获客链接"""
        api_name = "externalcontact/customer_acquisition/create_link"
        response = self.request(api_name=api_name, method="post", json=data)
        return response

    def update_link(self, data):
        """更新获客链接"""
        api_name = "externalcontact/customer_acquisition/update_link"
        response = self.request(api_name=api_name, method="post", json=data)
        return response

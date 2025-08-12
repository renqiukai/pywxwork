from ...base import base
from loguru import logger


class groupWelcomeTemplate(base):
    """客户群欢迎语管理"""

    def __init__(self, token: str):
        super().__init__(token)

    def add(self, data):
        api_name = "externalcontact/group_welcome_template/add"
        return self.request(api_name=api_name, method="post", json=data)

    def edit(self, data):
        api_name = "externalcontact/group_welcome_template/edit"
        return self.request(api_name=api_name, method="post", json=data)

    def get(self, template_id):
        api_name = "externalcontact/group_welcome_template/get"
        data = {"template_id": template_id}
        return self.request(api_name=api_name, method="post", json=data)

    def delete(self, template_id):
        api_name = "externalcontact/group_welcome_template/del"
        data = {"template_id": template_id}
        return self.request(api_name=api_name, method="post", json=data)

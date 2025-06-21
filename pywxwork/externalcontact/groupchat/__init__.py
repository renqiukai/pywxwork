from ...base import base
from loguru import logger


class groupChat(base):
    """客户群管理"""

    def __init__(self, token: str):
        super().__init__(token)

    def list(self, status_filter=0, owner=None, limit=100, cursor=None):
        api_name = "externalcontact/groupchat/list"
        data = {
            "status_filter": status_filter,
            "limit": limit,
        }
        if owner:
            data["owner"] = owner
        if cursor:
            data["cursor"] = cursor
        return self.request(api_name=api_name, method="post", json=data)

    def get(self, chat_id, need_name=0):
        api_name = "externalcontact/groupchat/get"
        data = {"chat_id": chat_id, "need_name": need_name}
        return self.request(api_name=api_name, method="post", json=data)

    def add_join_way(self, data):
        api_name = "externalcontact/groupchat/add_join_way"
        return self.request(api_name=api_name, method="post", json=data)

    def get_join_way(self, config_id):
        api_name = "externalcontact/groupchat/get_join_way"
        data = {"config_id": config_id}
        return self.request(api_name=api_name, method="post", json=data)

    def update_join_way(self, data):
        api_name = "externalcontact/groupchat/update_join_way"
        return self.request(api_name=api_name, method="post", json=data)

    def del_join_way(self, config_id):
        api_name = "externalcontact/groupchat/del_join_way"
        data = {"config_id": config_id}
        return self.request(api_name=api_name, method="post", json=data)

    def transfer(self, chat_id_list: list, new_owner: str):
        api_name = "externalcontact/groupchat/transfer"
        data = {
            "chat_id_list": chat_id_list,
            "new_owner": new_owner,
        }
        return self.request(api_name=api_name, method="post", json=data)

    def transfer_result(
        self,
        status_filter: int = 2,
        cursor: str = None,
        limit: int = 100,
    ):
        api_name = "externalcontact/groupchat/transfer_result"
        data = {
            "status_filter": status_filter,
            "limit": limit,
        }
        if cursor:
            data["cursor"] = cursor
        return self.request(api_name=api_name, method="post", json=data)

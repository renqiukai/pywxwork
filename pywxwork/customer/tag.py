from loguru import logger
from ..base import base


class tag(base):
    def __init__(self, token: str):
        super().__init__(token)

    def list(self, tag_id: list = [], group_id: list = []):
        api_name = "externalcontact/get_corp_tag_list"
        params = {}
        if tag_id:
            params["tag_id"] = tag_id
        if group_id:
            params["group_id"] = group_id
        response = self.request(api_name=api_name, json=params, method="POST")
        
        return response

    def add(
        self,
        tag: list,
        order: int,
        group_id: int = None,
        group_name: str = None,
        agentid: str = None,
    ):
        """添加企业客户标签

        Args:
            tag (list): [标签]
            order (int): [标签组次序值。order值大的排序靠前。有效的值范围是[0, 2^32)]
            group_id (int, optional): [标签组id]. Defaults to None.
            group_name (str, optional): [标签组名称，最长为30个字符]. Defaults to None.
            agentid (str, optional): [授权方安装的应用agentid。仅旧的第三方多应用套件需要填此参数]. Defaults to None.

        Returns:
            [type]: [description]

        Example(tag):
            {
                "name": "TAG_NAME_1",
                "order": 1
            }
        """
        api_name = "externalcontact/add_corp_tag"
        params = {"order": order, "tag": tag, "agentid": 1000014}
        if group_name:
            params["group_name"] = group_name
        if agentid:
            params["agentid"] = agentid
        if group_id:
            # 有groupid表示更新组内的标签无groupid表示新建组
            params["group_id"] = group_id
        response = self.request(api_name=api_name, json=params, method="POST")
        
        return response

    def update(self, id: str, name: str = None, order: int = None, agentid: str = None):
        """编辑企业客户标签

        Args:
            id (str): 标签或标签组的id
            name (str, optional): 新的标签或标签组名称，最长为30个字符. Defaults to None.
            order (int, optional): 	标签/标签组的次序值。order值大的排序靠前。有效的值范围是[0, 2^32). Defaults to None.
            agentid (str, optional): 	授权方安装的应用agentid。仅旧的第三方多应用套件需要填此参数. Defaults to None.

        Returns:
            response: dict
        """
        api_name = "externalcontact/edit_corp_tag"
        params = {
            "id": id,
        }
        if name:
            params["name"] = name
        if agentid:
            params["agentid"] = agentid
        if order:
            params["order"] = order
        response = self.request(api_name=api_name, json=params, method="POST")
        
        return response

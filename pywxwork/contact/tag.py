from loguru import logger
from ..base import base


class tag(base):
    def __init__(self, token) -> None:
        super().__init__(token)

    def create(self, tagname: str, tagid: int = None) -> dict:
        """创建标签

        Args:
            tagname (str): 标签名称，长度限制为32个字以内（汉字或英文字母），标签名不可与其他标签重名。
            tagid (int, optional): 标签id，非负整型，指定此参数时新增的标签会生成对应的标签id，不指定时则以目前最大的id自增。. Defaults to None.

        Returns:
            dict
        """
        data = {
            "tagname": tagname,
        }
        if tagid:
            data["tagid"] = tagid
        api_name = "tag/create"
        response = self.request(api_name=api_name, method="post", json=data)
        
        return response

    def update(self, tagid: int, tagname: str) -> dict:
        """更新标签名字

        Args:
            tagid (int): 标签ID
            tagname (str): 标签名称，长度限制为32个字（汉字或英文字母），标签不可与其他标签重名。

        Returns:
            dict: 
        """
        api_name = "tag/update"
        data = {"tagid": tagid, "tagname": tagname}
        response = self.request(api_name=api_name, method="post", json=data)
        
        return response

    def delete(self, tagid: int):
        api_name = "tag/delete"
        params = {"tagid": tagid}
        response = self.request(api_name=api_name, method="get", params=params)
        
        return response

    def get(self, tagid: int):
        """获取标签成员

        Args:
            tagid (int): 标签ID
        """
        api_name = "tag/get"
        params = {"tagid": tagid}
        response = self.request(api_name=api_name, method="get", params=params)
        
        return response

    def addtagusers(
        self, tagid: int, userlist: list = [], partylist: list = []
    ) -> dict:
        """增加标签成员

        Args:
            tagid (int): 标签ID
            userlist (list, optional): 企业成员ID列表，注意：userlist、partylist不能同时为空，单次请求个数不超过1000. Defaults to [].
            partylist (list, optional): 企业部门ID列表，注意：userlist、partylist不能同时为空，单次请求个数不超过100. Defaults to [].

        Returns:
            dict: 
        """
        api_name = "tag/addtagusers"
        data = {
            "tagid": tagid,
        }
        if userlist:
            data["userlist"] = userlist
        if partylist:
            data["partylist"] = partylist
        response = self.request(api_name=api_name, method="post", json=data)
        
        return response

    def deltagusers(
        self, tagid: int, userlist: list = [], partylist: list = []
    ) -> dict:
        """删除标签成员

        Args:
            tagid (int): 标签ID
            userlist (list, optional): 企业成员ID列表，注意：userlist、partylist不能同时为空，单次请求个数不超过1000. Defaults to [].
            partylist (list, optional): 企业部门ID列表，注意：userlist、partylist不能同时为空，单次请求个数不超过100. Defaults to [].

        Returns:
            dict: 
        """
        api_name = "tag/deltagusers"
        data = {
            "tagid": tagid,
        }
        if userlist:
            data["userlist"] = userlist
        if partylist:
            data["partylist"] = partylist
        response = self.request(api_name=api_name, method="post", json=data)
        
        return response

    def list(self):
        api_name = "tag/list"
        response = self.request(api_name=api_name, method="get")
        
        return response

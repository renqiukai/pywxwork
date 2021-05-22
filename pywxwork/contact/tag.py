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
        response = self.request(
            api_name=api_name, method="post", json=data)
        logger.debug(response)
        return response

    def update(self, tagid: int, tagname: str):
        api_name = "department/update"
        data = {
            "id": id,
        }
        if name:
            data["name"] = name
        if name_en:
            data["name_en"] = name_en
        if parentid:
            data["parentid"] = parentid
        if order:
            data["order"] = order
        response = self.request(
            api_name=api_name, method="post", json=data)
        logger.debug(response)
        return response

    def delete(self, id):
        api_name = "department/delete"
        params = {
            "id": id
        }
        response = self.request(
            api_name=api_name, method="get", params=params)
        logger.debug(response)
        return response

    def list(self, id: int = None):
        """获取部门列表

        Args:
            id (int, optional): 部门id。获取指定部门及其下的子部门（以及及子部门的子部门等等，递归）。 如果不填，默认获取全量组织架构. Defaults to None.

        Returns:
            [type]: [description]
        """
        api_name = "department/list"
        params = {
            "id": id,
        }
        response = self.request(
            api_name=api_name, method="get", params=params)
        logger.debug(response)
        return response

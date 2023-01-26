from loguru import logger
from ..base import base


class department(base):
    def __init__(self, token) -> None:
        super().__init__(token)

    def create(self, data: dict):
        """创建部门
        https://open.work.weixin.qq.com/api/doc/90000/90135/90205

        Args:
            data (dict): {
                "name": "广州研发中心",
                "name_en": "RDGZ",
                "parentid": 1,
                "order": 1,
                "id": 2
                }
        Returns:
            [type]: [description]
        """
        api_name = "department/create"
        response = self.request(api_name=api_name, method="post", json=data)
        return response

    def update(
        self,
        id: int,
        name: str = None,
        name_en: str = None,
        parentid: int = None,
        order: int = None,
    ):
        """更新部门

        Args:
            id (int): 部门id
            name (str, optional): 部门名称。长度限制为1~32个字符，字符不能包括\:?”<>｜. Defaults to None.
            name_en (str, optional): 英文名称，需要在管理后台开启多语言支持才能生效。长度限制为1~32个字符，字符不能包括\:?”<>｜. Defaults to None.
            parentid (int, optional): 父部门id. Defaults to None.
            order (int, optional): 在父部门中的次序值。order值大的排序靠前。有效的值范围是[0, 2^32). Defaults to None.

        Returns:
            [type]: [description]
        """
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
        response = self.request(api_name=api_name, method="post", json=data)
        return response

    def delete(self, id):
        api_name = "department/delete"
        params = {"id": id}
        response = self.request(api_name=api_name, method="get", params=params)
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
        response = self.request(api_name=api_name, method="get", params=params)
        return response

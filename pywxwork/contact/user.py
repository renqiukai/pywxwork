from loguru import logger
from ..base import base

class user(base):
    def __init__(self, token) -> None:
        super().__init__(token)

    def create(self, data):
        api_name = "user/create"
        response = self.request(
            api_name=api_name, method="post", json=data)
        logger.debug(response)
        return response

    def get(self, userid):
        api_name = "user/get"
        params = {
            "userid": userid
        }
        response = self.request(
            api_name=api_name, method="get", params=params)
        logger.debug(response)
        return response

    def update(self, data):
        api_name = "user/update"
        response = self.request(
            api_name=api_name, method="post", json=data)
        logger.debug(response)
        return response

    def delete(self, userid):
        api_name = "user/delete"
        params = {
            "userid": userid
        }
        response = self.request(
            api_name=api_name, method="get", params=params)
        logger.debug(response)
        return response

    def batchdelete(self, useridlist):
        api_name = "user/batchdelete"
        params = {
            "useridlist": useridlist
        }
        response = self.request(
            api_name=api_name, method="post", params=params)
        logger.debug(response)
        return response

    def simplelist(self, department_id, fetch_child=0):
        """获取部门成员

        Args:
            department_id (int): department id
            fetch_child (int, optional): 是否递归获取子部门下面的成员：1-递归获取，0-只获取本部门. Defaults to 0.

        Returns:
            dict: member
        """        
        api_name = "user/simplelist"
        params = {
            "department_id": department_id,
            "fetch_child": fetch_child
        }
        response = self.request(
            api_name=api_name, method="get", params=params)
        logger.debug(response)
        return response

    def list(self, department_id, fetch_child=0):
        # get department member.
        # fetch_child
        # 是否递归获取子部门下面的成员：1-递归获取，0-只获取本部门
        api_name = "user/list"
        params = {
            "department_id": department_id,
            "fetch_child": fetch_child
        }
        response = self.request(
            api_name=api_name, method="get", params=params)
        logger.debug(response)
        return response

    def convert_to_openid(self, userid):
        api_name = "user/convert_to_openid"
        params = {
            "userid": userid
        }
        response = self.request(
            api_name=api_name, method="post", params=params)
        logger.debug(response)
        return response

    def convert_to_userid(self, openid):
        api_name = "user/convert_to_userid"
        params = {
            "openid": openid
        }
        response = self.request(
            api_name=api_name, method="post", params=params)
        logger.debug(response)
        return response

    def get_user_info(self, code):
        api_name = "user/getuserinfo"
        params = {
            "code": code
        }
        response = self.request(
            api_name=api_name, method="get", params=params)
        logger.debug(response)
        return response

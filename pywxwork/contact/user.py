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

    def get_user_detail(self, user_ticket):
        api_name = "auth/getuserdetail"
        params = {
            "user_ticket": user_ticket
        }
        response = self.request(
            api_name=api_name, method="post", json=params)
        logger.debug(response)
        return response

    def authsucc(self, userid):
        api_name = "user/authsucc"
        params = {
            "userid": userid
        }
        response = self.request(
            api_name=api_name, method="get", params=params)
        logger.debug(response)
        return response

    def invite(self, user_list: list = [], party_list: list = [], tag_list: list = []):
        """邀请成员
        企业可通过接口批量邀请成员使用企业微信，邀请后将通过短信或邮件下发通知。
        https://open.work.weixin.qq.com/api/doc/90000/90135/90975


        Args:
            user_list (list, optional): 成员ID列表, 最多支持1000个。. Defaults to [].
            party_list (list, optional): 部门ID列表，最多支持100个。. Defaults to [].
            tag_list (list, optional): 标签ID列表，最多支持100个。. Defaults to [].

        Returns:
            [type]: [description]
        """
        api_name = "batch/invite"
        data = {}
        if user_list:
            data["user"] = user_list
        if party_list:
            data["party"] = party_list
        if tag_list:
            data["tag"] = tag_list

        response = self.request(
            api_name=api_name, method="post", json=data)
        logger.debug(response)
        return response

    def get_join_qrcode(self, size_type: int = None):
        """获取加入企业二维码

        Args:
            size_type (int, optional): qrcode尺寸类型，1: 171 x 171; 2: 399 x 399; 3: 741 x 741; 4: 2052 x 2052. Defaults to None.

        Returns:
            [type]: [description]
        """
        api_name = "corp/get_join_qrcode"
        if size_type:
            params = {
                "size_type": size_type
            }
        response = self.request(
            api_name=api_name, method="get", params=params)
        logger.debug(response)
        return response

    def get_active_stat(self, date: str):
        api_name = "user/get_active_stat"
        data = {
            "date": date
        }
        response = self.request(
            api_name=api_name, method="post", json=data)
        logger.debug(response)
        return response

    def getuserid(self, mobile: str):
        api_name = "user/getuserid"
        data = {
            "mobile": mobile
        }
        response = self.request(
            api_name=api_name, method="post", json=data)
        logger.debug(response)
        return response

    def get_userid_by_email(self, email: str, email_type: str = 1):
        api_name = "user/get_userid_by_email"
        data = {
            "email": email,
            "email_type": email_type,
        }
        response = self.request(
            api_name=api_name, method="post", json=data)
        logger.debug(response)
        return response

    def list_id(self, cursor: str = None, limit: int = 10000):
        api_name = "user/list_id"
        data = {
            "cursor": cursor,
            "limit": limit,
        }
        response = self.request(
            api_name=api_name, method="post", json=data)
        logger.debug(response)
        return response

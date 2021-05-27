from loguru import logger
from ..base import base


class customer(base):
    def __init__(self, token: str):
        super().__init__(token)

    def get_follow_user_list(self):
        api_name = "externalcontact/get_follow_user_list"
        response = self.request(
            api_name=api_name, method="get")
        logger.debug(response)
        return response

    def list(self, userid):
        api_name = "externalcontact/list"
        params = {
            "userid": userid
        }
        response = self.request(
            api_name=api_name,
            params=params,
            method="get")
        logger.debug(response)
        return response

    def get(self, external_userid: str, cursor: str = None):
        api_name = "externalcontact/get"
        params = {
            "external_userid": external_userid
        }
        if cursor:
            params["cursor"] = cursor

        response = self.request(
            api_name=api_name,
            params=params,
            method="get")
        logger.debug(response)
        return response

    def batch_get(self, userid: str, cursor: str = None, limit: int = None):
        api_name = "externalcontact/batch/get_by_user"
        params = {
            "userid": userid,
        }
        if cursor:
            params["cursor"] = cursor
        if limit:
            params["limit"] = limit
        response = self.request(
            api_name=api_name,
            json=params,
            method="post")
        logger.debug(response)
        return response

    def remark(self, userid: str, external_userid: str,
               remark: str = None, description: str = None, remark_company: str = None,
               remark_mobiles: str = None, remark_pic_mediaid: str = None,):
        api_name = "externalcontact/remark"
        params = {
            "userid": userid,
            "external_userid": external_userid,
        }
        if remark:
            params["remark"] = remark
        if description:
            params["description"] = description
        if remark_company:
            params["remark_company"] = remark_company
        if remark_mobiles:
            params["remark_mobiles"] = remark_mobiles
        if remark_pic_mediaid:
            params["remark_pic_mediaid"] = remark_pic_mediaid
        response = self.request(
            api_name=api_name,
            json=params,
            method="post")
        logger.debug(response)
        return response

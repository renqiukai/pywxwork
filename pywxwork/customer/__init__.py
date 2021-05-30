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

    def add_contact_way(self, data):
        """
        配置客户联系「联系我」方式
        """
        api_name = "externalcontact/add_contact_way"
        response = self.request(
            api_name=api_name, method="post", json=data)
        logger.debug(response)
        return response

    def add_contact_way_demo(self):
        data = {
            "type": 1,
            "scene": 1,
            "style": 1,
            "remark": "渠道客户",
            "skip_verify": True,
            "state": "teststate",
            "user": ["zhangsan", "lisi", "wangwu"],
            "party": [2, 3],
            "is_temp": True,
            "expires_in": 86400,
            "chat_expires_in": 86400,
            "unionid": "oxTWIuGaIt6gTKsQRLau2M0AAAA",
            "conclusions":
            {
                "text":
                {
                    "content": "文本消息内容"
                },
                "image":
                {
                    "media_id": "MEDIA_ID"
                },
                "link":
                {
                    "title": "消息标题",
                    "picurl": "https://example.pic.com/path",
                    "desc": "消息描述",
                    "url": "https://example.link.com/path"
                },
                "miniprogram":
                {
                    "title": "消息标题",
                    "pic_media_id": "MEDIA_ID",
                    "appid": "wx8bd80126147dfAAA",
                    "page": "/path/index.html"
                }
            }
        }

        response = self.add_contact_way(data)
        logger.debug(response)
        return response

    def get_contact_way(self, config_id):
        """
        获取企业已配置的「联系我」方式
        """
        api_name = "externalcontact/get_contact_way"
        data = {
            "config_id": config_id
        }
        response = self.request(
            api_name=api_name, method="post", json=data)
        logger.debug(response)
        return response

    def update_contact_way(self, data):
        """
        更新企业已配置的「联系我」方式
        """
        api_name = "externalcontact/update_contact_way"
        response = self.request(
            api_name=api_name, method="post", json=data)
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

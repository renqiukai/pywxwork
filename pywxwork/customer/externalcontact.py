from loguru import logger
from ..base import base


class externalContact(base):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class followUser(externalContact):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

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

    def update_contact_way_demo(self):
        """
        更新企业已配置的「联系我」方式
        """
        data = {
            "config_id": "42b34949e138eb6e027c123cba77fAAA",
            "remark": "渠道客户",
            "skip_verify": True,
            "style": 1,
            "state": "teststate",
            "user": ["zhangsan", "lisi", "wangwu"],
            "party": [2, 3],
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
                    "page": "/path/index"
                }
            }
        }

        response = self.update_contact_way(data)
        logger.debug(response)
        return response

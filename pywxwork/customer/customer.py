from loguru import logger
from ..base import base


class customer(base):
    def __init__(self, token: str):
        super().__init__(token)

    def get_follow_user_list(self):
        """
        获取配置了客户联系功能的成员列表
        """
        api_name = "externalcontact/get_follow_user_list"
        response = self.request(api_name=api_name, method="get")

        return response

    def add_contact_way(self, data):
        """
        配置客户联系「联系我」方式
        """
        api_name = "externalcontact/add_contact_way"
        response = self.request(api_name=api_name, method="post", json=data)

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
            "conclusions": {
                "text": {"content": "文本消息内容"},
                "image": {"media_id": "MEDIA_ID"},
                "link": {
                    "title": "消息标题",
                    "picurl": "https://example.pic.com/path",
                    "desc": "消息描述",
                    "url": "https://example.link.com/path",
                },
                "miniprogram": {
                    "title": "消息标题",
                    "pic_media_id": "MEDIA_ID",
                    "appid": "wx8bd80126147dfAAA",
                    "page": "/path/index.html",
                },
            },
        }

        response = self.add_contact_way(data)

        return response

    def get_contact_way(self, config_id):
        """
        获取企业已配置的「联系我」方式
        """
        api_name = "externalcontact/get_contact_way"
        data = {"config_id": config_id}
        response = self.request(api_name=api_name, method="post", json=data)

        return response

    def update_contact_way(self, data):
        """
        更新企业已配置的「联系我」方式
        """
        api_name = "externalcontact/update_contact_way"
        response = self.request(api_name=api_name, method="post", json=data)

        return response

    def list(self, userid):
        """
        获取客户列表
        """
        api_name = "externalcontact/list"
        params = {"userid": userid}
        response = self.request(api_name=api_name, params=params, method="get")

        return response

    def get(self, external_userid: str, cursor: str = None):
        """
        获取客户详情
        """
        api_name = "externalcontact/get"
        params = {"external_userid": external_userid}
        if cursor:
            params["cursor"] = cursor

        response = self.request(api_name=api_name, params=params, method="get")

        return response

    def batch_get(self, userid_list: str, cursor: str = None, limit: int = 100):
        """
        批量获取客户详情
        """
        api_name = "externalcontact/batch/get_by_user"
        params = {
            "userid_list": userid_list,
        }
        if cursor:
            params["cursor"] = cursor
        if limit:
            params["limit"] = limit
        response = self.request(api_name=api_name, json=params, method="post")

        return response

    def remark(
        self,
        userid: str,
        external_userid: str,
        remark: str = None,
        description: str = None,
        remark_company: str = None,
        remark_mobiles: str = None,
        remark_pic_mediaid: str = None,
    ):
        """
        修改客户备注信息
        """
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
        response = self.request(api_name=api_name, json=params, method="post")

        return response

    def get_all_customer(self, userid_list: list):
        """
        取得全量的客户信息
        """
        start = 0
        for i in range(int(len(userid_list) / 100) + 1):
            # 循环多次加载
            end = start + 100
            next_cursor = None
            while 1:
                resp = self.batch_get(userid_list[start:end], next_cursor)
                rows = resp.get("external_contact_list")
                next_cursor = resp.get("next_cursor")
                yield rows
                if not next_cursor:
                    # 没有cursor表示客户列表到底了
                    break
            start = end + 1

    def customer_strategy_list(self, limit: int = 1000, cursor: str = None):
        """
        获取规则组列表
        """
        api_name = "customer_strategy/list"
        params = {"cursor": cursor, "limit": limit}
        if cursor:
            params["cursor"] = cursor
        response = self.request(api_name=api_name, json=params, method="post")
        return response

    def customer_strategy_get(self, strategy_id: str):
        """
        获取规则组详情
        """
        api_name = "customer_strategy/get"
        params = {"strategy_id": strategy_id}
        response = self.request(api_name=api_name, json=params, method="post")
        return response

    def send_welcome_msg(self, data):
        """发送新客户欢迎语"""
        api_name = "externalcontact/send_welcome_msg"
        response = self.request(api_name=api_name, method="post", json=data)
        return response

    def transfer_customer(
        self,
        external_userid: list,
        handover_userid: str,
        takeover_userid: str,
        transfer_success_msg: bool = True,
    ):
        """在职成员分配客户"""
        api_name = "externalcontact/transfer_customer"
        data = {
            "external_userid": external_userid,
            "handover_userid": handover_userid,
            "takeover_userid": takeover_userid,
            "transfer_success_msg": transfer_success_msg,
        }
        response = self.request(api_name=api_name, method="post", json=data)
        return response

    def transfer_result(
        self,
        handover_userid: str,
        takeover_userid: str,
        cursor: str = None,
        limit: int = 100,
    ):
        """查询在职成员分配结果"""
        api_name = "externalcontact/transfer_result"
        data = {
            "handover_userid": handover_userid,
            "takeover_userid": takeover_userid,
            "limit": limit,
        }
        if cursor:
            data["cursor"] = cursor
        response = self.request(api_name=api_name, method="post", json=data)
        return response

    def resigned_transfer_customer(
        self,
        external_userid: list,
        handover_userid: str,
        takeover_userid: str,
        transfer_success_msg: bool = True,
    ):
        """离职成员客户继承"""
        api_name = "externalcontact/resigned/transfer_customer"
        data = {
            "external_userid": external_userid,
            "handover_userid": handover_userid,
            "takeover_userid": takeover_userid,
            "transfer_success_msg": transfer_success_msg,
        }
        response = self.request(api_name=api_name, method="post", json=data)
        return response

    def resigned_transfer_result(
        self,
        handover_userid: str,
        takeover_userid: str,
        cursor: str = None,
        limit: int = 100,
    ):
        """查询离职成员客户继承结果"""
        api_name = "externalcontact/resigned/transfer_result"
        data = {
            "handover_userid": handover_userid,
            "takeover_userid": takeover_userid,
            "limit": limit,
        }
        if cursor:
            data["cursor"] = cursor
        response = self.request(api_name=api_name, method="post", json=data)
        return response

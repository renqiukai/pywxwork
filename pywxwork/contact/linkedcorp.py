from loguru import logger
from ..base import base


class linkedcorp(base):
    def __init__(self, token) -> None:
        super().__init__(token)

    def get_perm_list(self):
        """获取应用的可见范围
        https://open.work.weixin.qq.com/api/doc/90000/90135/93172
        """
        api_name = "linkedcorp/agent/get_perm_list"
        response = self.request(
            api_name=api_name, method="post")
        logger.debug(response)
        return response

    def get_user(self, userid):
        """获取互联企业成员详细信息
        https://open.work.weixin.qq.com/api/doc/90000/90135/93171
        userid:"CORPID/USERID"
        """
        api_name = "linkedcorp/user/get"
        data = {
            "userid": userid
        }
        response = self.request(
            api_name=api_name, json=data, method="post")
        logger.debug(response)
        return response

    def get_department_user(self, department_id, fetch_child=None):
        """获取互联企业部门成员
        https://open.work.weixin.qq.com/api/doc/90000/90135/93168
        department_id 该字段用的是互联应用可见范围接口返回的department_ids参数，用的是 linkedid + ’/‘ + department_id 拼成的字符串
        fetch_child 是否递归获取子部门下面的成员：1-递归获取，0-只获取本部门，不传默认只获取本部门成员
        """
        api_name = "linkedcorp/user/simplelist"
        data = {
            "department_id": department_id,
        }
        if fetch_child:
            data["fetch_child"] = fetch_child
        response = self.request(
            api_name=api_name, method="post", json=data)
        logger.debug(response)
        return response

    def get_department_user_detail(self, department_id, fetch_child=None):
        """获取互联企业部门成员详情
        https://open.work.weixin.qq.com/api/doc/90000/90135/93169
        department_id 该字段用的是互联应用可见范围接口返回的department_ids参数，用的是 linkedid + ’/‘ + department_id 拼成的字符串
        fetch_child 是否递归获取子部门下面的成员：1-递归获取，0-只获取本部门，不传默认只获取本部门成员
        """
        api_name = "linkedcorp/user/list"
        data = {
            "department_id": department_id,
        }
        if fetch_child:
            data["fetch_child"] = fetch_child
        response = self.request(
            api_name=api_name, method="post", json=data)
        logger.debug(response)
        return response

    def get_department(self, department_id):
        """获取互联企业部门列表
        https://open.work.weixin.qq.com/api/doc/90000/90135/93170
        department_id 该字段用的是互联应用可见范围接口返回的department_ids参数，用的是 linkedid + ’/‘ + department_id 拼成的字符串
        """
        api_name = "linkedcorp/department/list"
        data = {
            "department_id": department_id
        }
        response = self.request(
            api_name=api_name, method="post", json=data)
        logger.debug(response)
        return response

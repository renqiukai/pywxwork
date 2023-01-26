from ..base import base
from loguru import logger


class appchat(base):
    def __init__(self, token: str):
        super().__init__(token)

    def create(
        self, userlist: list, name: str = None, owner: str = None, chatid: str = None
    ):
        """创建群聊会话

        Args:
            userlist (list): 	群成员id列表。至少2人，至多2000人
            name (str, optional): 群聊名，最多50个utf8字符，超过将截断. Defaults to None.
            owner (str, optional): 指定群主的id。如果不指定，系统会随机从userlist中选一人作为群主. Defaults to None.
            chatid (str, optional): 	群聊的唯一标志，不能与已有的群重复；字符串类型，最长32个字符。只允许字符0-9及字母a-zA-Z。如果不填，系统会随机生成群id. Defaults to None.
        """
        api_name = "appchat/create"
        data = {
            "userlist": userlist,
        }
        if name:
            data["name"] = name
        if owner:
            data["owner"] = owner
        if chatid:
            data["chatid"] = chatid
        response = self.request(api_name=api_name, method="POST", json=data,)
        
        return response

    def update(
        self,
        chatid: int,
        name: str = None,
        owner: str = None,
        add_user_list: list = [],
        del_user_list: list = [],
    ):
        """修改群聊会话
        https://open.work.weixin.qq.com/api/doc/90000/90135/90246
        Args:
            chatid (int): 群聊id
            name (str, optional): 	新的群聊名。若不需更新，请忽略此参数。最多50个utf8字符，超过将截断. Defaults to None.
            owner (str, optional): 新群主的id。若不需更新，请忽略此参数. Defaults to None.
            add_user_list (list, optional): 添加成员的id列表. Defaults to [].
            del_user_list (list, optional): 踢出成员的id列表. Defaults to [].
        """
        api_name = "appchat/update"
        data = {
            "chatid": chatid,
        }
        if name:
            data["name"] = name
        if owner:
            data["owner"] = owner
        if add_user_list:
            data["add_user_list"] = add_user_list
        if del_user_list:
            data["del_user_list"] = del_user_list
        response = self.request(api_name=api_name, method="POST", json=data,)
        
        return response

    def get(self, chatid: int):
        """获取群聊会话
        https://open.work.weixin.qq.com/api/doc/90000/90135/90247
        Args:
            chatid (int): 群聊id
        """
        api_name = "appchat/get"
        data = {
            "chatid": chatid,
        }
        response = self.request(api_name=api_name, method="get", params=data,)
        
        return response

    def send_text(self, chatid: str, content: str, safe: int = 0):
        api_name = "appchat/send"
        data = {
            "chatid": chatid,
            "msgtype": "text",
            "text": {"content": content},
            "safe": safe,
        }
        response = self.request(api_name=api_name, method="post", json=data,)
        
        return response

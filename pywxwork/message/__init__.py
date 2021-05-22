from ..base import base
from loguru import logger


class message(base):

    def __init__(self, token: str):
        super().__init__(token)

    def send(self, agentid: int, msgtype: str, send_content: dict, touser: list = [], toparty: list = [], totag: list = [],
             safe: int = 0, enable_id_trans: int = None, enable_duplicate_check: int = 0, duplicate_check_interval: int = 1800,
             content_type=None):
        api_name = "message/send"
        if not content_type:
            content_type = msgtype
        data = {
            "msgtype": msgtype,
            "agentid": agentid,
            content_type: send_content,
            "safe": safe,
            "enable_id_trans": enable_id_trans,
            "enable_duplicate_check": enable_duplicate_check,
            "duplicate_check_interval": duplicate_check_interval
        }
        if enable_id_trans:
            data["enable_id_trans"] = enable_id_trans

        if touser:
            touser = "|".join(touser)
            data["touser"] = touser
        if toparty:
            toparty = "|".join(toparty)
            data["toparty"] = toparty
        if totag:
            totag = "|".join(totag)
            data["totag"] = totag
        response = self.request(
            api_name=api_name,
            method="post",
            json=data,
        )
        logger.debug(response)
        return response

    def send_text(self, agentid: int, content: str, touser: list = [], toparty: list = [], totag: list = [],
                  safe: int = 0, enable_id_trans: int = 0, enable_duplicate_check: int = 0, duplicate_check_interval: int = 1800,
                  ):
        response = self.send(
            agentid=agentid,
            msgtype="text",
            send_content={"content": content},
            touser=touser,
            toparty=toparty,
            totag=totag,
            safe=safe,
            enable_id_trans=enable_id_trans,
            enable_duplicate_check=enable_duplicate_check,
            duplicate_check_interval=duplicate_check_interval,
        )
        logger.debug(response)
        return response

    def send_image(self, agentid: int, media_id: str, touser: list = [], toparty: list = [], totag: list = [],
                   safe: int = 0, enable_duplicate_check: int = 0, duplicate_check_interval: int = 1800,
                   ):
        response = self.send(
            agentid=agentid,
            msgtype="image",
            send_content={"image": media_id},
            touser=touser,
            toparty=toparty,
            totag=totag,
            safe=safe,
            enable_duplicate_check=enable_duplicate_check,
            duplicate_check_interval=duplicate_check_interval,
        )
        logger.debug(response)
        return response

    def send_voice(self, agentid: int, media_id: str, touser: list = [], toparty: list = [], totag: list = [],
                   safe: int = 0, enable_duplicate_check: int = 0, duplicate_check_interval: int = 1800,
                   ):
        response = self.send(
            agentid=agentid,
            msgtype="voice",
            send_content={"voice": media_id},
            touser=touser,
            toparty=toparty,
            totag=totag,
            safe=safe,
            enable_duplicate_check=enable_duplicate_check,
            duplicate_check_interval=duplicate_check_interval,
        )
        logger.debug(response)
        return response

    def send_video(self, agentid: int, media_id: str, touser: list = [], toparty: list = [], totag: list = [],
                   safe: int = 0, enable_duplicate_check: int = 0, duplicate_check_interval: int = 1800,
                   ):
        response = self.send(
            agentid=agentid,
            msgtype="video",
            send_content={"video": media_id},
            touser=touser,
            toparty=toparty,
            totag=totag,
            safe=safe,
            enable_duplicate_check=enable_duplicate_check,
            duplicate_check_interval=duplicate_check_interval,
        )
        logger.debug(response)
        return response

    def send_file(self, agentid: int, media_id: str, touser: list = [], toparty: list = [], totag: list = [],
                  safe: int = 0, enable_duplicate_check: int = 0, duplicate_check_interval: int = 1800,
                  ):
        response = self.send(
            agentid=agentid,
            msgtype="file",
            send_content={"file": media_id},
            touser=touser,
            toparty=toparty,
            totag=totag,
            safe=safe,
            enable_duplicate_check=enable_duplicate_check,
            duplicate_check_interval=duplicate_check_interval,
        )
        logger.debug(response)
        return response

    def send_textcard(self, agentid: int, title: str, description: str, url: str, btntxt: str, touser: list = [], toparty: list = [], totag: list = [],
                      safe: int = 0, enable_id_trans=0, enable_duplicate_check: int = 0, duplicate_check_interval: int = 1800,
                      ):
        response = self.send(
            agentid=agentid,
            msgtype="textcard",
            send_content={
                "title": title,
                "description": description,
                "url": url,
                "btntxt": btntxt,
            },
            touser=touser,
            toparty=toparty,
            totag=totag,
            safe=safe,
            enable_id_trans=enable_id_trans,
            enable_duplicate_check=enable_duplicate_check,
            duplicate_check_interval=duplicate_check_interval,
        )
        logger.debug(response)
        return response

    def send_news(self, agentid: int, articles: list, touser: list = [], toparty: list = [], totag: list = [],
                  safe: int = 0, enable_id_trans=0, enable_duplicate_check: int = 0, duplicate_check_interval: int = 1800,
                  ):
        """图文消息

        Args:
            agentid (int): [description]
            articles (list): [{
               "title" : "中秋节礼品领取",
               "description" : "今年中秋节公司有豪礼相送",
               "url" : "URL",
               "picurl" : "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
           }]
            touser (list, optional): [description]. Defaults to [].
            toparty (list, optional): [description]. Defaults to [].
            totag (list, optional): [description]. Defaults to [].
            safe (int, optional): [description]. Defaults to 0.
            enable_id_trans (int, optional): [description]. Defaults to 0.
            enable_duplicate_check (int, optional): [description]. Defaults to 0.
            duplicate_check_interval (int, optional): [description]. Defaults to 1800.

        Returns:
            [type]: [description]
        """
        response = self.send(
            agentid=agentid,
            msgtype="news",
            send_content={"articles": articles},
            touser=touser,
            toparty=toparty,
            totag=totag,
            safe=safe,
            enable_id_trans=enable_id_trans,
            enable_duplicate_check=enable_duplicate_check,
            duplicate_check_interval=duplicate_check_interval,
        )
        logger.debug(response)
        return response

    def send_mp_news(self, agentid: int, articles: list, touser: list = [], toparty: list = [], totag: list = [],
                     safe: int = 0, enable_id_trans=0, enable_duplicate_check: int = 0, duplicate_check_interval: int = 1800,
                     ):
        """图文消息(mpnews)

        mpnews类型的图文消息，跟普通的图文消息一致，唯一的差异是图文内容存储在企业微信。
        多次发送mpnews，会被认为是不同的图文，阅读、点赞的统计会被分开计算。

        Args:
            agentid (int): [description]
            articles (list): [ {
               "title": "Title", 
               "thumb_media_id": "MEDIA_ID",
               "author": "Author",
               "content_source_url": "URL",
               "content": "Content",
               "digest": "Digest description"
            }]
            touser (list, optional): [description]. Defaults to [].
            toparty (list, optional): [description]. Defaults to [].
            totag (list, optional): [description]. Defaults to [].
            safe (int, optional): [description]. Defaults to 0.
            enable_id_trans (int, optional): [description]. Defaults to 0.
            enable_duplicate_check (int, optional): [description]. Defaults to 0.
            duplicate_check_interval (int, optional): [description]. Defaults to 1800.

        Returns:
            [type]: [description]
        """
        response = self.send(
            agentid=agentid,
            msgtype="mpnews",
            send_content={"articles": articles},
            touser=touser,
            toparty=toparty,
            totag=totag,
            safe=safe,
            enable_id_trans=enable_id_trans,
            enable_duplicate_check=enable_duplicate_check,
            duplicate_check_interval=duplicate_check_interval,
        )
        logger.debug(response)
        return response

    def send_markdown(self, agentid: int, content: str, touser: list = [], toparty: list = [], totag: list = [],
                      safe: int = 0, enable_id_trans=0, enable_duplicate_check: int = 0, duplicate_check_interval: int = 1800,
                      ):
        response = self.send(
            agentid=agentid,
            msgtype="markdown",
            send_content={"content": content},
            touser=touser,
            toparty=toparty,
            totag=totag,
            safe=safe,
            enable_id_trans=enable_id_trans,
            enable_duplicate_check=enable_duplicate_check,
            duplicate_check_interval=duplicate_check_interval,
        )
        logger.debug(response)
        return response

    def send_miniprogram_notice(self, agentid: int, send_content: dict, touser: list = [], toparty: list = [], totag: list = [],
                                safe: int = 0, enable_id_trans=0, enable_duplicate_check: int = 0, duplicate_check_interval: int = 1800,
                                ):
        """小程序通知消息

        Args:
            agentid (int): [description]
            send_content (dict): {
                "appid": "wx123123123123123",
                "page": "pages/index?userid=zhangsan&orderid=123123123",
                "title": "会议室预订成功通知",
                "description": "4月27日 16:16",
                "emphasis_first_item": true,
                "content_item": [
                    {
                        "key": "会议室",
                        "value": "402"
                    },
                    {
                        "key": "会议地点",
                        "value": "广州TIT-402会议室"
                    },
                    {
                        "key": "会议时间",
                        "value": "2018年8月1日 09:00-09:30"
                    },
                    {
                        "key": "参与人员",
                        "value": "周剑轩"
                    }
                ]
            }
            touser (list, optional): [description]. Defaults to [].
            toparty (list, optional): [description]. Defaults to [].
            totag (list, optional): [description]. Defaults to [].
            safe (int, optional): [description]. Defaults to 0.
            enable_id_trans (int, optional): [description]. Defaults to 0.
            enable_duplicate_check (int, optional): [description]. Defaults to 0.
            duplicate_check_interval (int, optional): [description]. Defaults to 1800.

        Returns:
            [type]: [description]
        """
        response = self.send(
            agentid=agentid,
            msgtype="miniprogram_notice",
            send_content=send_content,
            touser=touser,
            toparty=toparty,
            totag=totag,
            safe=safe,
            enable_id_trans=enable_id_trans,
            enable_duplicate_check=enable_duplicate_check,
            duplicate_check_interval=duplicate_check_interval,
        )
        logger.debug(response)
        return response

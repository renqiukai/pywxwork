import requests
from loguru import logger


def upload_file(key, filename, file_path=None, file_url=None):
    if not (file_path or file_url):
        raise ValueError("文件路径和文件url必须要有一个")
    if file_url:
        resp = requests.get(file_url)
        files = {"file": (f"{filename}", resp.content)}
    if file_path:
        files = {"file": (f"{filename}", open(file_path, "rb"))}

    url = (
        f"https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={key}&type=file"
    )
    logger.debug(dict(msg="正在请求的url:", url=url))
    logger.debug(dict(msg="正在请求的参数:", files=files))
    response = requests.request(
        method="POST",
        url=url,
        files=files,
    )
    if response.status_code == 200:
        errcode = response.json().get("errcode")
        if errcode != 0:
            logger.error(
                {
                    "msg": "请求错误",
                    "data": response.json(),
                }
            )
        return response.json()
    logger.error(
        {
            "msg": "请求错误",
            "data": response.json(),
        }
    )


class webHook:
    def __init__(self, key: str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"
        self.url = url

    def request(self, method="POST", **kwargs):
        logger.debug(dict(msg="正在请求的url:", url=self.url))
        logger.debug(dict(msg="正在请求的参数:", kwargs=kwargs))

        response = requests.request(
            method=method,
            url=self.url,
            **kwargs,
        )
        if response.status_code == 200:
            return self.response(response.json())
        logger.error(
            {
                "msg": "请求错误",
                "data": response.json(),
            }
        )

    def response(self, data):
        errcode = data.get("errcode")
        if errcode != 0:
            logger.error(
                {
                    "msg": "请求错误",
                    "data": data,
                }
            )
        else:
            logger.debug(dict(msg="返回值", response=data))
        return data

    def send_text(
        self, content: str, mentioned_list=["@all"], mentioned_mobile_list=["@all"]
    ):
        data = {
            "msgtype": "text",
            "text": {
                "content": content,
                "mentioned_list": mentioned_list,
                "mentioned_mobile_list": mentioned_mobile_list,
            },
        }
        response = self.request(json=data)
        return response

    def send_markdown(self, content: str):
        data = {"msgtype": "markdown", "markdown": {"content": content}}

        response = self.request(json=data)
        return response

    def send_image(self, base64: str, md5: str):
        data = {"msgtype": "image", "image": {"base64": base64, "md5": md5}}

        response = self.request(json=data)
        return response

    def make_article(self, title, description, url, picurl):
        return {
            "title": title,
            "description": description,
            "url": url,
            "picurl": picurl,
        }

    def send_news(self, articles=[]):
        data = {"msgtype": "news", "news": {"articles": articles}}

        response = self.request(json=data)
        return response

    def send_file(self, media_id: str):
        data = {"msgtype": "file", "file": {"media_id": media_id}}
        response = self.request(json=data)
        return response

    def send_template_card(self, template_card=None):
        # todo:未能完成模板消息的发送代码
        data = {
            "msgtype": "template_card",
            "template_card": {
                "card_type": "news_notice",
                "source": {
                    "icon_url": "https://wework.qpic.cn/wwpic/252813_jOfDHtcISzuodLa_1629280209/0",
                    "desc": "美女直播",
                    "desc_color": 0,
                },
                "main_title": {"title": "欢迎使用每日大赛", "desc": "您的好友正在邀请您一起观看"},
                "card_image": {
                    "url": "https://wework.qpic.cn/wwpic/354393_4zpkKXd7SrGMvfg_1629280616/0",
                    "aspect_ratio": 2.25,
                },
                "image_text_area": {
                    "type": 1,
                    "url": "https://work.weixin.qq.com",
                    "title": "欢迎使用企业微信",
                    "desc": "您的好友正在邀请您加入企业微信",
                    "image_url": "https://wework.qpic.cn/wwpic/354393_4zpkKXd7SrGMvfg_1629280616/0",
                },
                "quote_area": {
                    "type": 1,
                    "url": "https://work.weixin.qq.com/?from=openApi",
                    "appid": "ww8f56cd087a516509",
                    "pagepath": "PAGEPATH",
                    "title": "引用文本标题",
                    "quote_text": "Jack：企业微信真的很好用~\nBalian：超级好的一款软件！",
                },
                "vertical_content_list": [
                    {"title": "惊喜红包等你来拿", "desc": "下载企业微信还能抢红包！"}
                ],
                "horizontal_content_list": [
                    {"keyname": "邀请人", "value": "张三"},
                    {
                        "keyname": "企微官网",
                        "value": "点击访问",
                        "type": 1,
                        "url": "https://work.weixin.qq.com/?from=openApi",
                    },
                ],
                "jump_list": [
                    {
                        "type": 1,
                        "url": "https://work.weixin.qq.com/?from=openApi",
                        "title": "企业微信官网",
                    },
                    # {
                    #     "type": 2,
                    #     "appid": "ww8f56cd087a516509",
                    #     "pagepath": "PAGEPATH",
                    #     "title": "跳转小程序"
                    # }
                ],
                "card_action": {
                    "type": 1,
                    "url": "https://work.weixin.qq.com/?from=openApi",
                    "appid": "ww8f56cd087a516509",
                    "pagepath": "PAGEPATH",
                },
            },
        }

        response = self.request(json=data)
        return response

from ..base import base
from loguru import logger


class calendar(base):
    def __init__(self, token: str):
        super().__init__(token)

    def add(
        self,
        organizer,
        summary,
        color="#0000FF",
        description="",
        shares=[],
        readonly=1,
        set_as_default=0,
        agentid=None,
    ):
        """添加日历
        https://open.work.weixin.qq.com/api/doc/90000/90135/93647

        Args:
            organizer (str): 指定的组织者userid。注意该字段指定后不可更新
            summary (str): 日历标题。1 ~ 128 字符
            color (str): 日历在终端上显示的颜色，RGB颜色编码16进制表示，例如：”#0000FF” 表示纯蓝色
            description (str, optional): 日历描述。. Defaults to "".
            shares (list, optional): 日历共享成员列表。最多2000人. Defaults to [].
                {
                    "userid" : "userid2",
                    "readonly" : 1
                }
            readonly (int, optional): [description]. Defaults to 1.
            set_as_default (int, optional): 是否将该日历设置为组织者的默认日历。
                                            0-否；1-是。默认为0，即不设为默认日历
                                            第三方应用不支持使用该参数. Defaults to 0.
            agentid ([type], optional): 授权方安装的应用agentid。仅旧的第三方多应用套件需要填此参数. Defaults to None.

        Returns:
            dict: 
        """
        api_name = "oa/calendar/add"
        data = {
            "calendar": {
                "organizer": organizer,
                "readonly": readonly,
                "set_as_default": set_as_default,
                "summary": summary,
                "color": color,
                "description": description,
                "shares": shares,
            },
        }
        if agentid:
            data["agentid"] = agentid
        response = self.request(api_name=api_name, method="post", json=data,)
        return response

    def update(
        self,
        cal_id,
        organizer,
        summary,
        color="#0000FF",
        description="",
        shares=[],
        readonly=1,
        set_as_default=0,
    ):
        """修改日历
        https://open.work.weixin.qq.com/api/doc/90000/90135/93647

        Args:
            cal_id (str): 日历ID
            organizer (str): 指定的组织者userid。注意该字段指定后不可更新
            summary (str): 日历标题。1 ~ 128 字符
            color (str): 日历在终端上显示的颜色，RGB颜色编码16进制表示，例如：”#0000FF” 表示纯蓝色
            description (str, optional): 日历描述。. Defaults to "".
            shares (list, optional): 日历共享成员列表。最多2000人. Defaults to [].
                {
                    "userid" : "userid2",
                    "readonly" : 1
                }
            readonly (int, optional): [description]. Defaults to 1.
            set_as_default (int, optional): 是否将该日历设置为组织者的默认日历。
                                            0-否；1-是。默认为0，即不设为默认日历
                                            第三方应用不支持使用该参数. Defaults to 0.

        Returns:
            dict: 
        """
        api_name = "oa/calendar/update"
        data = {
            "calendar": {
                "cal_id": cal_id,
                "organizer": organizer,
                "readonly": readonly,
                "set_as_default": set_as_default,
                "summary": summary,
                "color": color,
                "description": description,
                "shares": shares,
            },
        }
        response = self.request(api_name=api_name, method="post", json=data,)
        return response

    def get(self, cal_id_list=[]):
        """日历详情，可以同时请求多个

        Args:
            cal_id_list (list, optional): cal_id 列表. Defaults to [].
        { 
            "cal_id_list": ["wcjgewCwAAqeJcPI1d8Pwbjt7nttzAAA"]
        }
        """
        api_name = "oa/calendar/get"
        data = {"cal_id_list": cal_id_list}
        response = self.request(api_name=api_name, method="post", json=data,)
        return response

    def delete(self, cal_id):
        """删除日历，可以同时请求多个

        Args:
            cal_id (str): cal_id. Defaults to [].
        { 
            "cal_id":"wcjgewCwAAqeJcPI1d8Pwbjt7nttzAAA"
        }
        """
        api_name = "oa/calendar/del"
        data = {"cal_id": cal_id}
        response = self.request(api_name=api_name, method="post", json=data,)
        return response


class schedule(base):
    def __init__(self, token: str):
        super().__init__(token)

    def add(
        self,
        organizer: str,
        summary: str,
        cal_id: str,
        location: str,
        is_remind=1,
        remind_before_event_secs=3600,
        repeat_until=0,
        is_repeat=1,
        repeat_type=7,
        is_custom_repeat=0,
        repeat_interval=7,
        repeat_day_of_week=[1, 7],
        repeat_day_of_month=[1, 31],
        timezone=8,
        attendees=[],
        start_time: int = None,
        end_time: int = None,
        description="",
        agentid: int = None,
    ):
        """添加日程
        https://open.work.weixin.qq.com/api/doc/90000/90135/93648

        Args:
            organizer (str): 组织者
            summary (str): 日程标题。0 ~ 128 字符。不填会默认显示为“新建事件”
            cal_id (str): 	日程所属日历ID。该日历必须是access_token所对应应用所创建的日历。
                            注意，这个日历必须是属于组织者(organizer)的日历；
                            如果不填，那么插入到组织者的默认日历上。
                            第三方应用必须指定cal_id
                            不多于64字节
            location (str): 日程地址
                            不多于128个字符
        Returns:
            [type]: [description]
        """
        api_name = "oa/schedule/add"
        data = {
            "schedule": {
                "organizer": organizer,
                "start_time": start_time,
                "end_time": end_time,
                "attendees": attendees,
                "summary": summary,
                "description": description,
                "reminders": {
                    "is_remind": is_remind,
                    "remind_before_event_secs": remind_before_event_secs,
                    "is_repeat": is_repeat,
                    "repeat_type": repeat_type,
                    "repeat_until": repeat_until,
                    "is_custom_repeat": is_custom_repeat,
                    "repeat_interval": repeat_interval,
                    "repeat_day_of_week": repeat_day_of_week,
                    "repeat_day_of_month": repeat_day_of_month,
                    "timezone": timezone,
                },
                "location": location,
                "cal_id": cal_id,
            },
        }
        if agentid:
            data["agentid"] = agentid
        response = self.request(api_name=api_name, method="post", json=data,)
        return response

    def update(
        self,
        organizer: str,
        schedule_id: str,
        summary: str,
        location: str,
        is_remind=1,
        remind_before_event_secs=3600,
        repeat_until=0,
        is_repeat=1,
        repeat_type=7,
        is_custom_repeat=0,
        repeat_interval=7,
        repeat_day_of_week=[1, 7],
        repeat_day_of_month=[1, 31],
        timezone=8,
        attendees=[],
        start_time: int = None,
        end_time: int = None,
        description="",
        agentid: int = None,
    ):
        """添加日程
        https://open.work.weixin.qq.com/api/doc/90000/90135/93648

        Args:
            organizer (str): 组织者
            summary (str): 日程标题。0 ~ 128 字符。不填会默认显示为“新建事件”
            location (str): 日程地址
                            不多于128个字符
        Returns:
            [type]: [description]
        """
        api_name = "oa/schedule/update"
        data = {
            "schedule": {
                "organizer": organizer,
                "schedule_id": schedule_id,
                "start_time": start_time,
                "end_time": end_time,
                "attendees": attendees,
                "summary": summary,
                "description": description,
                "reminders": {
                    "is_remind": is_remind,
                    "remind_before_event_secs": remind_before_event_secs,
                    "is_repeat": is_repeat,
                    "repeat_type": repeat_type,
                    "repeat_until": repeat_until,
                    "is_custom_repeat": is_custom_repeat,
                    "repeat_interval": repeat_interval,
                    "repeat_day_of_week": repeat_day_of_week,
                    "repeat_day_of_month": repeat_day_of_month,
                    "timezone": timezone,
                },
                "location": location,
            },
        }
        response = self.request(api_name=api_name, method="post", json=data,)
        return response

    def get(self, schedule_id_list=[]):
        """日程详情，可以同时请求多个

        Args:
            schedule_id_list (list, optional): calschedule_id_list_id 列表. Defaults to [].
        { 
            "schedule_id_list": ["17c7d2bd9f20d652840f72f59e796AAA"]
        }
        """
        api_name = "oa/schedule/get"
        data = {"schedule_id_list": schedule_id_list}
        response = self.request(api_name=api_name, method="post", json=data,)
        return response

    def delete(self, schedule_id=[]):
        """取消日程

        Args:
            schedule_id (str): schedule_id
        { 
            "schedule_id": "17c7d2bd9f20d652840f72f59e796AAA"
        }
        """
        api_name = "oa/schedule/del"
        data = {"schedule_id": schedule_id}
        response = self.request(api_name=api_name, method="post", json=data,)
        return response

    def get_by_calendar(self, cal_id: str, offset=100, limit=1000):
        """获取日历下的日程列表

        Args:
            schedule_id (str): schedule_id
        {
            "cal_id": "wcjgewCwAAqeJcPI1d8Pwbjt7nttzAAA",
            "offset" : 100,
            "limit" : 1000
        }
        """
        api_name = "oa/schedule/get_by_calendar"
        data = {"cal_id": cal_id, "offset": offset, "limit": limit}
        response = self.request(api_name=api_name, method="post", json=data,)
        return response

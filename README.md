# 目录

- [目录](#目录)
- [版本更新](#版本更新)
- [pywxwork](#pywxwork)
- [企微 python 接口](#企微python接口)
- [框架结构](#框架结构)
  - [接口](#接口)
    - [接口列表](#接口列表)
- [how to use](#how-to-use)
  - [install pywxwork](#install-pywxwork)
  - [get token](#get-token)
  - [get user list](#get-user-list)

# 版本更新

| ver   | desc               | date     |
| ----- | ------------------ | -------- |
| 1.0.4 | 完成电子发票的接口 | 20210530 |
| 1.0.5 | 完成日历日程       | 20210702 |

# pywxwork

- python wxwork server api(企业微信自建应用服务端)
- version==1.0.1

# 企微 python 接口

- 写一个企微的 python 库，开箱即用。
- 这个接口库完全用于企微的服务端接口。
- 接口应当包括两部分

  - 直接调用企微的接口，这里做一个 pip 库上传到 pypi。
  - 用 fastapi 起服务，来做回调服务。

- [企微接口地址](https://open.work.weixin.qq.com/api/doc/90000/90135/90664)

# 框架结构

## 接口

### 接口列表

| status   | name         | mod_name         |
| -------- | ------------ | ---------------- |
| 完成     | 通讯录管理   | contact          |
| 未完成   | 客户联系     | customer         |
| 未完成   | 身份验证     |                  |
| 未完成   | 应用管理     |                  |
| 完成     | 消息推送     | message          |
| 完成     | 素材管理     | media            |
| 部分完成 | OA           | 日历，日程已完成 |
| 未完成   | 效率工具     |                  |
| 未完成   | 企业支付     |                  |
| 未完成   | 企业互联     |                  |
| 未完成   | 会话内容存档 |                  |
| 已完成   | 电子发票     | invoice          |
| 未完成   | 家校沟通     |                  |
| 未完成   | 家校应用     |                  |
| 未完成   | 政民沟通     |                  |
| 未完成   | 邮件         | exmail           |

### 新版

| 状态     | name         | mod_name         |
| -------- | ------------ | ---------------- |
| 完成     | 通讯录管理   | contact          |
| 未完成   | 客户联系     | customer         |
| 未完成   | 身份验证     |                  |
| 未完成   | 应用管理     |                  |
| 完成     | 消息推送     | message          |
| 完成     | 素材管理     | media            |
| 部分完成 | OA           | 日历，日程已完成 |
| 未完成   | 效率工具     |                  |
| 未完成   | 企业支付     |                  |
| 未完成   | 企业互联     |                  |
| 未完成   | 会话内容存档 |                  |
| 已完成   | 电子发票     | invoice          |
| 未完成   | 家校沟通     |                  |
| 未完成   | 家校应用     |                  |
| 未完成   | 政民沟通     |                  |
| 未完成   | 邮件         | exmail           |

### 功能包括

- 内部开发接口-服务端
  - 回调的事件
  - 主动查询接口
- 第三方开发接口-服务端
- 单元测试

# how to use

### install pywxwork

`pip install pywxwork`

### get token

```python
from pywxwork.token import token

corpid = "wxaadfasdfasdfasdfas"
corpsecret = "asdfasdfasdfasfasdfasdfasdf"

t = token(corpid=corpid, corpsecret=corpsecret)
t.token
```

### get user list

```python
from pywxwork.contact.user import user

u = user(token)
response = u.list(department_id=1, fetch_child=1)
user_list = response.get("userlist")
for row in user_list:
  print(row)
```

### 20240617 更新

https://developer.work.weixin.qq.com/document/path/97297#%E8%8E%B7%E5%8F%96%E8%8E%B7%E5%AE%A2%E9%93%BE%E6%8E%A5%E5%88%97%E8%A1%A8
https://developer.work.weixin.qq.com/document/path/97297#%E8%8E%B7%E5%8F%96%E8%8E%B7%E5%AE%A2%E9%93%BE%E6%8E%A5%E8%AF%A6%E6%83%85
https://developer.work.weixin.qq.com/document/path/97375#%E6%9F%A5%E8%AF%A2%E9%93%BE%E6%8E%A5%E4%BD%BF%E7%94%A8%E8%AF%A6%E6%83%85

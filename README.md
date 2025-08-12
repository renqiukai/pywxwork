# 目录

- [目录](#目录)
- [版本更新](#版本更新)
- [计划](#计划)
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

# 计划

- 完成客户联系、身份验证、应用管理等未完成模块
- 补充单元测试覆盖
- 提供更多使用示例与文档

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
新增获客链接接口封装：

- `customer_acquisition.list_link` - 获取获客链接列表
- `customer_acquisition.get` - 获取获客链接详情
- `customer_acquisition.create_link` - 创建获客链接
- `customer_acquisition.update_link` - 更新获客链接
- `customer_acquisition.delete_link` - 删除获客链接
- `customer_acquisition_quota.get_quota` - 查询剩余使用量
- `customer_acquisition_quota.statistic` - 查询链接使用详情

接口文档参考：
https://developer.work.weixin.qq.com/document/path/97297
https://developer.work.weixin.qq.com/document/path/97375

### 20240619 新增
新增客户群管理接口：

- `groupchat.list` - 获取客户群列表
- `groupchat.get` - 获取客户群详情
- `groupchat.add_join_way` - 创建群链接
- `groupchat.get_join_way` - 获取群链接详情
- `groupchat.update_join_way` - 更新群链接
- `groupchat.del_join_way` - 删除群链接

接口文档参考：
https://developer.work.weixin.qq.com/document/path/92120

### 20240620 新增
新增欢迎语和群欢迎语接口：

- `customer.send_welcome_msg` - 发送新客户欢迎语
- `group_welcome_template.add` - 创建群欢迎语模板
- `group_welcome_template.edit` - 编辑群欢迎语模板
- `group_welcome_template.get` - 获取群欢迎语模板详情
- `group_welcome_template.delete` - 删除群欢迎语模板

接口文档参考：
https://developer.work.weixin.qq.com/document/path/92134

### 20240621 新增
新增客户和群聊继承接口：

- `customer.transfer_customer` - 在职成员分配客户
- `customer.transfer_result` - 查询客户分配结果
- `customer.resigned_transfer_customer` - 离职成员客户继承
- `customer.resigned_transfer_result` - 查询离职客户继承结果
- `groupchat.transfer` - 离职成员群聊继承
- `groupchat.transfer_result` - 查询群聊继承结果

接口文档参考：
https://developer.work.weixin.qq.com/document/path/92125

### 20240622 新增
新增电子发票接口封装：

- `invoice.get_invoice_info` - 查询单张电子发票
- `invoice.get_invoice_info_batch` - 批量查询电子发票
- `invoice.update_invoice_status` - 更新单张发票状态
- `invoice.update_invoice_status_batch` - 批量更新发票状态

接口文档参考：
https://developer.work.weixin.qq.com/document/path/90664

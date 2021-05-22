- [pywxwork](#pywxwork)
- [企微python接口](#企微python接口)
- [框架结构](#框架结构)
- [how to use](#how-to-use)
    - [install pywxwork](#install-pywxwork)
    - [get token](#get-token)
    - [get user list](#get-user-list)

# pywxwork
- python wxwork server api
- version==1.0.1


# 企微python接口

- 写一个企微的python库，开箱即用。
- 这个接口库完全用于企微的服务端接口。
- 接口应当包括两部分
    - 直接调用企微的接口，这里做一个pip库上传到pypi。
    - 用fastapi起服务，来做回调服务。

- [企微接口地址](https://open.work.weixin.qq.com/api/doc/90000/90135/90664)


# 框架结构
- [ ] 通讯录管理 contact
- [ ] 客户联系
- [ ] 身份验证
- [ ] 应用管理
- [ ] 消息推送
- [ ] 素材管理
- [ ] OA
- [ ] 效率工具
- [ ] 企业支付
- [ ] 企业互联
- [ ] 会话内容存档
- [ ] 电子发票
- [ ] 家校沟通
- [ ] 家校应用
- [ ] 政民沟通


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
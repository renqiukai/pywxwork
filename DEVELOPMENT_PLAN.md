# pywxwork 现代化升级计划（2026）

更新日期：2026-05-26

## 1. 项目定位

`pywxwork` 继续定位为“企业微信企业内部开发/自建应用服务端 API 的 Python SDK”。本轮升级不追求一次性覆盖全部企业微信能力，而是先把现有可用接口修稳，再按企业自建应用的高频场景补齐接口。

## 2. 文档核对依据

本计划按企业微信企业内部开发服务端 API 目录重新梳理。当前目录核心板块包括：

- 开发指南：回调配置、自建应用与第三方应用对接、`access_token`、API 域名 IP 段。
- 通讯录管理：成员、部门、标签、异步批量、通讯录回调、互联企业、异步导出。
- 客户联系：服务人员、客户管理、客户标签、在职/离职继承、客户群、联系我/入群方式、朋友圈、群发、统计、商品图册、聊天敏感词。
- 身份验证：网页授权登录、扫码授权登录、敏感字段授权。
- 应用管理：菜单、工作台自定义展示、获取/设置应用。
- 消息推送：接收消息与事件、群聊会话、应用消息、模板卡片更新、消息撤回。
- 素材管理：上传/获取临时素材、上传图片、异步上传任务。
- OA 与效率工具：打卡、审批、汇报、会议室、日程、会议、直播、微盘、邮件、文档。
- 其他：微信客服、企业支付、企业互联、上下游、会话内容存档、电子发票、家校、政民沟通。

参考入口：

- https://developer.work.weixin.qq.com/document
- https://s.apifox.cn/apidoc/docs-site/406014
- https://wdk-docs.github.io/wework-docs/release-notes/

## 3. 当前仓库覆盖情况

已有模块：

- 基础层：`token.py`、`base.py`
- 通讯录：`contact/user.py`、`department.py`、`tag.py`、`async.py`、`linkedcorp.py`
- 客户联系：`customer/`、`externalcontact/customer_acquisition*`、`groupchat/`、`group_welcome_template/`
- 消息与素材：`message/`、`message/appchat.py`、`webhook/`、`media/`
- OA/效率局部：`calendar/`、`tool/living.py`
- 其他：`invoice/`、`ticket/ticket.py`、`callback/`

主要问题：

- 接口清单与官方现状不同步，缺少明确“已覆盖/缺失/废弃或变更”的矩阵。
- 请求层没有统一超时、重试、异常体系、分页 helper、文件上传 helper。
- 旧测试脚本依赖真实凭据，且仓库中已有明文样例风险。
- 通讯录敏感字段、客户敏感字段、应用可见范围等新权限模型需要重新校准。
- 包结构和命名风格不统一，未来补接口会越来越难维护。

## 4. 升级原则

1. 先稳定核心调用链，再扩接口。
2. 优先覆盖自建应用常用能力，不优先做第三方服务商、家校、政民沟通等垂直场景。
3. 每个新增接口必须带官方文档链接、请求方法、路径、参数、返回样例和最小测试。
4. 对历史方法保留兼容别名，破坏性变更放到 2.0。
5. 所有真实企业信息、token、secret、手机号、客户 ID 不进仓库。

## 5. 阶段计划

### 阶段 A：文档盘点与工程基线（第 1 周，P0）

交付：

- 新建 `docs/api-matrix.md`，按官方目录列出：模块、接口名、路径、当前状态、对应代码、优先级。
- 新建 `tests/`，把根目录 `test_*.py` 拆成 mock 单测与手工集成示例。
- 引入 `pytest`、`ruff`，新增最小 CI：lint + unit tests。
- 清理凭据样例，新增 `.env.example`。

验收：

- `python -m pytest` 可稳定运行，不访问真实企业微信。
- API 矩阵覆盖通讯录、客户联系、身份验证、应用管理、消息、素材这六个 P0/P1 模块。

### 阶段 B：核心 Client 重构（第 2 周，P0）

交付：

- 新增统一 `Client`：管理 `access_token`、`timeout`、`proxies`、debug、JSON/form/file 请求。
- 定义异常：`WxWorkAPIError`、`WxWorkHTTPError`、`WxWorkTokenError`。
- 增加分页 helper：支持 `cursor`、`next_cursor`、`has_more`。
- 增加上传 helper：普通素材、图片、异步上传任务共用。
- 移除默认可变参数，例如 `def invite(user_list=[])`。

验收：

- `base.py`/`token.py` 核心路径单测覆盖成功、业务错误、HTTP 错误、网络异常。
- 历史调用方式仍能跑通，至少保留一个小版本兼容期。

### 阶段 C：通讯录与身份验证校准（第 3 周，P0）

交付：

- 对齐成员、部门、标签、异步批量、异步导出、通讯录回调。
- 补齐 `userid`/`openid`、手机号/邮箱查 `userid`、成员 ID 列表等新接口。
- 新增身份验证模块：网页授权、扫码登录、`auth/getuserdetail` 敏感字段获取。
- 在文档中明确：手机号、邮箱、头像、二维码、地址等敏感字段需要授权或可能不返回。

验收：

- `contact` 模块 API 矩阵 P0 项状态为“已实现/已校准”。
- 敏感字段相关接口有测试覆盖与 README 提示。

### 阶段 D：客户联系升级（第 4-5 周，P0/P1）

交付：

- 整理 `customer` 与 `externalcontact` 包边界，统一到一个清晰命名空间。
- 补齐客户管理、客户标签、在职/离职继承、客户群、联系我、入群方式、欢迎语、群发、统计。
- 新增高价值但当前缺失的客户朋友圈、商品图册、聊天敏感词。
- 对分页列表统一返回迭代器：例如 `iter_customers()`、`iter_groupchats()`。

验收：

- 客户联系常用 CRM 场景可以完整串联：成员列表 -> 客户列表 -> 客户详情 -> 标签 -> 群聊 -> 统计。
- 每个子模块至少 1 个 mock 单测和 1 个 README 示例。

### 阶段 E：应用、消息、素材与回调（第 6 周，P1）

交付：

- 应用管理：菜单、工作台展示、获取应用、设置应用。
- 消息推送：应用消息类型、模板卡片更新、撤回消息、群聊会话。
- 素材管理：临时素材、图片、高清语音、异步上传。
- 回调：统一 URL 验证、解密、事件分发、回调类型注册表。

验收：

- 能完成自建应用常见闭环：配置回调 -> 收事件 -> 发应用消息 -> 上传素材。
- 回调加解密库有固定样例测试。

### 阶段 F：可选业务模块（第 7-8 周，P2）

按使用价值选择实现，不作为首版阻塞项：

- 微信客服：客服帐号、接待人员、读取/发送客服消息、统计。
- OA：审批、打卡、汇报、会议室。
- 效率工具：日程、会议、直播、微盘、邮件、文档。
- 企业支付、企业互联、上下游、会话内容存档。
- 电子发票：保留并校准现有实现。

验收：

- 每个 P2 模块单独发小版本，不混入核心重构大 PR。

## 6. 建议的新包结构

```text
pywxwork/
  client.py
  exceptions.py
  token.py
  contact/
  external_contact/
  auth/
  application/
  message/
  media/
  callback/
  oa/
  efficiency/
  invoice/
```

兼容策略：

- 新代码使用 `external_contact`、`auth` 等清晰命名。
- 旧路径如 `externalcontact` 保留 re-export，并在文档标注 deprecated。

## 7. 发布路线

- `1.1.x`：工程基线、测试、请求层修复，不大改 API。
- `1.2.x`：通讯录、身份验证、应用管理、消息、素材校准。
- `1.3.x`：客户联系完整升级。
- `1.4.x`：微信客服/OA/效率工具按需补齐。
- `2.0.0`：统一命名、移除废弃别名、全面迁移到新 Client。

## 8. 每个接口的开发模板

1. 在 `docs/api-matrix.md` 登记官方路径与优先级。
2. 在对应模块实现方法，保留原始字段名，不随意改业务含义。
3. 写 mock 单测：成功、业务错误、参数边界。
4. 写 README 或模块文档示例。
5. 如接口涉及权限/敏感字段/频控，在 docstring 和文档中说明。

## 9. 第一批可立即执行任务

1. 建 `docs/api-matrix.md`，先录入通讯录、客户联系、身份验证、应用管理、消息、素材。
2. 新建 `pywxwork/client.py` 和 `pywxwork/exceptions.py`，为旧 `base` 提供兼容适配。
3. 新建 `tests/test_client.py`、`tests/test_token.py`、`tests/contact/test_user.py`。
4. 清理根目录测试脚本中的真实凭据，移动到 `examples/`。
5. 补 `auth` 模块，优先实现网页授权身份与敏感字段获取。

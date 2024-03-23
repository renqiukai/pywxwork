from .WXBizMsgCrypt import WXBizMsgCrypt


def receive_check_msg(
    corpId: str,
    token: str,
    encodingAesKey: str,
    msg_signature,
    timestamp: str,
    nonce: str,
    echostr: str,
):
    w = WXBizMsgCrypt(token, encodingAesKey, corpId)
    ret, sReplyEchoStr = w.VerifyURL(msg_signature, timestamp, nonce, echostr)
    if ret == 0:
        print(sReplyEchoStr)
    return sReplyEchoStr

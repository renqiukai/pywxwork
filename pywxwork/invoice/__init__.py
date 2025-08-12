from loguru import logger
from ..base import base


class invoice(base):
    def __init__(self, token: str):
        super().__init__(token)

    def get_invoice_info(self, card_id, encrypt_code):
        api_name = "card/invoice/reimburse/getinvoiceinfo"
        data = {"card_id": card_id, "encrypt_code": encrypt_code}
        response = self.request(api_name=api_name, method="post", json=data)

        return response

    def get_invoice_info_batch(self, item_list):
        """批量查询电子发票信息"""
        api_name = "card/invoice/reimburse/getinvoiceinfobatch"
        data = {"item_list": item_list}
        response = self.request(api_name=api_name, method="post", json=data)

        return response

    def update_invoice_status(self, card_id, encrypt_code, reimburse_status):
        """
        发报销状态
        INVOICE_REIMBURSE_INIT：发票初始状态，未锁定；
        INVOICE_REIMBURSE_LOCK：发票已锁定，无法重复提交报销;
        INVOICE_REIMBURSE_CLOSURE:发票已核销，从用户卡包中移除
        """
        api_name = "card/invoice/reimburse/updateinvoicestatus"
        data = {
            "card_id": card_id,
            "encrypt_code": encrypt_code,
            "reimburse_status": reimburse_status,
        }

        response = self.request(api_name=api_name, method="post", json=data)

        return response

    def update_invoice_status_batch(self, data):
        """
        发报销状态
        INVOICE_REIMBURSE_INIT：发票初始状态，未锁定；
        INVOICE_REIMBURSE_LOCK：发票已锁定，无法重复提交报销;
        INVOICE_REIMBURSE_CLOSURE:发票已核销，从用户卡包中移除
        """
        api_name = "card/invoice/reimburse/updatestatusbatch"
        response = self.request(api_name=api_name, method="post", json=data)

        return response

    def update_invoice_status_batch_demo(self):
        """
        发报销状态
        INVOICE_REIMBURSE_INIT：发票初始状态，未锁定；
        INVOICE_REIMBURSE_LOCK：发票已锁定，无法重复提交报销;
        INVOICE_REIMBURSE_CLOSURE:发票已核销，从用户卡包中移除
        """
        data = {
            "openid": "OPENID",
            "reimburse_status": "INVOICE_REIMBURSE_INIT",
            "invoice_list": [
                {"card_id": "cardid_1", "encrypt_code": "encrypt_code_1"},
                {"card_id": "cardid_2", "encrypt_code": "encrypt_code_2"},
            ],
        }
        response = self.update_invoice_status_batch(data)

        return response

    def get_invoice_status_batch(self, data):
        """
        发报销状态
        INVOICE_REIMBURSE_INIT：发票初始状态，未锁定；
        INVOICE_REIMBURSE_LOCK：发票已锁定，无法重复提交报销;
        INVOICE_REIMBURSE_CLOSURE:发票已核销，从用户卡包中移除
        """
        api_name = "card/invoice/reimburse/getinvoiceinfobatch"
        response = self.request(api_name=api_name, method="post", json=data)

        return response

    def get_invoice_status_batch_demo(self):
        """
        发报销状态
        INVOICE_REIMBURSE_INIT：发票初始状态，未锁定；
        INVOICE_REIMBURSE_LOCK：发票已锁定，无法重复提交报销;
        INVOICE_REIMBURSE_CLOSURE:发票已核销，从用户卡包中移除
        """
        data = {
            "item_list": [
                {"card_id": "CARDID1", "encrypt_code": "ENCRYPTCODE1"},
                {"card_id": "CARDID2", "encrypt_code": "ENCRYPTCODE2"},
            ]
        }
        response = self.get_invoice_status_batch(data)

        return response

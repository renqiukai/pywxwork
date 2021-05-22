from loguru import logger
from ..base import base


class media(base):
    def __init__(self, token: str):
        super().__init__(token)

    def upload(self, type: str, file: str):
        api_name = "media/upload"
        params = {
            "type": type
        }
        files = {type: open(file, "rb")}
        response = self.request(
            api_name=api_name,
            method="POST",
            params=params,
            files=files
        )
        logger.debug(response)
        return response

from loguru import logger
from ..base import base


class media(base):
    def __init__(self, token: str):
        super().__init__(token)

    def upload(self, type: str, file: str, filename: str = "data.xlsx"):
        api_name = "media/upload"
        params = {"type": type}
        # files = {type: open(file, "rb")}
        files = {"file": (f"{filename}.xlsx", open(file, "rb"))}
        response = self.request(
            api_name=api_name, method="POST", params=params, files=files
        )

        return response

    def uploadimg(self, file: str):
        api_name = "media/uploadimg"
        files = {"image": open(file, "rb")}
        response = self.request(api_name=api_name, method="POST", files=files)

        return response

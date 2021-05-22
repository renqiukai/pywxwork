from loguru import logger
from .base import base


class externalContact(base):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

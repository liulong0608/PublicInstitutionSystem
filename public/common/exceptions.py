"""         ==Coding: UTF-8==
**    @Project :        UIAutomationTestTemplate
**    @fileName         exceptions.py
**    @author           Echo
**    @EditTime         2023/12/5
"""
from typing import *

from public.common.log import Log


class BaseFailure(Exception):
    def __init__(self, message: Text):
        log = Log(stream=True).logger
        log.error(message)


class ElementNotFound(BaseFailure):
    pass


class InvalidArgumentException(BaseFailure):
    pass


class UnsupportedBrowserException(BaseFailure):
    pass


class NameError(BaseFailure):
    pass

# -*- coding=UTF-8 -*-
# @Project :        base_util.py
# @fileName         check_download.py
# @author           Echo
# @EditTime         2024/5/10
import os.path
import time
from typing import *
from public.common.log import Log
from config.globalparam import download_path

log = Log().get_logger()


def check_download(filename: Text, load: int = 5) -> bool:
    """
    检查下载
    :param filename: 文件名
    :param load: 加载时间
    """
    try:
        if os.path.exists(download_path):
            time.sleep(load)
            for file in os.listdir(download_path):
                if filename in file:
                    return True
                return False
    except Exception:
        log.error("The file is not exist！Please check the code！")


def clear_download() -> None:
    """
    清空下载文件
    """
    if os.path.exists(download_path):
        for file in os.listdir(download_path):
            if len(file) > 0:
                os.remove(os.path.join(download_path))


def assert_download(filename: Text, load: int = 5) -> None:
    """
    断言下载
    :param filename: 文件名
    :param load: 加载时间
    """
    assert check_download(filename, load)

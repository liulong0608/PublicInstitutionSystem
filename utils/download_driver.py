# -*- coding: UTF-8 -*-
"""
**    @Project :        PublicInstitutionSystem
**    @fileName         download_driver.py
**    @author           Echo
**    @EditTime         2024/1/24
"""
import os
import shutil

from config.globalparam import config_path
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

from public.common.exceptions import UnsupportedBrowserException


def download_driver(browser):
    """
    download driver
    :return:
    """
    if browser == 'chrome':
        # 1.使用ChromeDriverManager安装ChromeDriver，并返回驱动程序的路径
        driver_path = ChromeDriverManager().install()
    elif browser == 'firefox':
        driver_path = GeckoDriverManager().install()
    elif browser == 'ie':
        driver_path = IEDriverManager().install()
    elif browser == 'edge':
        driver_path = EdgeChromiumDriverManager().install()
    elif browser == 'opera':
        driver_path = OperaDriverManager().install()
    else:
        raise UnsupportedBrowserException(f"Browser {browser} is not supported.")
    # 打印驱动程序路径
    print(driver_path)
    new_path = config_path
    # 把驱动程序复制到指定路径
    shutil.copy(driver_path, new_path)


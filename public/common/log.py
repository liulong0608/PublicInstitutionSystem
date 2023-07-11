# == Coding: UTF-8 ==
# @Project :        BusinessWageSystem
# @fileName         log.py  
# @version          v0.1
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/6/9
# @Software:        PyCharm
# ====/******/=====
import logging
import time
import os
from datetime import datetime
from config import globalparam


log_path = globalparam.log_path


class Log:
    def __init__(self):
        self.logname = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))

    def capture_screenshot(self, driver, screenshot_dir):
        # 创建截图目录（如果不存在）
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
            # 生成截图文件名，基于当前时间戳
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            screenshot_file = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")

            # 执行截图操作
            driver.save_screenshot(screenshot_file)

            # 记录截图文件路径到日志
            self.info(f"Screenshot captured: {screenshot_file}")

    def __printconsole(self, level, message):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter(
            '\n%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__printconsole('debug', message)

    def info(self, message):
        self.__printconsole('info', message)

    def warning(self, message):
        self.__printconsole('warning', message)

    def error(self, message):
        self.__printconsole('error', message)

# == Coding: UTF-8 ==
# @Project :        UIAutomationTestTemplate
# @fileName         run.py  
# @version          v0.1
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/4/6
# @Software:        PyCharm
# ====/******/=====
import unittest
from scripts.HTMLTestRunner import *
import time
from config import globalparam
from testcase.test_all_case import TestAll
from BeautifulReport import BeautifulReport


def run():
    test_dir = './testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test*.py')

    now = time.strftime('%Y-%m-%d')
    reportname = globalparam.report_path + '\\' + 'TestResult' + now + '.html'
    with open(reportname, 'w', encoding='utf-8') as f:
        runner = HTMLTestRunner(
            stream=f, verbosity=2,
            title='测试报告',
            description='Test the import testcase'
        )
        runner.run(suite)
    # time.sleep(3)
    # # 发送邮件
    # mail = sendmail.SendMail()
    # mail.send()
    # # 邮件发送需要邮件配置信息


if __name__ == '__main__':
    run()

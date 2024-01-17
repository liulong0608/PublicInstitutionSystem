# == Coding: UTF-8 ==
# @Project :        UIAutomationTestTemplate
# @fileName         run.py  
# @version          v0.1
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/4/6
# @Software:        PyCharm
# ====/******/=====
import os.path
import unittest
from utils.HTMLTestRunner import *
import time
from config import globalparam
from BeautifulReport import BeautifulReport as bf


def run():
    suite = unittest.defaultTestLoader.discover(start_dir=globalparam.case_path, pattern='test*.py')
    now = time.strftime('%Y-%m-%d')
    reportname = globalparam.report_path + '\\' + 'TestResult' + now + '.html'
    reportname = os.path.join(globalparam.report_path, 'report.html')
    # run_result = bf(suite)
    # run_result.report(filename="report", description='测试报告',
    #                   report_dir=globalparam.report_path)
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

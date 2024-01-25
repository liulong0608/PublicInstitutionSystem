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
import time
import unittest
import unittestreport
from config import globalparam


def run():
    suite = unittest.defaultTestLoader.discover(start_dir=globalparam.case_path, pattern='test*.py')
    # now = time.strftime('%Y-%m-%d')
    report_path = globalparam.report_path
    # reportname = 'TestResult' + now
    reportname = 'TestResult'
    runner = unittestreport.TestRunner(
        suite=suite,
        tester='Echo',
        report_dir=report_path,
        filename=reportname,
        title='事业工资系统-测试报告',
        templates=1,
        desc='This is the test report of the business payroll system.'
    )
    runner.run(
        # count=3, interval=3  # 失败重跑3次，每次间隔3秒
    )
    # time.sleep(3)
    # # 发送邮件
    # runner.send_email(
    #     host='smtp.qq.com',    # smtp服务器地址
    #     port=465,      # smtp服务器端口465,25
    #     user='tzu-mingliu@qq.com',    # 发送邮箱用户名
    #     password='Flzx3000c',    # 发送邮箱密码
    #     to_addrs='liulong@3mencn.com'  # 收件人邮箱地址
    # )


if __name__ == '__main__':
    run()

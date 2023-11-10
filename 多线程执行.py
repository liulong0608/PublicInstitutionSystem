# == Coding: UTF-8 ==
# @Project :        PublicInstitutionSystem
# @fileName         多线程执行.py  
# @version          v0.1
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/7/12
# @Software:        PyCharm
# ====/******/=====
import time
import unittest
import threadpool
import HTMLTestRunner
from concurrent.futures import ThreadPoolExecutor
from config import globalparam


def add_case():
    test_dir = './testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test*.py')
    return suite


def run_case(test_case):
    now = time.strftime('%Y-%m-%d')
    reportname = globalparam.report_path + '\\' + 'TestResult' + now + '.html'
    fp = open(reportname, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp, verbosity=2,
        title='测试报告',
        description='Test the import testcase'
    )
    runner.run(test_case)
    fp.close()


# if __name__ == '__main__':
#     cases = add_case()
#     pool = threadpool.ThreadPool(10)
#     requests = threadpool.makeRequests(run_case, cases)
#     [pool.putRequest(req) for req in requests]
#     pool.wait()
if __name__ == '__main__':
    cases = add_case()
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(run_case, cases)

# == Coding: UTF-8 ==
# @Project :        UIAutomationTestTemplate
# @fileName         run.py  
# @version          v0.1
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/4/6
# @Software:        PyCharm
# ====/******/=====
import os

import pytest
from utils.others_controls.allure_control import set_report_env_on_results, set_report_executer_on_results
from config.globalparam import report_temp_path, report_path

if __name__ == "__main__":
    pytest.main()
    set_report_env_on_results()  # 写入环境信息
    # set_report_executer_on_results()    # 写入运行器
    os.system(f"allure generate {report_temp_path} -o {report_path} --clean")
    os.system(f"allure open -h localhost -p 51733 {report_path}")

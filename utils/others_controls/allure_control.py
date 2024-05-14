# -*- coding=UTF-8 -*-
# @Project :        base_util.py
# @fileName         allure_control.py
# @author           Echo
# @EditTime         2024/5/9
import json
import os

from config.globalparam import node, report_temp_path


def set_report_env_on_results():
    """
    在allure-results报告的目录下生成一个写入了环境信息的文件：environment.properties(注意：不能放置中文，否则会出现乱码)
    @return:
    """
    # 需要写入的环境信息
    allure_env = {
        'OperatingEnvironment': 'TESTING ENVIRONMENT',
        'BaseUrl': node
    }
    allure_env_file = os.path.join(report_temp_path, 'environment.properties')
    with open(allure_env_file, 'w', encoding='utf-8') as f:
        for _k, _v in allure_env.items():
            f.write(f'{_k}={_v}\n')


def set_report_executer_on_results():
    """
    在allure-results报告的目录下生成一个写入了执行人的文件：executor.json
    @return:
    """
    # 需要写入的环境信息
    allure_executor = {
        "name": "liulong",
        "type": "jenkins",
        "url": "http://helloqa.com",  # allure报告的地址
        "buildOrder": 3,
        "buildName": "allure-report_deploy#1",
        "buildUrl": "http://helloqa.com/#1",
        "reportUrl": "http://helloqa.com/#1/AllureReport",
        "reportName": "张三 Allure Report"
    }
    allure_env_file = os.path.join(report_temp_path, 'executor.json')
    with open(allure_env_file, 'w', encoding='utf-8') as f:
        f.write(str(json.dumps(allure_executor, ensure_ascii=False, indent=4)))

# == Coding: UTF-8 ==
# @Project :        BooksManagementSystem
# @fileName         RandomlyGenerateStudentInformation.py
# @version          v0.6
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/3/30
# @Software:        PyCharm
# ====/******/=====
import json
import random

from faker import Factory

from utils.generateRandomIDNumbers import GenerateRandomIDNumbers


def generate_name():
    # Generate random name
    # fake = Factory.create('zh_CN')
    fake = Factory.create()
    return "测试" + fake.name()


def generate_idcard():
    # Generate random idcard
    return GenerateRandomIDNumbers().generate_id


def generate_gender():
    """ 根据生成的身份证号码判断性别 """
    temp = generate_idcard()
    sex_n = temp[-2]
    if int(sex_n) % 2 == 0:
        return "女"
    else:
        return "男"


def generate_phoneNumber():
    # 生成手机号码前三位
    prefix = random.choice(["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                            "150", "151", "152", "153", "155", "156", "157", "158", "159",
                            "180", "181", "182", "183", "184", "185", "186", "187", "188", "189"])
    # 生成手机号码后8位
    suffix = "".join(str(random.randint(0, 9)) for _ in range(8))
    return prefix + suffix


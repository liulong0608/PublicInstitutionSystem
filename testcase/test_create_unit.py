# -*- coding: UTF-8 -*-
"""
**    @Project :        PublicInstitutionSystem
**    @fileName         test_create_unit.py
**    @author           Echo
**    @EditTime         2024/1/17
"""
import random
from typing import *

import allure
import pytest
from faker import Faker
from public.common.base_util import BaseUtil
from public.common.datainfo import get_xls_to_dict
from public.pages.modules.运维中心.createUnitPage import CreateUnitPage
from utils.RandomlyGeneratePersonnelInformation import generate_idcard
from utils.social_unified_creditcode.succ_utils.sucreditcode import generateUnifiedSocialCreditCode


@allure.epic('运维中心')
@allure.feature('单位管理')
@allure.story('新建单位')
class TestCreateUnit(BaseUtil):
    """ 创建单位 """

    @allure.title('新建单位')
    @pytest.mark.parametrize('args', get_xls_to_dict('test_datas.xlsx', 'create_unit'))
    def test_create_unit(self, args):
        """ 创建单位 """
        cu = CreateUnitPage(self.driver)
        orgcode = generateUnifiedSocialCreditCode()
        save_msg = cu.create_uniit(nest_messages_creditCode=orgcode,
                                   unit_name="测试" + Faker().company(),
                                   supervisor=random.choice(["是", "否"]))
        self.driver.assert_text(save_msg, '保存成功，是否需要维护单位信息？')
        maintenance_msg = cu.maintenance_unit_information(
            args['单位负责人'],
            args['单位电话'],
            args['单位地址'],
            args['邮编'],
            args['财政供养'],
            args['财政统发'],
            args['单位财政编码'],
            args['单位性质'],
            args['执行工资制度'],
            args['单位级别'],
            args['是否主管单位'],
            args['审核流程'],
            args['艰边类别'],
            args['隶属关系'],
            args['公务员规范后津贴标准类别驻地'],
            args['单位驻地'],
            args['平均海拔'],
            args['驻地海拔'],
            args['事业单位类型'],
            args['事业单位行业'],
            args['是否地勘单位'],
            args['经费来源']
        )
        self.driver.assert_text(maintenance_msg, '保存成功，稍后请在单位信息查看')
        operator_msg = cu.create_operator(
            username=orgcode,
            gender=random.choice(['男', '女']),
            name=Faker().name(),
            phoneNumber=Faker('zh_CN').phone_number(),
            identityCard=generate_idcard(),
            contact=None,
            email=None
        )
        self.driver.assert_text_contains('用户已添加', operator_msg)

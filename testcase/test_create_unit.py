# -*- coding: UTF-8 -*-
"""
**    @Project :        PublicInstitutionSystem
**    @fileName         test_create_unit.py
**    @author           Echo
**    @EditTime         2024/1/17
"""
import random
from typing import *
from faker import Faker
from public.common.base_util import BaseUtil
from public.pages.modules.运维中心.createUnitPage import CreateUnitPage
from utils.RandomlyGeneratePersonnelInformation import generate_idcard
from utils.social_unified_creditcode.succ_utils.sucreditcode import generateUnifiedSocialCreditCode


class TestCreateUnit(BaseUtil):
    """ 创建单位 """

    def test_create_unit(self):
        """ 创建单位 """
        cu = CreateUnitPage(self.driver)
        orgcode = generateUnifiedSocialCreditCode()
        save_msg = cu.create_uniit(nest_messages_creditCode=orgcode,
                                   unit_name="测试" + Faker().company(),
                                   supervisor="否")
        self.assert_text(save_msg, '保存成功，是否需要维护单位信息？')
        maintenance_msg = cu.maintenance_unit_information()
        self.assert_text(maintenance_msg, '保存成功，稍后请在单位信息查看')
        operator_msg = cu.create_operator(username=orgcode, gender="男", phoneNumber="15112345678", identityCard=generate_idcard())
        self.assert_text_contains(operator_msg, '用户已添加')

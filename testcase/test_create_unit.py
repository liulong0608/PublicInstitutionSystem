# -*- coding: UTF-8 -*-
"""
**    @Project :        PublicInstitutionSystem
**    @fileName         test_create_unit.py
**    @author           Echo
**    @EditTime         2024/1/17
"""
from typing import *
from faker import Faker
from public.common.base_util import BaseUtil
from public.pages.modules.运维中心.createUnitPage import CreateUnitPage
from utils.social_unified_creditcode.succ_utils.sucreditcode import generateUnifiedSocialCreditCode


class TestCreateUnit(BaseUtil):

    def test_create_unit(self):
        cu = CreateUnitPage(self.driver)
        msg = cu.create_uniit(nest_messages_creditCode=generateUnifiedSocialCreditCode(),
                              unit_name="测试" + Faker().company(),
                              supervisor="否")
        self.assert_text(msg, '保存成功，是否需要维护单位信息？')

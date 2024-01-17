# -*- coding: UTF-8 -*-
"""
**    @Project :        PublicInstitutionSystem
**    @fileName         test_create_unit.py
**    @author           Echo
**    @EditTime         2024/1/17
"""
from typing import *

from public.common.base_util import BaseUtil
from public.pages.modules.运维中心.createUnitPage import CreateUnitPage


class TestCreateUnit(BaseUtil):
    def test_create_unit(self, nest_messages_creditCode, unit_name, supervisor):
        cu = CreateUnitPage(self.driver)
        msg = cu.create_uniit(nest_messages_creditCode, unit_name, supervisor)
        self.assert_text(msg, '保存成功，是否需要维护单位信息？')

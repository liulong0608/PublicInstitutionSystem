# -*- coding: UTF-8 -*-
"""
**    @Project :        PublicInstitutionSystem
**    @fileName         test_personnelAdd.py
**    @author           Echo
**    @EditTime         2024/1/3
"""
import unittest
from typing import *
from public.pages.modules.人员新增减少.personnelAdd_page import PersonnelAddPage
from public.common.base_util import BaseUtil


class TestPersonnelAdd(BaseUtil):
    """人员新增"""
    @unittest.skip
    def test_add_staff(self):
        """人员新增"""
        pa = PersonnelAddPage(self.driver)
        pa.add_staff("12510322MB0M56223X", "运动员", 202301, "测试人员", "女")

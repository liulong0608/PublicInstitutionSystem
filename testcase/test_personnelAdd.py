# -*- coding: UTF-8 -*-
"""
**    @Project :        PublicInstitutionSystem
**    @fileName         test_personnelAdd.py
**    @author           Echo
**    @EditTime         2024/1/3
"""
import random

import pytest

from public.common.base_util import BaseUtil
from public.common.datainfo import get_xls_to_dict
from public.pages.modules.人员新增减少.personnelAdd_page import PersonnelAddPage
from utils.RandomlyGeneratePersonnelInformation import generate_name
from utils.generateRandomIDNumbers import GenerateRandomIDNumbers


class TestPersonnelAdd(BaseUtil):
    """人员新增"""

    @pytest.mark.skip
    @pytest.mark.parametrize("args", get_xls_to_dict("test_datas.xlsx", "add_person"))
    def test_add_staff(self, args):
        """人员新增"""
        pa = PersonnelAddPage(self.driver)
        idcard = GenerateRandomIDNumbers().generate_id
        msg = pa.add_staff(
            args['统一社会信用代码'],
            args['人员身份'],
            args['起薪时间'],
            args['依据文号'],
            args['变动备注'],
            generate_name(),
            args['性别'],
            args['民族'],
            idcard,
            idcard[6:14],
            args['政治面貌'],
            args['初始人员身份'],
            args['籍贯'],
            args['住址'],
            args['人员来源'],
            args['进入本单位时间'],
            args['内设机构'],
            args['备注'],
            args['参工时间'],
            args['学历'],
            args['学位'],
            args['毕业时间'],
            args['是否执行地勘标准'],
            args['是否义务教育教师'],
            args['现任职务'],
            args['现任职务时间'],
            args['实际岗位'],
            args['职员等级'],
            args['任职员等级时间'],
            args['基本工资对应岗位'],
            args['是否领导工资'],
            args['任现岗位时间'],
            args['薪级'],
            args['薪级起考年限'],
            args['是否中小学教师'],
            args['是否护士'],
            args['是否提高10%'],
            args['是否特殊教育'],
            args['保留原特殊岗位'],
            args['退役运动员保留工资额度'],
            args['中小学教师或护士保留原额10%'],
            args['原职员等级保留绝对额']
        )
        self.driver.assert_text("录入人员成功", msg)

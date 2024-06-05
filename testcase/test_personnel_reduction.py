# -*- coding=UTF-8 -*-
# @Project :        base_util.py
# @fileName         test_personnel_reduction.py
# @author           Echo
# @EditTime         2024/5/13
from typing import *

import allure
import pytest

from public.common.base_util import BaseUtil
from public.common.datainfo import get_xls_to_dict
from public.pages.modules.人员新增减少.personnel_reduction_page import PersonnelReductionPage


@allure.epic("人员新增减少")
@allure.feature("人员减少")
class TestPersonnelReduction(BaseUtil):

    @allure.title("人员减少")
    @pytest.mark.parametrize('args', get_xls_to_dict('test_datas.xlsx', 'personnel_reduction'))
    def test_personnel_reduction(self, args):
        pr = PersonnelReductionPage(self.driver)
        msg = pr.personnel_reduction(
            args["统一社会信用代码"],
            args["止薪时间"],
            args["减少类型"]
        )
        self.driver.assert_text("操作成功", msg)

# -*- coding=UTF-8 -*-
# @Project :        base_util.py
# @fileName         test_checked_regular_performance_level.py
# @author           Echo
# @EditTime         2024/5/16
from typing import *

import allure
import pytest

from public.common.base_util import BaseUtil
from public.common.datainfo import get_xls_to_dict
from public.pages.modules.绩效管理.checked_regular_performance_level_page import CheckedRegularPerformanceLevelPage


@allure.epic('绩效管理')
@allure.feature('核定绩效水平')
@allure.story('核定常规绩效水平')
class TestCheckedRegularPerformanceLevel(BaseUtil):

    @allure.title('新增核定常规绩效水平')
    @pytest.mark.parametrize('args', get_xls_to_dict('test_datas.xlsx', '核定常规绩效水平'))
    def test_checked_regular_performance_level(self, args):
        crpl = CheckedRegularPerformanceLevelPage(self.driver)
        msg = crpl.checked_regular_performance_level(
            args['绩效年份'],
            args['单位代码'],
            args['绩效金额']
        )
        self.driver.assert_text_contains("保存成功", msg)

    @pytest.mark.skip
    @allure.title('导出绩效水平列表')
    def test_export_performance_level_list(self):
        crpl = CheckedRegularPerformanceLevelPage(self.driver)
        msg = crpl.export_performance_level_list()
        self.driver.assert_text_contains("导出成功", msg)

    @allure.title('修改核定常规绩效水平')
    @pytest.mark.parametrize('args', get_xls_to_dict('test_datas.xlsx', '核定常规绩效水平'))
    def test_modification_performance_level(self, args):
        crpl = CheckedRegularPerformanceLevelPage(self.driver)
        msg = crpl.modification_performance_level(
            args['单位代码'],
            args['绩效年份'],
            args['修改绩效金额']
        )
        self.driver.assert_text_contains("修改成功", msg)

    @allure.title('核定常规绩效水平-附件补录')
    @pytest.mark.parametrize('args', get_xls_to_dict('test_datas.xlsx', '核定常规绩效水平'))
    def test_appendix_supplement(self, args):
        crpl = CheckedRegularPerformanceLevelPage(self.driver)
        msg = crpl.appendix_supplement(
            args['单位代码'],
            args['绩效年份']
        )
        self.driver.assert_text_contains("补录成功", msg)

    @allure.title('删除核定常规绩效水平')
    @pytest.mark.parametrize('args', get_xls_to_dict('test_datas.xlsx', '核定常规绩效水平'))
    def test_delete_performance_level(self, args):
        crpl = CheckedRegularPerformanceLevelPage(self.driver)
        msg = crpl.delete_performance_level(
            args['单位代码'],
            args['绩效年份']
        )
        self.driver.assert_text_contains("删除成功", msg)

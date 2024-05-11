# == Coding: UTF-8 ==
# @Project :        PublicInstitutionSystem
# @fileName         test_unitInfomaitionModification.py  
# @version          v0.1
# @author           LIULONG
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @WritingTime      2023/12/9 23:24
# @Software:        PyCharm
# ====/******/=====
import unittest

import allure
import pytest

from public.common.base_util import BaseUtil
from public.common.datainfo import get_xls_to_dict
from public.pages.modules.单位信息管理.unitInformationModification_page import UnitInformationModificationPage
from utils.social_unified_creditcode.succ_utils.sucreditcode import generateUnifiedSocialCreditCode


@allure.epic("信息管理")
@allure.feature("单位信息管理")
@allure.story("单位基础信息修改")
class TestUnitInfomaitionModification(BaseUtil):
    """ 单位基础信息修改 """

    @allure.title("单位基础信息修改")
    @pytest.mark.parametrize("args", get_xls_to_dict("test_datas.xlsx", "unitInformationModification"))
    def test_modification_unitInformation(self, args):
        """单位基础信息修改"""
        um = UnitInformationModificationPage(self.driver)
        msg = um.modification_unit_base_information(newGrassrootsUnitsID=generateUnifiedSocialCreditCode(),
                                                    unitName=args['单位名称'],
                                                    headOfUnit=args['单位负责人'], officeTel=args['单位电话'],
                                                    unitAddress=args['单位地址'],
                                                    postcode=args['邮编'], financialSupport=args['财政供养'],
                                                    financialRegulation=args['财政统发'],
                                                    unitFinancialCode=args['单位财政编码'],
                                                    unitProperty=args['单位性质'],
                                                    unitLevel=args['单位级别'],
                                                    whetherManager=args['是否主管单位'], auditProcess=args['审核流程'],
                                                    hardshipAreaType=args['艰边类别'],
                                                    salarySystemType=args['执行工资制度'],
                                                    membership=args['隶属关系'], unitStation=args['单位驻地'],
                                                    averageElevation=args['平均海拔'],
                                                    stationElevation=args['驻地海拔'],
                                                    typeOfPublicInstitution=args['事业单位类型'],
                                                    publicInstitutionIndustry=args['事业单位行业'],
                                                    defaultSurveyStandard=args['是否地勘单位'],
                                                    sourceOfFunds=args['经费来源'],
                                                    subsidyStandardTypeLocale=args['公务员规范后津贴标准类别驻地'])
        self.driver.assert_text(msg, "保存成功，稍后请在单位信息查看")

# == Coding: UTF-8 ==
# @Project :        PublicInstitutionSystem
# @fileName         test_unitInfomaitionModification.py  
# @version          v0.1
# @author           LIULONG
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @WritingTime      2023/12/9 23:24
# @Software:        PyCharm
# ====/******/=====
from ddt import data, ddt

from public.common.base_util import BaseUtil
from public.common.datainfo import get_xls_to_dict
from public.pages.modules.单位信息管理.unitInformationModification_page import UnitInformationModificationPage
from utils.social_unified_creditcode.succ_utils.sucreditcode import generateUnifiedSocialCreditCode


@ddt
class TestUnitInfomaitionModification(BaseUtil):
    @data(*get_xls_to_dict("unitInformationModification.xlsx", "unitInformationModification"))
    def test_07_modification_unitInformation(self, args):
        um = UnitInformationModificationPage(self.driver)
        um.modification_unit_base_information(grassrootsUnitsID=args['统一社会信用代码'],
                                              newGrassrootsUnitsID=generateUnifiedSocialCreditCode(),
                                              unitName=args['单位名称'],
                                              headOfUnit=args['单位负责人'], officeTel=args['单位电话'],
                                              unitAddress=args['单位地址'],
                                              postcode=args['邮编'], financialSupport=args['财政供养'],
                                              financialRegulation=args['财政统发'],
                                              unitFinancialCode=args['单位财政编码'], unitProperty=args['单位性质'],
                                              enforceTheWageSystem=args['执行工资制度'], unitLevel=args['单位级别'],
                                              whetherManager=args['是否主管单位'], competentUnit=args['主管单位'],
                                              auditProcess=args['审核流程'],
                                              difficultCategory=args['艰边类别'],
                                              subsidyStandardTypeArea=args['公务员规范后津贴标准类别驻地'],
                                              membership=args['隶属关系'], unitStation=args['单位驻地'],
                                              meanAltitude=args['平均海拔'],
                                              stationElevation=args['驻地海拔'],
                                              typeOfPublicInstitution=args['事业单位类型'],
                                              publicInstitutionIndustry=args['事业单位行业'],
                                              defaultSurveyStandard=args['是否地勘单位'],
                                              sourceOfFunds=args['经费来源']
                                              )

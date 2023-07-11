# == Coding: UTF-8 ==
# @Project :        BusinessWageSystem
# @fileName         test_all_case.py  
# @version          v0.1
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/6/9
# @Software:        PyCharm
# ====/******/=====
import unittest

from ddt import ddt, data
from public.common.datainfo import get_xls_to_dict
from public.common.base_util import BaseUtil
from public.pages.login_page import LoginPage
from public.pages.makeUnit_page import MakeUnitPage
from public.pages.personnelAdd_page import *
from scripts.RandomlyGeneratePersonnelInformation import *


@ddt
class TestAll(BaseUtil):
    # @unittest.skip
    # @data(*get_xls_to_dict('makeUnit.xlsx', '新建单位'))
    # def test_01_makeUnit(self, args):  # 新建单位
    #     lg = MakeUnitPage(self.driver)
    #     lg.make_unit(nest_messages_creditCode=args['统一社会信用代码'], unit_name=args['单位名称'], supervisor=args['是否主管'])

    @data(*get_xls_to_dict('addpersonnel.xlsx', '新增管理人员'))
    def test_02_add_manager(self, args):  # 新增管理人员
        am = PersonnelAddPage(self.driver)
        am.add_manager_page(
            dentityPersonne=args['人员身份'], salaryDate=args['起薪时间'], name=generate_name(), gender=args['性别'],
            # 随机生成姓名，身份证号
            nationality=args['民族'],
            idCard=generate_idcard(), politicalStatus=args['政治面貌'], initialPersonnelIdentity=args['初始人员身份'],
            birthplace=args['籍贯'], address=args['住址'], personnelSource=args['人员来源'],
            entryUnitTime=args['进入本单位时间'], enterDate=args['参加工作时间'], internalMechanism=args['所属机构'],
            remarks=args['人员备注'],
            personnelFinanceCode=args['人员财政编码'], education=args['学历'], degree=args['学位'],
            graduationTime=args['毕业时间'],
            localRankSequence=args['地方职级序列'], periodOfStudy=args['学段'], socialSecurityNumber=args['社会保障号'],
            surveyStandard=args['是否地勘'], position=args['现任职务'],
            positionTime=args['现任职务时间'], actualPost=args['实际岗位'], rankOfStaff=args['职员等级'],
            rankOffStaff_time=args['任职员等级时间'],
            postWage=args['基本工资对应岗位'], actualPostTime=args['任现岗位时间'], payScale=args['薪级'],
            payScaleTime=args['薪级起考年限'],
            primaryAndHighSchoolTeacher=args['是否中小学教师'], nurse=args['是否护士'], tg10wage=args['是否提高10%'],
            specialEducation=args['是否特殊教育'], jbt=args['津补贴值'], jx=args['绩效值']
        )

    @data(*get_xls_to_dict('addpersonnel.xlsx', '新增专业技术人员'))
    def test_03_add_professionalSkill(self, args):  # 新增专业技术人员
        am = PersonnelAddPage(self.driver)
        am.add_professionalSkill_page(
            dentityPersonne=args['人员身份'], salaryDate=args['起薪时间'], name=generate_name(), gender=args['性别'],
            # 随机生成姓名，身份证号
            nationality=args['民族'],
            idCard=generate_idcard(), politicalStatus=args['政治面貌'], initialPersonnelIdentity=args['初始人员身份'],
            birthplace=args['籍贯'], address=args['住址'], personnelSource=args['人员来源'],
            entryUnitTime=args['进入本单位时间'], enterDate=args['参加工作时间'], internalMechanism=args['所属机构'],
            remarks=args['人员备注'],
            personnelFinanceCode=args['人员财政编码'], education=args['学历'], degree=args['学位'],
            graduationTime=args['毕业时间'],
            full_time=args['专职情况'], periodOfStudy=args['学段'], socialSecurityNumber=args['社会保障号'],
            surveyStandard=args['是否地勘'], compulsoryEducation=args['是否义务教育教师'], position=args['现任职务'],
            positionTime=args['现任职务时间'], actualPost=args['实际岗位'],
            postWage=args['基本工资对应岗位'], actualPostTime=args['任现岗位时间'], payScale=args['薪级'],
            payScaleTime=args['薪级起考年限'],
            primaryAndHighSchoolTeacher=args['是否中小学教师'], nurse=args['是否护士'], tg10wage=args['是否提高10%'],
            specialEducation=args['是否特殊教育'], jbt=args['津补贴值'], jx=args['绩效值']
        )

    @data(*get_xls_to_dict('addpersonnel.xlsx', '新增事业技术工人'))
    def test_04_add_skilledWorker(self, args):  # 新增事业技术工人
        am = PersonnelAddPage(self.driver)
        am.add_skilledWorker_page(
            dentityPersonne=args['人员身份'], salaryDate=args['起薪时间'], name=generate_name(), gender=args['性别'],
            # 随机生成姓名，身份证号
            nationality=args['民族'],
            idCard=generate_idcard(), politicalStatus=args['政治面貌'], initialPersonnelIdentity=args['初始人员身份'],
            birthplace=args['籍贯'], address=args['住址'], personnelSource=args['人员来源'],
            entryUnitTime=args['进入本单位时间'], enterDate=args['参加工作时间'], internalMechanism=args['所属机构'],
            remarks=args['人员备注'],
            personnelFinanceCode=args['人员财政编码'], education=args['学历'], degree=args['学位'],
            graduationTime=args['毕业时间'],
            technicalCertificate=args['是否取得技术证书'], periodOfStudy=args['学段'],
            socialSecurityNumber=args['社会保障号'],
            surveyStandard=args['是否地勘'], position=args['现任职务'],
            positionTime=args['现任职务时间'], actualPost=args['实际岗位'],
            postWage=args['基本工资对应岗位'], actualPostTime=args['任现岗位时间'], payScale=args['薪级'],
            payScaleTime=args['薪级起考年限'],
            specialEducation=args['是否特殊教育'], jbt=args['津补贴值'], jx=args['绩效值']
        )

    @data(*get_xls_to_dict('addpersonnel.xlsx', '新增事业普通工人'))
    def test_05_add_ordinaryWorker(self, args):  # 新增事业普通工人
        am = PersonnelAddPage(self.driver)
        am.add_ordinaryWorker_page(
            dentityPersonne=args['人员身份'], salaryDate=args['起薪时间'], name=generate_name(), gender=args['性别'],
            # 随机生成姓名，身份证号
            nationality=args['民族'],
            idCard=generate_idcard(), politicalStatus=args['政治面貌'], initialPersonnelIdentity=args['初始人员身份'],
            birthplace=args['籍贯'], address=args['住址'], personnelSource=args['人员来源'],
            entryUnitTime=args['进入本单位时间'], enterDate=args['参加工作时间'], internalMechanism=args['所属机构'],
            remarks=args['人员备注'],
            personnelFinanceCode=args['人员财政编码'], education=args['学历'], degree=args['学位'],
            graduationTime=args['毕业时间'],
            periodOfStudy=args['学段'],
            socialSecurityNumber=args['社会保障号'],
            surveyStandard=args['是否地勘'], position=args['现任职务'],
            positionTime=args['现任职务时间'], actualPost=args['实际岗位'],
            postWage=args['基本工资对应岗位'], actualPostTime=args['任现岗位时间'], payScale=args['薪级'],
            payScaleTime=args['薪级起考年限'],
            specialEducation=args['是否特殊教育'], jbt=args['津补贴值'], jx=args['绩效值']
        )

    @data(*get_xls_to_dict('addpersonnel.xlsx', '新增运动员'))
    def test_06_add_sportsman(self, args):  # 新增运动员
        am = PersonnelAddPage(self.driver)
        am.add_sportsman_page(
            dentityPersonne=args['人员身份'], salaryDate=args['起薪时间'], name=generate_name(), gender=args['性别'],
            # 随机生成姓名，身份证号
            nationality=args['民族'],
            idCard=generate_idcard(), politicalStatus=args['政治面貌'], initialPersonnelIdentity=args['初始人员身份'],
            birthplace=args['籍贯'], address=args['住址'], personnelSource=args['人员来源'],
            entryUnitTime=args['进入本单位时间'], enterDate=args['参加工作时间'], internalMechanism=args['所属机构'],
            remarks=args['人员备注'], socialSecurityNumber=args['社会保障号'],
            personnelFinanceCode=args['人员财政编码'], education=args['学历'], degree=args['学位'],
            graduationTime=args['毕业时间'], calledTime=args['选招时间'], whetherMain=args['是否主力'],
            trueProRankId=args['实际基础津贴档次'],
            formerSalaryMappingProRankId=args['基本工资对应基础津贴档次'], formerSalaryRank=args['成绩津贴层次'],
            formerSalaryGrade=args['成绩津贴名次'],
            rankingDate=args['成绩津贴名次取得时间'], jbt=args['津补贴值'], jx=args['绩效值']
        )

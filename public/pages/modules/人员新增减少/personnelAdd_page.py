# == Coding: UTF-8 ==
# @Project :        BusinessWageSystem
# @fileName         personnelAdd_page.py  
# @version          v0.2
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/6/9
# @Software:        PyCharm
# ====/******/=====
import time

import allure
from selenium.webdriver.common.by import By

from config.globalparam import datas_path
from public.common.base_page import BasePage
from utils.files_upload import upload_file


class PersonnelAddPage(BasePage):
    _manager_menu_loc = 'xpath->//div[contains(text(),"管理版")]'
    _businessAudit_menu_loc = 'xpath->//span[contains(text(),"业务审核")]'
    _businessGuidance_menu_loc = "xpath->//span[contains(text(), '业务指导(基层)')]/ancestor::a"
    _add_decrease_loc = 'xpath->//ul[@class="menu-root"]/li[4]/div'
    _add_menu_loc = 'xpath->//div[@class="menu-sub ng-star-inserted"]/ul/li[1]/a'
    _query_org_input_loc = 'name->queryStr'
    _orgcode_link_loc = 'xpath->//tbody[@class="ant-table-tbody"]/tr[2]/td[1]/a'
    _personnel_identity_loc = 'css->nz-select[formcontrolname="personalIdentityId"] input'
    _qxDate_input_loc = 'css->lib-date-input[formcontrolname="qxDate"] input'
    _bySymbol_input_loc = 'xpath->//lib-staff-head/form[1]/nz-form-item[3]/nz-form-control[1]/div[1]/div[1]/input[1]'
    _changeRemarks_input_loc = 'xpath->//lib-staff-head/form[1]/nz-form-item[4]/nz-form-control[1]/div[1]/div[1]/input[1]'
    _attachment_btn_loc = "xpath->//span[contains(text(),'工资报审附件')]"
    _upload_btn_loc = "xpath->(//span[contains(text(),'上传附件')])[1]/ancestor::button"
    _upload_file_msg_loc = "xpath->//div/span[contains(text(),'附件示例.png')]"
    _save_attachment_btn_loc = 'css->div.ant-modal-footer button.ant-btn-primary'
    _staffName_input_loc = 'xpath->//input[@formcontrolname="staffName"]'
    _gender_input_loc = 'css->nz-select[formcontrolname="gender"]'
    _select_nation_loc = 'css->nz-select[formcontrolname="nationId"]'
    _input_idcard_loc = 'xpath->//input[@formcontrolname="identityCard"]'
    _input_birthday_loc = 'css->lib-date-input[formcontrolname="birthDate"] input'
    _select_politicalStatus_loc = 'css->nz-select[formcontrolname="politicalStatusId"]'
    _select_initialPersonality_loc = 'css->nz-select[formcontrolname="initialPersonalIdentityId"]'
    _input_nativePlace_loc = 'xpath->//input[@formcontrolname="nativePlace"]'
    _input_address_loc = 'xpath->//textarea[@formcontrolname="address"]'
    _select_staffSource_loc = 'css->nz-select[formcontrolname="staffSourceTypeId"]'
    _input_joinDate_loc = 'css->lib-date-input[formcontrolname="joinDate"] input'
    _select_department_loc = 'css->nz-select[formcontrolname="departmentId"]'
    _input_staffRemark_loc = 'xpath->//textarea[@formcontrolname="staffRemark"]'
    _input_enterDate_loc = 'css->lib-date-input[formcontrolname="enterDate"] input'
    _select_education_loc = 'css->nz-select[formcontrolname="educationTypeId"]'
    _select_degree_loc = 'css->nz-select[formcontrolname="degreeTypeId"]'
    _input_graduateDate_loc = 'css->lib-date-input[formcontrolname="graduateDate"] input'
    _click_wage_info_btn_loc = 'xpath->//div[contains(text(),"工资信息")]'
    _select_surveyStandard_loc = 'css->nz-select[formcontrolname="surveyStandard"]'
    _select_compulsoryEducation_loc = 'css->nz-select[formcontrolname="compulsoryEducation"]'
    _input_presentOccupation_loc = 'xpath->//input[@formcontrolname="presentOccupation"]'
    _input_presentOccupationDate_loc = 'css->lib-date-input[formcontrolname="presentOccupationDate"] input'
    _select_trueProRank_loc = 'css->nz-select[formcontrolname="trueProRankId"]'
    _select_levelProRank_loc = 'css->nz-select[formcontrolname="levelProRankId"]'
    _input_levelDate_loc = 'css->lib-date-input[formcontrolname="levelDate"] input'
    _select_salaryMappingProRank_loc = 'css->nz-select[formcontrolname="salaryMappingProRankId"]'
    _select_leadership_loc = 'css->nz-select[formcontrolname="leadership"]'
    _input_jobNowDate_loc = 'css->lib-date-input[formcontrolname="jobNowDate"] input'
    _select_formerSalaryGrade_loc = 'css->nz-select[formcontrolname="formerSalaryGrade"]'
    _input_salaryGradeDate_loc = 'css->lib-date-input[formcontrolname="salaryGradeDate"] input'
    _select_primaryAndHighSchoolTeacher_loc = 'css->nz-select[formcontrolname="primaryAndHighSchoolTeacher"]'
    _select_nurse_loc = 'css->nz-select[formcontrolname="nurse"]'
    _select_tg10wage_loc = 'css->nz-select[formcontrolname="tg10wage"]'
    _select_specialEducation_loc = 'css->nz-select[formcontrolname="specialEducation"]'
    _input_hgzbl_loc = 'css->.wage-cont:nth-child(2) div.ng-star-inserted:nth-child(1) input'
    _input_retire_sports_man_hold_loc = 'css->.wage-cont:nth-child(2) div.ng-star-inserted:nth-child(2) input'
    _input_jh10percent_hold_loc = 'css->.wage-cont:nth-child(2) div.ng-star-inserted:nth-child(3) input'
    _input_employee_level_retention_loc = 'css->.wage-cont:nth-child(2) div.ng-star-inserted:nth-child(4) input'
    _click_annual_btn_loc = 'xpath->//span[contains(text(),"年度考核")]/ancestor::button'
    _click_annual_determine_btn_loc = 'xpath->//span[contains(text(),"确认")]/ancestor::button'
    _save_addPerson_btn_loc = "xpath->//div[@class='staff-head-warp']//button[@class='ant-btn ant-btn-primary']"
    _add_msg_loc = 'css->.ant-message span'

    def _click_manager_menu(self):
        with allure.step("点击管理版按钮"):
            self.driver.click(self._manager_menu_loc)  # 点击管理版按钮

    def _switch_to_basic_unit(self, org_code):
        with allure.step("进入基层单位"):
            self.business_guidance_grass_roots(org_code)  # 进入基层单位

    def _click_addstaff_menu(self):
        with allure.step("点击人员新增按钮"):
            self.driver.switch_to_new_window()  # 跳转新窗口
            self.driver.move_to_element(self._add_decrease_loc)  # 悬停在人员新增减少菜单上
            self.driver.click(self._add_menu_loc)  # 点击人员新增

    def _select_stafftype(self, identity):
        """ 选择人员身份 """
        with allure.step("选择人员身份"):
            self.driver.htmlSelect(self._personnel_identity_loc, identity)  # 选择人员身份

    def _input_qxDate(self, qxDate):
        """ 输入起薪时间 """
        with allure.step("输入起薪时间"):
            self.driver.clear_and_input(self._qxDate_input_loc, qxDate)  # 输入起薪时间

    def _input_bySymbol(self, msg):
        """ 输入依据文号 """
        if msg is not None:
            with allure.step("输入依据文号"):
                self.driver.input(self._bySymbol_input_loc, msg)  # 输入依据文号

    def _input_change_remarks(self, msg):
        """ 变动备注 """
        if msg is not None:
            with allure.step("输入变动备注"):
                self.driver.input(self._changeRemarks_input_loc, msg)

    def _uploadAttachment(self):
        """ 上传附件 """
        with allure.step("上传附件"):
            self.driver.salary_report_attachment()

    def _input_staffName(self, name):
        """输入人员姓名"""
        with allure.step("输入人员姓名"):
            self.driver.input(self._staffName_input_loc, name)

    def _select_gender(self, gender):
        """ 选择性别 """
        with allure.step("选择性别"):
            self.driver.htmlSelect(self._gender_input_loc, gender)

    def _select_nationality(self, nationality):
        """ 选择民族 """
        with allure.step("选择民族"):
            self.driver.htmlSelect(self._select_nation_loc, nationality)

    def _input_idcard(self, idcard):
        """ 输入身份证号 """
        with allure.step("输入身份证号"):
            self.driver.input(self._input_idcard_loc, idcard)

    def _input_birthday(self, birthday):
        """ 输入出生日期 """
        with allure.step("输入出生日期"):
            self.driver.clear_and_input(self._input_birthday_loc, birthday)

    def _select_politicalStatus(self, politicalStatus):
        """ 选择政治面貌 """
        with allure.step("选择政治面貌"):
            self.driver.htmlSelect(self._select_politicalStatus_loc, politicalStatus)

    def _select_initialPersonality(self, initialPersonality):
        """ 选择初始人员身份 """
        if initialPersonality is not None:
            with allure.step("选择初始人员身份"):
                self.driver.htmlSelect(self._select_initialPersonality_loc, initialPersonality)

    def _input_nativePlace(self, nativePlace):
        """ 输入籍贯 """
        if nativePlace is not None:
            with allure.step("输入籍贯"):
                self.driver.input(self._input_nativePlace_loc, nativePlace)

    def _input_address(self, address):
        """ 输入地址 """
        if address is not None:
            with allure.step("输入地址"):
                self.driver.input(self._input_address_loc, address)

    def _select_staffSource(self, staffSource):
        """ 选择人员来源 """
        with allure.step("选择人员来源"):
            self.driver.htmlSelect(self._select_staffSource_loc, staffSource)

    def _input_joinDate(self, joinDate):
        """ 进入本单位时间 """
        with allure.step("输入进入本单位时间"):
            self.driver.clear_and_input(self._input_joinDate_loc, joinDate)

    def _select_department(self, department):
        """ 选择内设机构 """
        if department is not None:
            with allure.step("选择内设机构"):
                self.driver.htmlSelect(self._select_department_loc, department)

    def _input_staffRemark(self, staffRemark):
        """ 输入备注 """
        if staffRemark is not None:
            with allure.step("输入备注"):
                self.driver.input(self._input_staffRemark_loc, staffRemark)

    def _input_enterDate(self, enterDate):
        """ 参工时间 """
        with allure.step("输入参工时间"):
            self.driver.clear_and_input(self._input_enterDate_loc, enterDate)

    def _select_education(self, education):
        """ 选择学历 """
        with allure.step("选择学历"):
            self.driver.htmlSelect(self._select_education_loc, education)

    def _select_degree(self, degree):
        """ 选择学位 """
        if degree is not None:
            with allure.step("选择学位"):
                self.driver.htmlSelect(self._select_degree_loc, degree)

    def _input_graduateDate(self, graduateDate):
        """ 毕业时间 """
        with allure.step("输入毕业时间"):
            self.driver.clear_and_input(self._input_graduateDate_loc, graduateDate)

    def _click_wage_info(self):
        """ 点击工资信息 """
        with allure.step("点击工资信息按钮"):
            self.driver.click(self._click_wage_info_btn_loc)

    def _select_surveyStandard(self, surveyStandard):
        """ 是否地勘标准 """
        if surveyStandard == "是":
            with allure.step("选择是否地勘标准"):
                self.driver.htmlSelect(self._select_surveyStandard_loc, surveyStandard)

    def _select_compulsoryEducation(self, compulsoryEducation, identity, surveyStandard):
        """ 是否义务教育教师 """
        if identity == "专业技术人员" and surveyStandard == "否":
            with allure.step("选择是否义务教育教师"):
                self.driver.htmlSelect(self._select_compulsoryEducation_loc, compulsoryEducation)

    def _input_presentOccupation(self, presentOccupation):
        """ 输入现任职务 """
        with allure.step("输入现任职务"):
            self.driver.input(self._input_presentOccupation_loc, presentOccupation)

    def _input_presentOccupationDate(self, presentOccupationDate):
        """ 输入现任职务时间 """
        with allure.step("输入现任职务时间"):
            self.driver.clear_and_input(self._input_presentOccupationDate_loc, presentOccupationDate)

    def _select_trueProRank(self, trueProRank):
        """ 实际岗位 """
        with allure.step("选择实际岗位"):
            self.driver.htmlSelect(self._select_trueProRank_loc, trueProRank)

    def _select_levelProRank(self, levelProRank, identity):
        """ 职员等级 """
        if levelProRank is not None and identity == "管理人员" and self.driver.element_exists(
                self._select_levelProRank_loc):
            with allure.step("选择职员等级"):
                self.driver.htmlSelect(self._select_levelProRank_loc, levelProRank)

    def _input_levelProRankDate(self, levelProRankDate, identity):
        """ 任职员等级时间 """
        if levelProRankDate is not None and identity == "管理人员" and self.driver.element_exists(
                self._input_levelDate_loc):
            self.driver.clear_and_input(self._input_levelDate_loc, levelProRankDate)

    def _select_salaryMappingProRank(self, salaryMappingProRank):
        """ 基本工资对应岗位 """
        with allure.step("选择基本工资对应岗位"):
            self.driver.htmlSelect(self._select_salaryMappingProRank_loc, salaryMappingProRank)

    def _select_leadership(self, leadership, salaryMappingProRank):
        """ 是否领导工资 """
        if salaryMappingProRank in ['四级岗位', '五级岗位'] and self.driver.element_exists(self._select_leadership_loc):
            with allure.step("选择是否领导工资"):
                self.driver.htmlSelect(self._select_leadership_loc, leadership)

    def _input_jobNowDate(self, jobNowDate):
        """ 任现岗位时间 """
        with allure.step("输入任现岗位时间"):
            self.driver.clear_and_input(self._input_jobNowDate_loc, jobNowDate)

    def _select_formerSalaryGrade(self, formerSalaryGrade):
        """ 薪级 """
        with allure.step("选择薪级"):
            self.driver.htmlSelect(self._select_formerSalaryGrade_loc, formerSalaryGrade)

    def _input_salaryGradeDate(self, salaryGradeDate):
        """ 起薪时间 """
        with allure.step("输入起薪时间"):
            self.driver.clear_and_input(self._input_salaryGradeDate_loc, salaryGradeDate)

    def _select_primaryAndHighSchoolTeacher(self, primaryAndHighSchoolTeacher, compulsoryEducation):
        """ 是否中小学教师 """
        if primaryAndHighSchoolTeacher is not None and compulsoryEducation == "否":
            with allure.step("选择是否中小学教师"):
                self.driver.htmlSelect(self._select_primaryAndHighSchoolTeacher_loc, primaryAndHighSchoolTeacher)

    def _select_nurse(self, nurse, compulsoryEducation):
        """ 是否护士 """
        if nurse is not None and compulsoryEducation == "否":
            with allure.step("选择是否护士"):
                self.driver.htmlSelect(self._select_nurse_loc, nurse)

    def _select_tg10wage(self, tg10wage, primaryAndHighSchoolTeacher, nurse, compulsoryEducation):
        """ 是否提高10% """
        if tg10wage is not None and (
                primaryAndHighSchoolTeacher == "是" or nurse == "是") and compulsoryEducation == "否":
            with allure.step("选择是否提高10%工资"):
                self.driver.htmlSelect(self._select_tg10wage_loc, tg10wage)

    def _select_specialEducation(self, specialEducation):
        """ 是否特殊教育 """
        if specialEducation is not None:
            with allure.step("选择是否特殊教育"):
                self.driver.htmlSelect(self._select_specialEducation_loc, specialEducation)

    def _input_hgzbl(self, hgzbl):
        """ 保留原特殊岗位 """
        if hgzbl is not None:
            with allure.step("输入保留原特殊岗位"):
                self.driver.input(self._input_hgzbl_loc, int(hgzbl))

    def _input_retireSportsManHold(self, retireSportsManHold):
        """ 退役运动员保留工资额度 """
        if retireSportsManHold is not None:
            with allure.step("输入退役运动员保留工资额度"):
                self.driver.input(self._input_retire_sports_man_hold_loc, int(retireSportsManHold))

    def _input_jh10percentHold(self, jh10percentHold):
        """ 中小学教师或护士保留原额10% """
        if jh10percentHold is not None:
            with allure.step("输入中小学教师或护士保留原额10%"):
                self.driver.input(self._input_jh10percent_hold_loc, int(jh10percentHold))

    def _input_employeeLevelRetention(self, employeeLevelRetention):
        """ 原职员等级保留绝对额 """
        if employeeLevelRetention is not None:
            with allure.step("输入原职员等级保留绝对额"):
                self.driver.input(self._input_employee_level_retention_loc, int(employeeLevelRetention))

    def _click_annual(self):
        """ 点击年度考核 """
        with allure.step("点击年度考核按钮"):
            self.driver.click(self._click_annual_btn_loc)

    def _determine_annual(self):
        """ 确定年度考核 """
        if self.driver.element_exists(self._click_annual_determine_btn_loc):
            with allure.step("点击确定年度考核"):
                self.driver.click(self._click_annual_determine_btn_loc)

    def _click_save(self):
        """ 点击保存 """
        with allure.step("点击保存按钮"):
            self.driver.click(self._save_addPerson_btn_loc)

    def _get_addPerson_msg(self):
        """ 获取新增人员提示信息 """
        with allure.step("获取新增人员提示信息"):
            return self.driver.get_text(self._add_msg_loc)

    def add_staff(self, org_code, identity, qxDate, bySymbol_msg, change_remarks_msg, name, gender, nationality, idcard,
                  birthday, politicalStatus, initialPersonality, nativePlace, address, staffSource, joinDate,
                  department, staffRemark, enterDate, education, degree, graduateDate, surveyStandard,
                  compulsoryEducation,
                  presentOccupation, presentOccupationDate, trueProRank, levelProRank, levelProRankDate,
                  salaryMappingProRank, leadership, jobNowDate, formerSalaryGrade,
                  salaryGradeDate, primaryAndHighSchoolTeacher, nurse, tg10wage, specialEducation, hgzbl,
                  retireSportsManHold, jh10percentHold, employeeLevelRetention):
        """
        人员新增业务组合
        :param org_code: 统一社会信用代码
        :param identity: 人员身份
        :param qxDate: 起薪时间
        :param bySymbol_msg: 依据文号
        :param change_remarks_msg: 变更备注
        :param name: 人员姓名
        :param gender: 性别
        :param nationality: 民族
        :param idcard: 身份证号
        :param birthday: 出生日期
        :param politicalStatus: 政治面貌
        :param initialPersonality: 初始人员身份
        :param nativePlace: 籍贯
        :param address: 地址
        :param staffSource: 人员来源
        :param joinDate: 进入本单位时间
        :param department: 内设机构
        :param staffRemark: 备注
        :param enterDate: 参公时间
        :param education: 学历
        :param degree: 学位
        :param graduateDate: 毕业时间
        :param surveyStandard: 是否执行地勘标准
        :param compulsoryEducation: 是否中小学教师
        :param presentOccupation: 现任职务
        :param presentOccupationDate: 现任职务时间
        :param trueProRank: 实际岗位
        :param levelProRank: 职员等级
        :param levelProRankDate: 任职员等级时间
        :param salaryMappingProRank: 基本工资对应岗位
        :param leadership: 是否领导工资
        :param jobNowDate: 任现岗位时间
        :param formerSalaryGrade: 薪级
        :param salaryGradeDate: 起薪时间
        :param primaryAndHighSchoolTeacher: 是否中小学教师
        :param nurse: 是否护士
        :param tg10wage: 是否提高10%
        :param specialEducation: 是否特殊教育
        :param hgzbl: 保留原特殊岗位
        :param retireSportsManHold: 退役运动员保留工资额度
        :param jh10percentHold: 中小学教师或护士保留原额10%
        :param employeeLevelRetention: 原职员等级保留绝对额
        """
        self._click_manager_menu()  # 点击管理版按钮
        self._switch_to_basic_unit(org_code)  # 进入基层单位
        self._click_addstaff_menu()
        self._select_stafftype(identity)
        self._input_qxDate(qxDate)
        self._input_bySymbol(bySymbol_msg)
        self._input_change_remarks(change_remarks_msg)
        self._input_staffName(name)
        self._select_gender(gender)
        self._select_nationality(nationality)
        self._input_idcard(idcard)
        self._input_birthday(birthday)
        self._select_politicalStatus(politicalStatus)
        self._select_initialPersonality(initialPersonality)
        self._input_nativePlace(nativePlace)
        self._input_address(address)
        self._select_staffSource(staffSource)
        self._input_joinDate(joinDate)
        self._select_department(department)
        self._input_staffRemark(staffRemark)
        self._input_enterDate(enterDate)
        self._select_education(education)
        self._select_degree(degree)
        self._input_graduateDate(graduateDate)
        self._uploadAttachment()
        self._click_wage_info()
        self._select_surveyStandard(surveyStandard)
        self._select_compulsoryEducation(compulsoryEducation, identity, surveyStandard)
        self._input_presentOccupation(presentOccupation)
        self._input_presentOccupationDate(presentOccupationDate)
        self._select_trueProRank(trueProRank)
        self._select_levelProRank(levelProRank, identity)
        self._input_levelProRankDate(levelProRankDate, identity)
        self._select_salaryMappingProRank(salaryMappingProRank)
        self._select_leadership(leadership, salaryMappingProRank)
        self._input_jobNowDate(jobNowDate)
        self._select_formerSalaryGrade(formerSalaryGrade)
        self._input_salaryGradeDate(salaryGradeDate)
        self._select_primaryAndHighSchoolTeacher(primaryAndHighSchoolTeacher, compulsoryEducation)
        self._select_nurse(nurse, compulsoryEducation)
        self._select_tg10wage(tg10wage, primaryAndHighSchoolTeacher, nurse, compulsoryEducation)
        self._select_specialEducation(specialEducation)
        self._input_hgzbl(hgzbl)
        self._input_retireSportsManHold(retireSportsManHold)
        self._input_jh10percentHold(jh10percentHold)
        self._input_employeeLevelRetention(employeeLevelRetention)
        self._click_annual()
        self._determine_annual()
        self._click_save()
        return self._get_addPerson_msg()

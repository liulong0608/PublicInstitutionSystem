# -*- coding: UTF-8 -*-
"""
**    @Project :        PublicInstitutionSystem
**    @fileName         createUnitPage.py
**    @author           Echo
**    @EditTime         2024/1/17
"""
import time
from typing import *

from selenium.webdriver.common.by import By

from config.globalparam import file_path
from public.common.base_page import BasePage


class CreateUnitPage(BasePage):
    """ 新建单位 """
    _makeUnit_btn_loc = 'xpath->//*[@id="root"]/section/section/main/div[1]/div[3]/div/div/div[2]/div[1]'
    _orgcode_loc = 'id->nest-messages_creditCode'
    _unit_name_loc = 'id->nest-messages_organizationName'
    _supervisor_loc = 'xpath->//div[@class="ant-select-selector"]'
    _save_btn_loc = 'xpath->//div[@class="unit_add_head__fNOk6"]/button[1]'  # 保存
    _createUnit_msg = 'xpath->//div[@class="ant-modal-content"]/div/div/div/div'  # 保存成功断言信息
    _maintain_btn_loc = 'xpath->//div[@class="ant-modal-confirm-btns"]/button[2]'  # 前往维护按钮

    _unitInformationManagement__btn_loc = 'css->.ant-card:nth-child(3) .home_auto_btn__LBhkK:nth-child(2)'
    _query_loc = 'name->queryStr'
    _queryBtn_loc = 'xpath->//div[@class="ant-row"]/nz-form-item[7]/nz-form-control/div/div/nz-button-group/button[1]'
    _orgCode_loc = 'xpath->//tbody[@class="ant-table-tbody"]/tr[2]/td[2]'
    _orgInfo_btn_loc = 'xpath->//div[@class="btn"]/button[1]'
    _input_orgcode_loc = 'xpath->//input[@formcontrolname="organizationCode"]'
    _input_orgName_loc = 'xpath->//input[@formcontrolname="organizationName"]'
    _input_headOfUnit_loc = 'xpath->//input[@formcontrolname="head"]'
    _input_phone_loc = 'xpath->//input[@formcontrolname="telephone"]'
    _input_address_loc = 'xpath->//input[@formcontrolname="address"]'
    _input_postcode_loc = 'xpath->//input[@formcontrolname="zipCode"]'
    _select_financialSupport_loc = 'xpath->//nz-select[@formcontrolname="financialSupportType"]'
    _select_financialRegulation_loc = 'xpath->//nz-select[@formcontrolname="financialPaymentType"]'
    _input_unitFinancialCode_loc = 'xpath->//input[@formcontrolname="financialCode"]'
    _select_unitProperty_loc = 'xpath->//nz-select[@formcontrolname="organizationTypeId"]'
    _select_salarySystem_loc = 'xpath->//nz-select[@formcontrolname="salarySystemType"]'
    _select_unitLevel_loc = 'xpath->//nz-select[@formcontrolname="gradeId"]'
    _click_isManager_loc = 'xpath->//nz-radio-group[@formcontrolname="supervisor"]/label[1]/span[1]/input'
    _click_noManager_loc = 'css->nz-radio-group[formcontrolname="supervisor"] label:nth-child(2) span:nth-child(1) input'
    _input_managerUnit_loc = ('xpath->//nz-select[@formcontrolname="supervisorOrganizationId"]/nz-select-top-control'
                              '/nz-select-search/input')
    _click_managerUnit_loc = 'xpath->//nz-select[@formcontrolname="supervisorOrganizationId"]'
    _select_auditProcess_loc = 'xpath->//nz-select[@formcontrolname="auditProcess"]'
    _select_hardshipArea_loc = 'xpath->//nz-select[@formcontrolname="hardshipAreaTypeId"]'
    _select_subsidyStandardTypeLocale_loc = 'xpath->//lib-cascader-wrap[@formcontrolname="subsidyStandardTypeLocaleId"]'
    _select_membership_loc = 'xpath->//nz-select[@formcontrolname="subordinationCodeId"]'
    _click_unitStation_loc = 'xpath->//lib-cascader-wrap[@formcontrolname="localeId"]'
    _select_averageElevation_loc = 'xpath->//nz-select[@formcontrolname="localeAverageElevationId"]'
    _select_stationElevation_loc = 'xpath->//nz-select[@formcontrolname="localeElevationId"]'
    _select_typeOfPublicInstitution_loc = 'xpath->//nz-select[@formcontrolname="institutionTypeId"]'
    _select_publicInstitutionIndustry_loc = 'xpath->//nz-tree-select[@formcontrolname="institutionIndustryId"]/div/nz-select-search/input'
    _select_defaultSurveyStandard_loc = 'xpath->//nz-select[@formcontrolname="defaultSurveyStandard"]'
    _select_sourceOfFunds_loc = 'xpath->//nz-select[@formcontrolname="financialSourceTypeId"]'
    _attachment_btn_loc = 'xpath->//span[contains(text(),"附件上传")]'
    _input_attachment_loc = ("xpath->/html/body/div/div[3]/div/nz-modal-container/div/div/div["
                             "2]/nz-space/nz-space-item[1]/lib-attach-list/nz-list/nz-list-header/div/div["
                             "2]/nz-space/nz-space-item[1]/nz-upload/div/div/input")
    _save_attachment_btn_loc = 'css->div.ant-modal-footer button.ant-btn-primary'
    _save_modify_btn_loc = 'xpath->//div[@class="ant-tabs-content-holder"]/div/div/lib-unit-basis/button'
    _save_msg_loc = 'css->.ant-message span'

    _operator_btn_loc = "xpath->//div[contains(text(),'单位经办人信息')]"
    _create_btn_loc = "xpath->//span[contains(text(),'新建账号')]"
    _input_username_loc = "xpath->//input[@formcontrolname='userName']"
    _input_name_loc = "xpath->//input[@formcontrolname='userNickName']"
    _select_gender_loc = "xpath->//nz-select[@formcontrolname='gender']"
    _input_identityCard_loc = "xpath->//input[@formcontrolname='identityCard']"
    _input_phoneNumber_loc = "xpath->//input[@formcontrolname='phoneNumber']"
    _set_jurisdiction_loc = "css->nz-card[nztitle='权限选择'] div.ant-card-body div:nth-child(1)"
    _save_operator_btn_loc = "xpath->//span[contains(text(),'保存')]/ancestor::button"
    _save_operator_msg_loc = "css->.ant-modal-footer span.foot_msg"

    def _swith_to_home(self):
        self.open_url('http://192.168.2.194/console/home')

    def _switch_to_creat(self):
        """
        点击新建单位按钮
        """
        self.click(self._makeUnit_btn_loc)

    def _input_unit_code(self, nest_messages_creditCode):
        """
        输入单位社会信用代码
        """
        self.input(self._orgcode_loc, nest_messages_creditCode)

    def _input_unit_name(self, unit_name):
        """
        输入单位名称
        """
        self.input(self._unit_name_loc, unit_name)

    def _select_whetherToBeInCharge(self, supervisor):
        """
        选择是否主管单位
        """
        self.click(self._supervisor_loc)
        self.click(f"xpath->//div[@title='{supervisor}']")

    def _click_save(self):
        """
        点击保存
        """
        self.click(self._save_btn_loc)

    def _get_createUnit_msg(self):
        """
        获取保存成功提示
        """
        return self.get_text(self._createUnit_msg)

    def _swith_to_maintain(self):
        """
        点击维护单位信息按钮
        """
        self.click(self._maintain_btn_loc)

    def _input_headOfUnit(self, headOfUnit):
        self.input(self._input_headOfUnit_loc, headOfUnit)

    def _input_phone(self, officeTel):
        self.input(self._input_phone_loc, officeTel)

    def _input_address(self, unitAddress):
        self.input(self._input_address_loc, unitAddress)

    def _input_postcode(self, postcode):
        self.input(self._input_postcode_loc, postcode)

    def _select_financialSupport(self, financialSupportType):
        self.htmlSelect(self._select_financialSupport_loc, financialSupportType)

    def _select_financialRegulation(self, financialRegulation):
        self.htmlSelect(self._select_financialRegulation_loc, financialRegulation)

    def _input_unitFinancialCode(self, financialCode):
        if financialCode is not None:
            self.input(self._input_unitFinancialCode_loc, financialCode)

    def _select_unitProperty(self, unitProperty):
        self.htmlSelect(self._select_unitProperty_loc, unitProperty)

    def _select_typeOfPublicInstitution(self, institutionType):
        self.htmlSelect(self._select_typeOfPublicInstitution_loc, institutionType)

    def _select_publicInstitutionIndustry(self, industry):
        self.input(self._select_publicInstitutionIndustry_loc, industry)
        self.click(f'xpath->//nz-tree-node-title[@title="{industry}"]')

    def _select_defaultSurveyStandard(self, surveyStandard):
        self.htmlSelect(self._select_defaultSurveyStandard_loc, surveyStandard)

    def _select_sourceOfFunds(self, fundsSource):
        self.htmlSelect(self._select_sourceOfFunds_loc, fundsSource)

    def _select_salarySystem(self, salarySystemType):
        """
        选择工资制度
        :param salarySystemType:
        """
        self.htmlSelect(self._select_salarySystem_loc, salarySystemType)

    def _select_unitLevel(self, unitLevel):
        self.htmlSelect(self._select_unitLevel_loc, unitLevel)

    def _select_isManager(self, whetherManager):
        if whetherManager == '是':
            self.click(self._click_isManager_loc, False)
        else:
            self.click(self._click_noManager_loc, False)

    def _input_managerUnit(self, managerUnit):
        self.input(self._input_managerUnit_loc, managerUnit)
        self.click(f"xpath->//nz-option-item[@title='{managerUnit}']")

    def _select_auditProcess(self, auditProcess):
        self.htmlSelect(self._select_auditProcess_loc, auditProcess)

    def _select_hardshipArea(self, hardshipAreaType):
        self.htmlSelect(self._select_hardshipArea_loc, hardshipAreaType)

    def _select_membership(self, membership):
        self.htmlSelect(self._select_membership_loc, membership)

    def _select_unitStation(self, unitStation):
        self.click(self._click_unitStation_loc)
        self.click(f"xpath->//li[@title='{unitStation}']")

    def _select_averageElevation(self, averageElevation):
        self.htmlSelect(self._select_averageElevation_loc, averageElevation)

    def _select_stationElevation(self, stationElevation):
        self.htmlSelect(self._select_stationElevation_loc, stationElevation)

    def _upload_attachment(self):
        self.click(self._attachment_btn_loc)
        ele = self.get_element(self._input_attachment_loc)
        ele.send_keys(file_path)
        self.click(self._save_attachment_btn_loc)

    def _click_save_modify_btn(self):
        self.click(self._save_modify_btn_loc)

    def _get_save_msg(self):
        return self.get_text(self._save_msg_loc)

    def _switch_to_operator(self):
        self.click(self._operator_btn_loc)

    def _click_createOperator_btn(self):
        self.click(self._create_btn_loc)

    def _input_username(self, username):
        self.input(self._input_username_loc, username)
        self.tab(self._input_username_loc)

    def _input_name(self):
        # self.driver.find_element(By.XPATH, "//input[@formcontrolname='userNickName']").send_keys("test")
        self.input(self._input_name_loc, "test")

    def _select_gender(self, gender):
        self.htmlSelect(self._select_gender_loc, gender)

    def _input_identityCard(self, identityCard):
        self.input(self._input_identityCard_loc, identityCard)

    def _input_phoneNumber(self, phoneNumber):
        self.input(self._input_phoneNumber_loc, phoneNumber)

    def _choice_jurisdiction(self):
        self.click(self._set_jurisdiction_loc)

    def _click_save_operator(self):
        self.click(self._save_operator_btn_loc)

    def _get_create_operator_msg(self):
        return self.get_text(self._save_operator_msg_loc)

    def create_uniit(self, nest_messages_creditCode, unit_name, supervisor):
        """
        新建单位
        """
        self._swith_to_home()
        self._switch_to_creat()
        self._input_unit_code(nest_messages_creditCode)
        self._input_unit_name(unit_name)
        self._select_whetherToBeInCharge(supervisor)
        self._click_save()
        return self._get_createUnit_msg()

    def maintenance_unit_information(self):
        """
        维护单位信息
        """
        self._swith_to_maintain()
        self._input_headOfUnit("测试")
        self._input_phone("15111111111")
        self._input_address("xxx省xxx市xxx区xxx路")
        self._input_postcode("631002")
        self._select_financialSupport("部分人员")
        self._select_financialRegulation("部分人员")  # 选择财政统发
        self._input_unitFinancialCode(None)  # 输入财政编码
        self._select_unitProperty("事业单位")  # 选择单位性质
        self._select_salarySystem("事业单位工资制度")  # 选择工资制度
        self._select_unitLevel("正区科级")  # 选择单位级别
        self._select_isManager("否")  # 选择是否为主管
        self._input_managerUnit("测试主管单位")  # 输入主管单位,点击主管单位
        self._select_auditProcess("2级审核（基层-终审）")  # 选择审核流程
        self._select_hardshipArea("无")  # 选择艰边类别
        self._select_membership("县、市、区")  # 选择隶属关系
        self._select_unitStation("四川省")  # 选择单位驻地
        self._select_averageElevation("3499米以下地区")  # 选择平均海拔
        self._select_stationElevation("3499米以下地区")  # 选择驻地海拔
        self._select_typeOfPublicInstitution("公益一类事业单位")  # 选择事业单位类型
        self._select_publicInstitutionIndustry("11.其他行业")  # 选择事业单位行业
        self._select_defaultSurveyStandard("否")  # 选择是否地勘单位
        self._select_sourceOfFunds("核定收支、定额补助")  # 选择经费来源
        # self._upload_attachment()  # 附件上传
        self._click_save_modify_btn()  # 点击保存
        return self._get_save_msg()

    def create_operator(self, username, gender, identityCard, phoneNumber):
        """
        新建经办人
        """
        self._switch_to_operator()
        self._click_createOperator_btn()
        self._input_username(username)
        self._input_name()
        self._select_gender(gender)
        self._input_identityCard(identityCard)
        self._input_phoneNumber(phoneNumber)
        self._choice_jurisdiction()
        self._click_save_operator()
        time.sleep(0.5)
        return self._get_create_operator_msg()


# -*- coding: UTF-8 -*-
"""
**    @Project :        PublicInstitutionSystem
**    @fileName         createUnitPage.py
**    @author           Echo
**    @EditTime         2024/1/17
"""
import random
import time
from typing import *

import allure
from selenium.webdriver.common.by import By

from config import globalparam
from config.globalparam import file_path, datas_path
from public.common.base_page import BasePage
from utils.files_upload import upload_file


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
    _upload_btn_loc = "xpath->(//button[@class='ant-btn ng-star-inserted'])[1]"
    _upload_file_msg_loc = "xpath->//div/span[contains(text(),'附件示例.png')]"
    _save_attachment_btn_loc = 'css->div.ant-modal-footer button.ant-btn-primary'
    _save_modify_btn_loc = 'xpath->//div[@class="ant-tabs-content-holder"]/div/div/lib-unit-basis/button'
    _save_msg_loc = 'css->.ant-message span'

    _operator_btn_loc = "xpath->//div[contains(text(),'单位经办人信息')]"
    _create_btn_loc = "xpath->//span[contains(text(),'新建账号')]"
    _input_username_loc = "xpath->//input[@formcontrolname='userName']"
    _input_name_loc = "xpath->//input[@formcontrolname='userNickName']"
    _select_gender_loc = "xpath->//nz-select[@formcontrolname='gender']"
    _input_identityCard_loc = "xpath->//input[@formcontrolname='identityCard']"
    _input_contact_loc = "xpath->//input[@formcontrolname='contact']"
    _input_phoneNumber_loc = "xpath->//input[@formcontrolname='phoneNumber']"
    _input_email_loc = "xpath->//input[@formcontrolname='email']"
    _set_jurisdiction_loc = "css->nz-card[nztitle='权限选择'] div.ant-card-body div:nth-child(1)"
    _save_operator_btn_loc = "xpath->//span[contains(text(),'保存')]/ancestor::button"
    _save_operator_msg_loc = "css->.ant-modal-footer span.foot_msg"
    _shutDown_btn_loc = "xpath->//div[contains(@class, 'ant-modal-footer')]/button[2]"

    def _swith_to_home(self):
        """ 切换到运维中心首页 """
        with allure.step('切换到运维中心首页'):
            self.driver.open_url(f'{globalparam.env}/home')

    def _switch_to_creat(self):
        """
        点击新建单位按钮
        """
        with allure.step('点击新建单位按钮'):
            self.driver.click(self._makeUnit_btn_loc)

    def _input_unit_code(self, nest_messages_creditCode):
        """
        输入单位社会信用代码
        """
        with allure.step('输入单位社会信用代码'):
            self.driver.input(self._orgcode_loc, nest_messages_creditCode)

    def _input_unit_name(self, unit_name):
        """
        输入单位名称
        """
        with allure.step('输入单位名称'):
            self.driver.input(self._unit_name_loc, unit_name)

    def _select_whetherToBeInCharge(self, supervisor):
        """
        选择是否主管单位
        """
        with allure.step('选择是否主管单位'):
            self.driver.click(self._supervisor_loc)
            self.driver.click(f"xpath->//div[@title='{supervisor}']")

    def _click_save(self):
        """
        点击保存
        """
        with allure.step('点击保存'):
            self.driver.click(self._save_btn_loc)

    def _get_createUnit_msg(self):
        """
        获取保存成功提示
        """
        with allure.step('获取保存成功提示'):
            return self.driver.get_text(self._createUnit_msg)

    def _swith_to_maintain(self):
        """
        点击维护单位信息按钮
        """
        with allure.step('点击维护单位信息按钮'):
            self.driver.click(self._maintain_btn_loc)

    def _input_headOfUnit(self, headOfUnit):
        """
        输入单位负责人
        """
        if headOfUnit is not None:
            with allure.step('输入单位负责人'):
                self.driver.input(self._input_headOfUnit_loc, headOfUnit)

    def _input_phone(self, officeTel):
        """
        输入单位电话
        """
        if officeTel is not None:
            with allure.step('输入单位电话'):
                self.driver.input(self._input_phone_loc, officeTel)

    def _input_address(self, unitAddress):
        """
        输入单位地址
        """
        if unitAddress is not None:
            with allure.step('输入单位地址'):
                self.driver.input(self._input_address_loc, unitAddress)

    def _input_postcode(self, postcode):
        """
        输入邮编
        """
        if postcode is not None:
            with allure.step('输入邮编'):
                self.driver.input(self._input_postcode_loc, postcode)

    def _select_financialSupport(self, financialSupportType):
        """
        选择财政供养
        """
        with allure.step('选择财政供养'):
            self.driver.htmlSelect(self._select_financialSupport_loc, financialSupportType)

    def _select_financialRegulation(self, financialRegulation):
        """
        选择财政统发
        """
        with allure.step('选择财政统发'):
            self.driver.htmlSelect(self._select_financialRegulation_loc, financialRegulation)

    def _input_unitFinancialCode(self, financialCode):
        """
        输入财政编码
        """
        if financialCode is not None:
            with allure.step('输入财政编码'):
                self.driver.input(self._input_unitFinancialCode_loc, financialCode)

    def _select_unitProperty(self, unitProperty):
        """
        选择单位性质
        """
        with allure.step('选择单位性质'):
            self.driver.htmlSelect(self._select_unitProperty_loc, unitProperty)

    def _select_salarySystem(self, salarySystemType):
        """
        选择工资制度
        :param salarySystemType:
        """
        self.driver.htmlSelect(self._select_salarySystem_loc, salarySystemType)

    def _select_unitLevel(self, unitLevel):
        """
        选择单位级别
        """
        with allure.step('选择单位级别'):
            self.driver.htmlSelect(self._select_unitLevel_loc, unitLevel)

    def _select_isManager(self, whetherManager):
        """
        选择是否主管单位
        """
        with allure.step('选择是否主管单位'):
            if whetherManager == '是':
                self.driver.click(self._click_isManager_loc, False)
            else:
                self.driver.click(self._click_noManager_loc, False)

    def _input_managerUnit(self, whetherManager):
        """ 选择主管单位 """
        _get_orgs_loc = ("xpath->//nz-option-container[contains(@class, "
                         "'ant-select-dropdown')]/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item")
        if whetherManager == '否':
            with allure.step('选择主管单位'):
                self.driver.click(self._click_managerUnit_loc)
                managerUnit = random.choice(self.driver.get_elements(_get_orgs_loc)).get_attribute('title')
                self.driver.input(self._input_managerUnit_loc, managerUnit)
                self.driver.click(f"xpath->//nz-option-item[@title='{managerUnit}']")

    def _select_auditProcess(self, auditProcess):
        """
        选择审核流程
        """
        with allure.step('选择审核流程'):
            self.driver.htmlSelect(self._select_auditProcess_loc, auditProcess)

    def _select_hardshipArea(self, hardshipAreaType):
        """
        选择艰边类别
        """
        with allure.step('选择艰边类别'):
            self.driver.htmlSelect(self._select_hardshipArea_loc, hardshipAreaType)

    def _select_subsidyStandardTypeLocale(self, subsidyStandardTypeLocale):
        """ 选择公务员规范后津补贴标准驻地 """
        if self.driver.element_exists(self._select_subsidyStandardTypeLocale_loc):
            with allure.step('选择公务员规范后津补贴标准驻地'):
                self.driver.click(self._select_subsidyStandardTypeLocale_loc)
                self.driver.click(f'//li[@title="{subsidyStandardTypeLocale}"]')

    def _select_membership(self, membership):
        """
        选择隶属关系
        """
        with allure.step('选择隶属关系'):
            self.driver.htmlSelect(self._select_membership_loc, membership)

    def _select_unitStation(self, unitStation):
        """
        选择单位驻地
        """
        with allure.step('选择单位驻地'):
            self.driver.click(self._click_unitStation_loc)
            self.driver.click(f"xpath->//li[@title='{unitStation}']")

    def _select_averageElevation(self, averageElevation):
        """
        选择平均海拔
        """
        with allure.step('选择平均海拔'):
            self.driver.htmlSelect(self._select_averageElevation_loc, averageElevation)

    def _select_stationElevation(self, stationElevation):
        """
        选择驻地海拔
        """
        with allure.step('选择驻地海拔'):
            self.driver.htmlSelect(self._select_stationElevation_loc, stationElevation)

    def _select_typeOfPublicInstitution(self, institutionType):
        """
        选择单位类型
        """
        if self.driver.element_exists(self._select_typeOfPublicInstitution_loc):
            with allure.step('选择单位类型'):
                self.driver.htmlSelect(self._select_typeOfPublicInstitution_loc, institutionType)

    def _select_publicInstitutionIndustry(self, industry):
        """
        选择单位行业
        """
        if self.driver.element_exists(self._select_publicInstitutionIndustry_loc):
            with allure.step('选择单位行业'):
                self.driver.input(self._select_publicInstitutionIndustry_loc, industry)
                self.driver.click(f'xpath->//nz-tree-node-title[@title="{industry}"]')

    def _select_defaultSurveyStandard(self, surveyStandard):
        """
        选择是否地勘
        """
        if self.driver.element_exists(self._select_defaultSurveyStandard_loc):
            with allure.step('选择是否地勘'):
                self.driver.htmlSelect(self._select_defaultSurveyStandard_loc, surveyStandard)

    def _select_sourceOfFunds(self, fundsSource):
        """
        选择经费来源
        """
        if self.driver.element_exists(self._select_sourceOfFunds_loc):
            with allure.step('选择经费来源'):
                self.driver.htmlSelect(self._select_sourceOfFunds_loc, fundsSource)

    def _upload_attachment(self):
        file_download_loc = 'xpath->//span[contains(text(),"下载")]'
        self.driver.click(self._attachment_btn_loc)
        self.driver.click(self._upload_btn_loc)
        upload_file(datas_path, "附件示例.png")
        if self.driver.get_element(file_download_loc):
            assert "附件示例.png" == self.driver.get_text(self._upload_file_msg_loc), "上传附件失败."
            self.driver.assert_text("附件示例.png", self.driver.get_text(self._upload_file_msg_loc))
            self.driver.click(self._save_attachment_btn_loc)

    def _click_save_btn(self):
        """
        点击保存
        """
        with allure.step('点击保存'):
            self.driver.click(self._save_modify_btn_loc)

    def _get_save_msg(self):
        """
        获取保存成功的提示信息
        """
        with allure.step('获取保存成功的提示信息'):
            return self.driver.get_text(self._save_msg_loc)

    def _switch_to_operator(self):
        """
        切换到经办人
        """
        with allure.step('切换到经办人界面'):
            self.driver.click(self._operator_btn_loc)

    def _click_createOperator_btn(self):
        """
        点击新建经办人
        """
        with allure.step('点击新建经办人'):
            self.driver.click(self._create_btn_loc)

    def _input_username(self, username):
        """
        输入账号
        """
        with allure.step('输入账号'):
            time.sleep(0.5)
            self.driver.input(self._input_username_loc, username)
            self.driver.tab(self._input_username_loc)

    def _input_name(self, name):
        """
        输入姓名
        """
        with allure.step('输入姓名'):
            self.driver.input(self._input_name_loc, name)

    def _select_gender(self, gender):
        """
        选择性别
        """
        with allure.step('选择性别'):
            self.driver.htmlSelect(self._select_gender_loc, gender)

    def _input_identityCard(self, identityCard):
        """
        输入身份证号
        """
        with allure.step('输入身份证号'):
            self.driver.input(self._input_identityCard_loc, identityCard)

    def _input_contact(self, phone):
        """
        输入电话
        """
        if phone is not None:
            with allure.step('输入电话'):
                self.driver.input(self._input_contact_loc, phone)

    def _input_phoneNumber(self, phoneNumber):
        """
        输入手机号
        """
        with allure.step('输入手机号'):
            self.driver.input(self._input_phoneNumber_loc, phoneNumber)

    def _input_email(self, email):
        """
        输入邮箱
        """
        if email is not None:
            with allure.step('输入邮箱'):
                self.driver.input(self._input_email_loc, email)

    def _choice_jurisdiction(self):
        """
        选择经办人权限
        """
        with allure.step('选择经办人权限'):
            self.driver.click(self._set_jurisdiction_loc)

    def _click_save_operator(self):
        """
        点击保存
        """
        with allure.step('点击保存经办人信息'):
            self.driver.click(self._save_operator_btn_loc)

    def _get_create_operator_msg(self):
        """
        获取保存成功的提示信息
        """
        with allure.step('获取保存成功的提示信息'):
            return self.driver.get_text(self._save_operator_msg_loc)

    def _click_shutDown_btn(self):
        """
        关闭弹窗
        """
        with allure.step('点击关闭'):
            self.driver.click(self._shutDown_btn_loc)

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

    def maintenance_unit_information(self, headOfUnit, officeTel, unitAddress,
                                     postcode, financialSupport, financialRegulation, unitFinancialCode,
                                     unitProperty, salarySystemType, unitLevel, whetherManager, auditProcess,
                                     hardshipAreaType, membership, subsidyStandardTypeLocale,
                                     unitStation, averageElevation, stationElevation, typeOfPublicInstitution,
                                     publicInstitutionIndustry, defaultSurveyStandard, sourceOfFunds):
        """
        维护单位信息
        """
        self._swith_to_maintain()
        self._input_headOfUnit(headOfUnit)
        self._input_phone(officeTel)
        self._input_address(unitAddress)
        self._input_postcode(postcode)
        self._select_financialSupport(financialSupport)  # 选择财政供养
        self._select_financialRegulation(financialRegulation)  # 选择财政统发
        self._input_unitFinancialCode(unitFinancialCode)  # 输入财政编码
        self._select_unitProperty(unitProperty)  # 选择单位性质
        self._select_salarySystem(salarySystemType)  # 选择工资制度
        self._select_unitLevel(unitLevel)  # 选择单位级别
        self._select_isManager(whetherManager)  # 选择是否为主管
        self._input_managerUnit(whetherManager)  # 输入主管单位,点击主管单位
        self._select_auditProcess(auditProcess)  # 选择审核流程
        self._select_hardshipArea(hardshipAreaType)  # 选择艰边类别
        self._select_subsidyStandardTypeLocale(subsidyStandardTypeLocale)  # 选择公务员规范后津补贴标准驻地
        self._select_membership(membership)  # 选择隶属关系
        self._select_unitStation(unitStation)  # 选择单位驻地
        self._select_averageElevation(averageElevation)  # 选择平均海拔
        self._select_stationElevation(stationElevation)  # 选择驻地海拔
        self._select_typeOfPublicInstitution(typeOfPublicInstitution)  # 选择事业单位类型
        self._select_publicInstitutionIndustry(publicInstitutionIndustry)  # 选择事业单位行业
        self._select_defaultSurveyStandard(defaultSurveyStandard)  # 选择是否地勘单位
        self._select_sourceOfFunds(sourceOfFunds)  # 选择经费来源
        self._upload_attachment()  # 附件上传
        self._click_save_btn()  # 点击保存
        return self._get_save_msg()

    def create_operator(self, username, name, gender, identityCard, contact, phoneNumber, email):
        """
        新建经办人
        """
        time.sleep(1)
        self._switch_to_operator()
        self._click_createOperator_btn()
        self._input_username(username)
        self._input_name(name)
        self._select_gender(gender)
        self._input_identityCard(identityCard)
        self._input_contact(contact)
        self._input_phoneNumber(phoneNumber)
        self._input_email(email)
        self._choice_jurisdiction()
        self._click_save_operator()
        time.sleep(0.5)
        msg = self._get_create_operator_msg()
        self._click_shutDown_btn()
        return msg

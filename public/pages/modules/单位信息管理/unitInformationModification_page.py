# == Coding: UTF-8 ==
# @Project :        PublicInstitutionSystem
# @fileName         unitInformationModification_page.py
# @version          v0.1
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/7/11
# @Software:        PyCharm
# ====/******/=====
import random
import time
from typing import Text

import allure
from selenium.webdriver.common.by import By

from config import globalparam
from public.common.base_page import BasePage


class UnitInformationModificationPage(BasePage):
    """单位基础信息修改"""
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
    _save_modify_btn_loc = 'xpath->//div[@class="ant-tabs-content-holder"]/div/div/lib-unit-basis/button'
    _save_msg_loc = 'css->.ant-message span'

    def _get_orgCode(self) -> Text:
        _orgCode_loc = f'xpath->//tbody/tr[{random.randint(2, 15)}]/td[2]'
        orgcode_loc = self.driver.get_element(locator=_orgCode_loc)
        if orgcode_loc:
            return orgcode_loc.text
        else:
            self._get_orgCode()

    def _swith_to_home(self):
        with allure.step('切换到首页'):
            self.driver.open_url(f'{globalparam.env}/home')

    def _switch_to_unitInformationManagement(self):
        with allure.step('切换到单位信息管理'):
            self.driver.click(self._unitInformationManagement__btn_loc)

    def _org_code(self):
        return self._get_orgCode()

    def _query_unit(self):
        with allure.step('查询单位'):
            self.driver.input(self._query_loc, self._org_code())
            self.driver.click(self._queryBtn_loc)

    def _select_unit(self):
        with allure.step('选择单位'):
            self.driver.click(self._orgCode_loc)

    def _click_orgInfo_btn(self):
        with allure.step('点击单位基础信息'):
            self.driver.click(self._orgInfo_btn_loc)

    def _input_orgCode(self, newGrassrootsUnitsID):
        """ 修改单位统一社会信用代码 """
        with allure.step('修改单位统一社会信用代码'):
            self.driver.input(self._input_orgcode_loc, newGrassrootsUnitsID)

    def _input_orgName(self, unitName):
        """ 修改单位名称 """
        with allure.step('修改单位名称'):
            self.driver.input(self._input_orgName_loc, unitName)

    def _input_headOfUnit(self, headOfUnit):
        """ 修改单位负责人 """
        if headOfUnit is not None:
            with allure.step('修改单位负责人'):
                self.driver.input(self._input_headOfUnit_loc, headOfUnit)

    def _input_phone(self, officeTel):
        """ 修改单位电话 """
        if officeTel is not None:
            with allure.step('修改单位电话'):
                self.driver.input(self._input_phone_loc, officeTel)

    def _input_address(self, unitAddress):
        """ 修改单位地址 """
        if unitAddress is not None:
            with allure.step('修改单位地址'):
                self.driver.input(self._input_address_loc, unitAddress)

    def _input_postcode(self, postcode):
        """ 修改邮编 """
        if postcode is not None:
            with allure.step('修改邮编'):
                self.driver.input(self._input_postcode_loc, postcode)

    def _select_financialSupport(self, financialSupportType):
        """ 修改财政供养 """
        if financialSupportType is not None:
            with allure.step('修改财政供养'):
                self.driver.htmlSelect(self._select_financialSupport_loc, financialSupportType)

    def _select_financialRegulation(self, financialRegulation):
        """ 修改财政统发 """
        if financialRegulation is not None:
            with allure.step('修改财政统发'):
                self.driver.htmlSelect(self._select_financialRegulation_loc, financialRegulation)

    def _input_unitFinancialCode(self, financialCode):
        """ 修改财政编码 """
        if financialCode is not None:
            with allure.step('修改财政编码'):
                self.driver.input(self._input_unitFinancialCode_loc, financialCode)

    def _select_unitProperty(self, unitProperty):
        """ 修改单位性质 """
        if unitProperty is not None:
            with allure.step('修改单位性质'):
                self.driver.htmlSelect(self._select_unitProperty_loc, unitProperty)

    def _select_salarySystem(self, salarySystemType):
        """ 选择工资制度 """
        if salarySystemType is not None:
            with allure.step('修改执行工资制度'):
                self.driver.htmlSelect(self._select_salarySystem_loc, salarySystemType)

    def _select_unitLevel(self, unitLevel):
        """ 修改单位级别 """
        if unitLevel is not None:
            with allure.step('修改单位级别'):
                self.driver.htmlSelect(self._select_unitLevel_loc, unitLevel)

    def _select_isManager(self, whetherManager):
        """ 修改是否为主管单位 """
        if whetherManager is not None:
            with allure.step('修改是否为主管单位'):
                if whetherManager == '是':
                    self.driver.click(self._click_isManager_loc, False)
                else:
                    self.driver.click(self._click_noManager_loc, False)

    def _input_managerUnit(self, whetherManager):
        """ 修改主管单位 """
        _get_orgs_loc = ("xpath->//nz-option-container[contains(@class, "
                         "'ant-select-dropdown')]/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item")
        if whetherManager == '否':
            with allure.step('修改主管单位'):
                self.driver.click(self._click_managerUnit_loc)
                managerUnit = random.choice(self.driver.get_elements(_get_orgs_loc)).get_attribute('title')
                self.driver.input(self._input_managerUnit_loc, managerUnit)
                self.driver.click(f"xpath->//nz-option-item[@title='{managerUnit}']")

    def _select_auditProcess(self, auditProcess):
        """ 修改审核流程 """
        with allure.step('修改审核流程'):
            self.driver.htmlSelect(self._select_auditProcess_loc, auditProcess)

    def _select_hardshipArea(self, hardshipAreaType):
        """ 修改艰边类别 """
        with allure.step('修改艰边类别'):
            self.driver.htmlSelect(self._select_hardshipArea_loc, hardshipAreaType)

    def _select_subsidyStandardTypeLocale(self, subsidyStandardTypeLocale):
        """ 选择公务员规范后津补贴标准驻地 """
        if self.driver.element_exists(self._select_subsidyStandardTypeLocale_loc):
            with allure.step('修改公务员规范后津补贴标准驻地'):
                self.driver.click(self._select_subsidyStandardTypeLocale_loc)
                self.driver.click(f'//li[@title="{subsidyStandardTypeLocale}"]')

    def _select_membership(self, membership):
        """ 修改隶属关系 """
        with allure.step('修改隶属关系'):
            self.driver.htmlSelect(self._select_membership_loc, membership)

    def _select_unitStation(self, unitStation):
        """ 修改单位驻地 """
        with allure.step('修改单位驻地'):
            self.driver.click(self._click_unitStation_loc)
            self.driver.click(f"xpath->//li[@title='{unitStation}']")

    def _select_averageElevation(self, averageElevation):
        """ 修改平均海拔 """
        with allure.step('修改平均海拔'):
            self.driver.htmlSelect(self._select_averageElevation_loc, averageElevation)

    def _select_stationElevation(self, stationElevation):
        """ 修改驻地海拔 """
        with allure.step('修改驻地海拔'):
            self.driver.htmlSelect(self._select_stationElevation_loc, stationElevation)

    def _select_typeOfPublicInstitution(self, institutionType):
        """ 修改单位类型 """
        if self.driver.element_exists(self._select_typeOfPublicInstitution_loc):
            with allure.step('修改单位类型'):
                self.driver.htmlSelect(self._select_typeOfPublicInstitution_loc, institutionType)

    def _select_publicInstitutionIndustry(self, industry):
        """ 修改单位行业 """
        if self.driver.element_exists(self._select_publicInstitutionIndustry_loc):
            with allure.step('修改单位行业'):
                self.driver.input(self._select_publicInstitutionIndustry_loc, industry)
                self.driver.click(f'xpath->//nz-tree-node-title[@title="{industry}"]')

    def _select_defaultSurveyStandard(self, surveyStandard):
        """ 修改是否地勘 """
        if self.driver.element_exists(self._select_defaultSurveyStandard_loc):
            with allure.step('修改是否地勘'):
                self.driver.htmlSelect(self._select_defaultSurveyStandard_loc, surveyStandard)

    def _select_sourceOfFunds(self, fundsSource):
        """ 修改经费来源 """
        if self.driver.element_exists(self._select_sourceOfFunds_loc):
            with allure.step('修改经费来源'):
                self.driver.htmlSelect(self._select_sourceOfFunds_loc, fundsSource)

    def _click_save_modify_btn(self):
        with allure.step('点击保存修改按钮'):
            self.driver.click(self._save_modify_btn_loc)

    def _get_save_msg(self):
        with allure.step('获取保存信息'):
            return self.driver.get_text(self._save_msg_loc)

    def modification_unit_base_information(self, newGrassrootsUnitsID, unitName, headOfUnit, officeTel, unitAddress,
                                           postcode, financialSupport, financialRegulation, unitFinancialCode,
                                           unitProperty, salarySystemType, unitLevel, whetherManager, auditProcess,
                                           hardshipAreaType, membership, subsidyStandardTypeLocale,
                                           unitStation, averageElevation, stationElevation, typeOfPublicInstitution,
                                           publicInstitutionIndustry, defaultSurveyStandard, sourceOfFunds):
        """ 修改单位基础信息 """
        self._swith_to_home()  # 前往控制台
        self._switch_to_unitInformationManagement()  # 前往单位信息管理
        self._query_unit()  # 查询单位
        self._select_unit()  # 选择单位
        self._click_orgInfo_btn()  # 点击单位基础信息按钮
        self._input_orgCode(newGrassrootsUnitsID)  # 输入单位统一社会信用代码
        self._input_orgName(unitName)  # 输入单位名称
        self._input_headOfUnit(headOfUnit)  # 输入单位负责人
        self._input_phone(officeTel)  # 输入单位电话
        self._input_address(unitAddress)  # 输入单位地址
        self._input_postcode(postcode)  # 输入邮编
        self._select_financialSupport(financialSupport)  # 选择财政供养
        self._select_financialRegulation(financialRegulation)  # 选择财政统发
        self._input_unitFinancialCode(unitFinancialCode)  # 输入财政编码
        self._select_unitProperty(unitProperty)  # 选择单位性质
        self._select_salarySystem(salarySystemType)  # 选择工资制度
        self._select_unitLevel(unitLevel)  # 选择单位级别
        self._select_isManager(whetherManager)  # 选择是否为主管
        self._input_managerUnit(whetherManager)  # 输入主管单位，点击主管单位
        self._select_auditProcess(auditProcess)  # 选择审核流程
        self._select_hardshipArea(hardshipAreaType)  # 选择艰边类别
        self._select_subsidyStandardTypeLocale(subsidyStandardTypeLocale)  # 选择公务员规范后津补贴标准驻地
        self._select_membership(membership)  # 选择隶属关系
        self._select_unitStation(unitStation)  # 选择单位驻地
        self._select_averageElevation(averageElevation)  # 输入平均海拔
        self._select_stationElevation(stationElevation)  # 输入站点海拔
        self._select_typeOfPublicInstitution(typeOfPublicInstitution)  # 选择单位类型
        self._select_publicInstitutionIndustry(publicInstitutionIndustry)  # 选择单位行业
        self._select_defaultSurveyStandard(defaultSurveyStandard)  # 选择是否地勘
        self._select_sourceOfFunds(sourceOfFunds)  # 选择经费来源
        self._click_save_modify_btn()  # 点击保存修改按钮
        return self._get_save_msg()

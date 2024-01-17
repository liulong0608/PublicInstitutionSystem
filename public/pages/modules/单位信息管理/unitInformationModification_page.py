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

from selenium.webdriver.common.by import By

from config import globalparam
from public.common.base_page import BasePage


class UnitInformationModificationPage(BasePage):
    """单位基础信息修改"""

    def _get_orgCode(self) -> Text:
        _orgCode_loc = f'xpath->//tbody/tr[{random.randint(2, 15)}]/td[2]'
        orgcode_loc = self.get_element(locator=_orgCode_loc)
        if orgcode_loc:
            return orgcode_loc.text
        else:
            self._get_orgCode()

    def modification_unit_base_information(self, newGrassrootsUnitsID, unitName, headOfUnit,
                                           officeTel,
                                           unitAddress, postcode, financialSupport, financialRegulation,
                                           unitFinancialCode, unitProperty, enforceTheWageSystem, unitLevel,
                                           whetherManager,
                                           competentUnit, auditProcess, difficultCategory, subsidyStandardTypeArea,
                                           membership, unitStation, meanAltitude, stationElevation,
                                           typeOfPublicInstitution,
                                           publicInstitutionIndustry, defaultSurveyStandard, sourceOfFunds
                                           ):

        dwxxgl_loc = 'css->.ant-card:nth-child(3) .home_auto_btn__LBhkK:nth-child(2)'
        query_loc = 'name->queryStr'
        queryBtn_loc = ('xpath->//div[@class="ant-row"]/nz-form-item['
                        '7]/nz-form-control/div/div/nz-button-group/button[1]')
        dw_loc = 'xpath->//tbody[@class="ant-table-tbody"]/tr[2]/td[2]'
        dwxxBtn_loc = 'xpath->//div[@class="btn"]/button[1]'
        tyshxydm_loc = 'xpath->//input[@formcontrolname="organizationCode"]'
        dwmc_loc = 'xpath->//input[@formcontrolname="organizationName"]'
        dwfzr_loc = 'xpath->//input[@formcontrolname="head"]'
        dwdh_loc = 'xpath->//input[@formcontrolname="telephone"]'
        dwdz_loc = 'xpath->//input[@formcontrolname="address"]'
        yb_loc = 'xpath->//input[@formcontrolname="zipCode"]'
        czgy_loc = 'xpath->//nz-select[@formcontrolname="financialSupportType"]'
        cztf_loc = 'xpath->//nz-select[@formcontrolname="financialPaymentType"]'
        dwczbm_loc = 'xpath->//input[@formcontrolname="financialCode"]'
        tfryglBtn_loc = ('xpath->//div[@class="ant-tabs-content-holder"]/div/div/lib-unit-basis/div/div['
                         '2]/lib-fiscal/form/nz-form-item[3]/nz-form-control/div/div/button')  # 统发人员管理按钮
        dwxz_loc = 'xpath->//nz-select[@formcontrolname="organizationTypeId"]'
        zxgzzd_loc = 'xpath->//nz-select[@formcontrolname="salarySystemType"]'
        dwjb_loc = 'xpath->//nz-select[@formcontrolname="gradeId"]'
        is_zg_loc = 'xpath->//nz-radio-group[@formcontrolname="supervisor"]/label[1]/span[1]/input'
        no_zg_loc = 'css->nz-radio-group[formcontrolname="supervisor"] label:nth-child(2) span:nth-child(1) input'
        query_zgdw_loc = ('xpath->//nz-select[@formcontrolname="supervisorOrganizationId"]/nz-select-top-control/nz'
                          '-select-search/input')
        zgdw_loc = 'xpath->//nz-select[@formcontrolname="supervisorOrganizationId"]'
        shlc_loc = 'xpath->//nz-select[@formcontrolname="auditProcess"]'
        jblb_loc = 'xpath->//nz-select[@formcontrolname="hardshipAreaTypeId"]'
        gwygfjtzd_loc = 'xpath->//lib-cascader-wrap[@formcontrolname="subsidyStandardTypeLocaleId"]'
        lsgx_loc = 'xpath->//nz-select[@formcontrolname="subordinationCodeId"]'
        dwzd_loc = 'xpath->//lib-cascader-wrap[@formcontrolname="localeId"]'
        pjhb_loc = 'xpath->//nz-select[@formcontrolname="localeAverageElevationId"]'
        zdhb_loc = 'xpath->//nz-select[@formcontrolname="localeElevationId"]'
        sydwlx_loc = 'xpath->//nz-select[@formcontrolname="institutionTypeId"]'
        sydwhy_loc = 'xpath->//nz-tree-select[@formcontrolname="institutionIndustryId"]/div/nz-select-search/input'
        sfdkdw_loc = 'xpath->//nz-select[@formcontrolname="defaultSurveyStandard"]'
        jfly_loc = 'xpath->//nz-select[@formcontrolname="financialSourceTypeId"]'
        dwjcxx_saveBtn_loc = 'xpath->//div[@class="ant-tabs-content-holder"]/div/div/lib-unit-basis/button'
        sava_msg_loc = 'css->.ant-message span'

        self.open_url('http://192.168.2.209/console/home')  # 打开控制台
        self.click(dwxxgl_loc)  # 点击单位信息管理
        # 因为单位比较多，为了方便先进行单位搜索
        org_code = self._get_orgCode()
        self.input(query_loc, org_code)  # 搜索单位
        self.click(queryBtn_loc)  #
        time.sleep(1)
        self.assert_text(dw_loc, org_code)
        self.click(dw_loc)  # 选择单位
        self.click(dwxxBtn_loc)  # 点击单位信息管理

        field_actions = {
            tyshxydm_loc: ('clear_and_input', newGrassrootsUnitsID),  # 修改统一社会信用代码
            dwmc_loc: ('clear_and_input', unitName),  # 修改单位名称
            dwfzr_loc: ('clear_and_input', headOfUnit),  # 修改单位负责人
            dwdh_loc: ('clear_and_input', officeTel),  # 修改电话
            dwdz_loc: ('clear_and_input', unitAddress),  # 修改地址
            yb_loc: ('clear_and_input', postcode),  # 修改邮编
            dwczbm_loc: ('clear_and_input', unitFinancialCode),  # 修改财政编码
            czgy_loc: ('htmlSelect', financialSupport),  # 选择财政供养
            cztf_loc: ('htmlSelect', financialRegulation),  # 选择财政统发
            dwxz_loc: ('htmlSelect', unitProperty),  # 选择单位性质
            zxgzzd_loc: ('htmlSelect', enforceTheWageSystem),  # 选择执行工资制度
            dwjb_loc: ('htmlSelect', unitLevel),  # 选择单位级别
            shlc_loc: ('htmlSelect', auditProcess),  # 选择审核流程
            jblb_loc: ('htmlSelect', difficultCategory),  # 选择艰边类别
            lsgx_loc: ('htmlSelect', membership),  # 选择隶属关系
            pjhb_loc: ('htmlSelect', meanAltitude),  # 选择平均海拔
            zdhb_loc: ('htmlSelect', stationElevation),  # 选择驻地海拔
        }
        for field, (action, value) in field_actions.items():
            if value is not None:
                getattr(self, action)(field, value)
                time.sleep(0.8)
        # self.click(tfryglBtn_loc)    # 点击统发人员管理按钮
        # self.fuzzy_assert(unitFinancialCode, )  # 断言修改单位财政编码后，人员的财政编码有没有发生变化
        if whetherManager == '否':
            self.click(no_zg_loc, whetherWait=False)  # 选择是否主管单位
            if competentUnit is not None:
                self.input(query_zgdw_loc, competentUnit)
                self.htmlSelect(zgdw_loc, competentUnit)  # 选择主管单位
        elif whetherManager == '是':
            self.click(is_zg_loc, whetherWait=False)
        if enforceTheWageSystem == '机关工资制度' or enforceTheWageSystem == '机关、事业两种制度并存':
            self.click(gwygfjtzd_loc)  # 点击公务员规范后津贴标准类别驻地
            self.click(f'xpath->//li[@title="{subsidyStandardTypeArea}"]')
        else:
            pass
        if unitProperty == '事业单位' and enforceTheWageSystem == '事业单位工资制度':
            self.htmlSelect(sydwlx_loc, typeOfPublicInstitution)  # 事业单位类型
            self.input(sydwhy_loc, publicInstitutionIndustry)  # 事业单位行业
            self.click(f'xpath->//nz-tree-node-title[@title="{publicInstitutionIndustry}"]')
            self.htmlSelect(sfdkdw_loc, defaultSurveyStandard)  # 是否地勘单位
            self.htmlSelect(jfly_loc, sourceOfFunds)  # 经费来源
        elif unitProperty == '参公单位' and enforceTheWageSystem == '机关工资制度' or enforceTheWageSystem == '机关、事业两种制度并存':
            self.htmlSelect(sydwlx_loc, typeOfPublicInstitution)  # 事业单位类型
            self.input(sydwhy_loc, publicInstitutionIndustry)  # 事业单位行业
        elif unitProperty == '机关服务中心' and enforceTheWageSystem == '机关、事业两种制度并存':
            self.htmlSelect(sydwlx_loc, typeOfPublicInstitution)  # 事业单位类型
            self.input(sydwhy_loc, publicInstitutionIndustry)  # 事业单位行业
            self.htmlSelect(jfly_loc, sourceOfFunds)  # 经费来源
        else:
            pass
        self.click(dwzd_loc)  # 点击单位驻地
        self.click(f'xpath->//li[@title="{unitStation}"]')  # 选择单位驻地

        self.click(dwjcxx_saveBtn_loc)  # 点击保存
        self.assert_text(sava_msg_loc, '保存成功，稍后请在单位信息查看')

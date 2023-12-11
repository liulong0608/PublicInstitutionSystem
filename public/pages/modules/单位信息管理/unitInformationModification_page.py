# == Coding: UTF-8 ==
# @Project :        PublicInstitutionSystem
# @fileName         unitInformationModification_page.py
# @version          v0.1
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/7/11
# @Software:        PyCharm
# ====/******/=====
import time

from selenium.webdriver.common.by import By

from config import globalparam
from public.common.base_page import BasePage


class UnitInformationModificationPage(BasePage):

    # 单位基础信息修改
    def modification_unit_base_information(self, grassrootsUnitsID, newGrassrootsUnitsID, unitName, headOfUnit,
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
        queryBtn_loc = 'xpath->//div[@class="ant-row"]/nz-form-item[7]/nz-form-control/div/div/nz-button-group/button[1]'
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
        tfryglBtn_loc = 'xpath->////div[@class="ant-tabs-content-holder"]/div/div/lib-unit-basis/div/div[2]/lib-fiscal/form/nz-form-item[3]/nz-form-control/div/div/button'
        dwxz_loc = 'xpath->//nz-select[@formcontrolname="organizationTypeId"]'
        zxgzzd_loc = 'xpath->//nz-select[@formcontrolname="salarySystemType"]'
        dwjb_loc = 'xpath->//nz-select[@formcontrolname="gradeId"]'
        is_zg_loc = 'xpath->//nz-radio-group[@formcontrolname="supervisor"]/label[1]/span[1]/input'
        no_zg_loc = 'xpath->//nz-radio-group[@formcontrolname="supervisor"]/label[2]/span[1]/input'
        query_zgdw_loc = 'xpath->//nz-select[@formcontrolname="supervisorOrganizationId"]/nz-select-top-control/nz-select-search/input'
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
        self.input(query_loc, grassrootsUnitsID)  # 搜索单位
        self.click(queryBtn_loc)  #
        self.assert_text(dw_loc, newGrassrootsUnitsID)
        self.click(dw_loc)  # 选择单位
        self.click(dwxxBtn_loc)  # 点击单位信息管理

        # fields = {
        #     tyshxydm_loc: newGrassrootsUnitsID,  # 修改统一社会信用代码
        #     dwmc_loc: unitName,  # 修改单位名称
        #     dwfzr_loc: headOfUnit,  # 修改单位负责人
        #     dwdh_loc: officeTel,  # 修改单位电话
        #     dwdz_loc: unitAddress,  # 修改单位地址
        #     yb_loc: postcode,  # 修改邮编
        #     dwczbm_loc: unitFinancialCode,  # 修改单位财政编码
        # }
        # for loc, value in fields.items():
        #     if value is not None:
        #         self.clear_and_input(loc, value)
        #     else:
        #         pass

        self.clear_and_input(tyshxydm_loc, newGrassrootsUnitsID)  # 修改统一社会信用代码
        self.clear_and_input(dwmc_loc, unitName)  # 修改单位名称
        self.clear_and_input(dwfzr_loc, headOfUnit)  # 修改单位负责人
        self.clear_and_input(dwdh_loc, officeTel)  # 修改单位电话
        self.clear_and_input(dwdz_loc, unitAddress)  # 修改单位地址
        self.clear_and_input(yb_loc, postcode)  # 修改邮编
        self.clear_and_input(dwczbm_loc, unitFinancialCode)  # 修改单位财政编码
        self.htmlSelect(czgy_loc, financialSupport)  # 修改财政供养
        self.htmlSelect(cztf_loc, financialRegulation)  # 修改财政统发
        # self.click(tfryglBtn_loc)    # 点击统发人员管理按钮
        # self.fuzzy_assert(unitFinancialCode, )  # 断言修改单位财政编码后，人员的财政编码有没有发生变化
        self.htmlSelect(dwxz_loc, unitProperty)  # 选择单位性质
        self.htmlSelect(zxgzzd_loc, enforceTheWageSystem)  # 选择执行工资制度
        self.htmlSelect(dwjb_loc, unitLevel)  # 选择单位级别
        if whetherManager == '否':
            self.click(no_zg_loc)  # 选择是否主管单位
            self.input(query_zgdw_loc, competentUnit)
            self.htmlSelect(zgdw_loc, competentUnit)  # 选择主管单位
        elif whetherManager == '是':
            self.click(is_zg_loc)
        self.htmlSelect(shlc_loc, auditProcess)  # 选择审核流程
        self.htmlSelect(jblb_loc, difficultCategory)  # 选择艰边类别
        if enforceTheWageSystem == '机关工资制度' or enforceTheWageSystem == '机关、事业两种制度并存':
            self.click(gwygfjtzd_loc)  # 点击公务员规范后津贴标准类别驻地
            self.click(f'xpath->//li[@title="{subsidyStandardTypeArea}"]')
        else:
            pass
        self.htmlSelect(lsgx_loc, membership)  # 选择隶属关系
        self.click(dwzd_loc)
        self.click(f'xpath->//li[@title="{unitStation}"]')  # 选择单位驻地
        self.htmlSelect(pjhb_loc, meanAltitude)  # 平均海拔
        self.htmlSelect(zdhb_loc, stationElevation)  # 驻地海拔

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
        self.click(dwjcxx_saveBtn_loc)  # 点击保存
        self.assert_text('保存成功，稍后请在单位信息查看', sava_msg_loc)

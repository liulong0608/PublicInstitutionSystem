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
from config import globalparam
from public.common.base_page import BasePage
from public.pages import *


class UnitInformationModificationPage(BasePage):
    # 单位基础信息修改
    def modification_unit_base_information(self, grassrootsUnitsID, newGrassrootsUnitsID, unitName, headOfUnit,
                                           officeTel,
                                           unitAddress, postcode, financialSupport, financialRegulation,
                                           unitFinancialCode, unitProperty, enforceTheWageSystem, unitLevel,
                                           whetherManager,
                                           competentUnit, auditProcess, difficultCategory, subsidyStandardTypeArea,
                                           membership, unitStation, meanAltitude, stationElevation, typeOfPublicInstitution,
                                           publicInstitutionIndustry, defaultSurveyStandard, sourceOfFunds
                                           ):

        self.open('http://192.168.2.194/console/home')  # 打开控制台
        self.click(dwxxgl_loc)  # 点击单位信息管理
        time.sleep(3)
        # 因为单位比较多，为了方便先进行单位搜索
        self.send_keys(query_loc, grassrootsUnitsID)  # 搜索单位
        self.click(queryBtn_loc)  # 点击查询按钮
        time.sleep(2)
        self.click(dw_loc)  # 选择单位
        self.click(dwxxBtn_loc)  # 点击单位信息管理

        fields = {
            tyshxydm_loc: newGrassrootsUnitsID,  # 修改统一社会信用代码
            dwmc_loc: unitName,  # 修改单位名称
            dwfzr_loc: headOfUnit,  # 修改单位负责人
            dwdh_loc: officeTel,  # 修改单位电话
            dwdz_loc: unitAddress,  # 修改单位地址
            yb_loc: postcode,  # 修改邮编
            dwczbm_loc: unitFinancialCode,  # 修改单位财政编码
        }
        for loc, value in fields.items():
            if value is not None:
                self.clear_type(loc, value)
            else:
                pass
        self.htmlSelect(czgy_loc, financialSupport)  # 修改财政供养
        self.htmlSelect(cztf_loc, financialRegulation)  # 修改财政统发
        # self.click(tfryglBtn_loc)    # 点击统发人员管理按钮
        # self.fuzzy_assert(unitFinancialCode, )  # 断言修改单位财政编码后，人员的财政编码有没有发生变化
        self.htmlSelect(dwxz_loc, unitProperty)  # 选择单位性质
        self.htmlSelect(zxgzzd_loc, enforceTheWageSystem)  # 选择执行工资制度
        self.htmlSelect(dwjb_loc, unitLevel)  # 选择单位级别
        if whetherManager == '否':
            self.click(no_zg_loc)  # 选择是否主管单位
            self.send_keys(query_zgdw_loc, competentUnit)
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
            self.send_keys(sydwhy_loc, publicInstitutionIndustry)  # 事业单位行业
            self.click(f'xpath->//nz-tree-node-title[@title="{publicInstitutionIndustry}"]')
            self.htmlSelect(sfdkdw_loc, defaultSurveyStandard)  # 是否地勘单位
            self.htmlSelect(jfly_loc,  sourceOfFunds)  # 经费来源
        elif unitProperty == '参公单位' and enforceTheWageSystem == '机关工资制度' or enforceTheWageSystem == '机关、事业两种制度并存':
            self.htmlSelect(sydwlx_loc, typeOfPublicInstitution)  # 事业单位类型
            self.send_keys(sydwhy_loc, publicInstitutionIndustry)  # 事业单位行业
        elif unitProperty == '机关服务中心' and enforceTheWageSystem == '机关、事业两种制度并存':
            self.htmlSelect(sydwlx_loc, typeOfPublicInstitution)  # 事业单位类型
            self.send_keys(sydwhy_loc, publicInstitutionIndustry)  # 事业单位行业
            self.htmlSelect(jfly_loc,  sourceOfFunds)  # 经费来源
        else:
            pass
        self.click(dwjcxx_saveBtn_loc)  # 点击保存
        self.fuzzy_assert('保存成功，稍后请在单位信息查看', sava_msg_loc)

# -*- coding: UTF-8 -*-
"""
**    @Project :        PublicInstitutionSystem
**    @fileName         establishmentModification_page.py
**    @author           Echo
**    @EditTime         2024/3/4
"""
import random
from typing import *

from config import globalparam
from public.common.base_page import BasePage


class EstablishmentModificationPage(BasePage):
    """ 单位编制修改 """
    _unitInformationManagement_btn_loc = 'css->.ant-card:nth-child(3) .home_auto_btn__LBhkK:nth-child(2)'
    _input_establishment_loc = "css->.content .ant-row input"
    _save_establishment_btn_loc = "xpath->//span[text()='保存']"
    _query_loc = 'name->queryStr'
    _queryBtn_loc = 'xpath->//div[@class="ant-row"]/nz-form-item[7]/nz-form-control/div/div/nz-button-group/button[1]'
    _orgCode_loc = 'xpath->//tbody[@class="ant-table-tbody"]/tr[2]/td[2]'
    _orgInfo_btn_loc = 'xpath->//div[@class="btn"]/button[1]'
    _establishment_btn_loc = "xpath->//div[contains(text(),'单位编制信息')]"
    _save_establishment_msg_loc = "css->.ant-message span"

    def _get_orgCode(self) -> Text:
        _orgCode_loc = f'xpath->//tbody/tr[{random.randint(2, 15)}]/td[2]'
        orgcode_loc = self.get_element(locator=_orgCode_loc)
        if orgcode_loc:
            return orgcode_loc.text
        else:
            self._get_orgCode()

    def _swith_to_unitInformationManagement(self):
        """ 切换到单位信息管理界面 """
        self.click(self._unitInformationManagement_btn_loc)
        self.open_url(f'{globalparam.node}/test_admin/unit')

    def _org_code(self):
        return self._get_orgCode()

    def _query_unit(self):
        """ 查询并点击单位 """
        self.input(self._query_loc, self._org_code())
        self.click(self._queryBtn_loc)

    def _click_unitInformationManagement(self):
        """ 点击单位信息管理 """
        self.click(self._orgCode_loc)
        self.click(self._orgInfo_btn_loc)

    def _click_establishment_btn(self):
        """ 点击单位编制信息按钮 """
        self.click(self._establishment_btn_loc)

    def _input_establishment(self, establishment):
        """ 输入编制数 """
        self.input(self._input_establishment_loc, establishment)

    def _save_establishment(self):
        """ 保存单位编制信息 """
        self.click(self._save_establishment_btn_loc)

    def _get_save_establishment_msg(self):
        """ 获取保存成功的提示信息 """
        return self.get_text(self._save_establishment_msg_loc)

    def establishment_modification(self, establishment):
        """ 单位编制信息修改 """
        self._swith_to_unitInformationManagement()
        self._query_unit()
        self._click_unitInformationManagement()
        self._click_establishment_btn()
        self._input_establishment(establishment)
        self._save_establishment()
        return self._get_save_establishment_msg()

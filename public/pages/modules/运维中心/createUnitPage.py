# -*- coding: UTF-8 -*-
"""
**    @Project :        PublicInstitutionSystem
**    @fileName         createUnitPage.py
**    @author           Echo
**    @EditTime         2024/1/17
"""
from typing import *

from public.common.base_page import BasePage


class CreateUnitPage(BasePage):
    """ 新建单位 """
    _makeUnit_btn_loc = 'xpath->//*[@id="root"]/section/section/main/div[1]/div[3]/div/div/div[2]/div[1]'
    _orgcode_loc = 'id->nest-messages_creditCode'
    _unit_name_loc = 'id->nest-messages_organizationName'
    _supervisor_loc = 'xpath->//div[@class="ant-select-selector"]'
    _save_btn_loc = 'xpath->//div[@class="unit_add_head__fNOk6"]/button[1]'  # 保存
    _createUnit_msg = 'xpath->//div[@class="ant-modal-content"]/div/div/div/div'  # 保存成功断言信息

    def _swith_to_home(self):
        self.open_url('http://192.168.2.209/console/home')

    def _switch_to_creat(self):
        self.click(self._makeUnit_btn_loc)

    def _input_unit_code(self, nest_messages_creditCode):
        self.input(self._orgcode_loc, nest_messages_creditCode)

    def _input_unit_name(self, unit_name):
        self.input(self._unit_name_loc, unit_name)

    def _select_whetherToBeInCharge(self, supervisor):
        self.click(self._supervisor_loc)
        self.click(f"xpath->//div[@title='{supervisor}']")

    def _click_save(self):
        self.click(self._save_btn_loc)

    def _get_createUnit_msg(self):
        return self.get_text(self._createUnit_msg)

    def create_uniit(self, nest_messages_creditCode, unit_name, supervisor):
        self._swith_to_home()
        self._switch_to_creat()
        self._input_unit_code(nest_messages_creditCode)
        self._input_unit_name(unit_name)
        self._select_whetherToBeInCharge(supervisor)
        self._click_save()
        return self._get_createUnit_msg()


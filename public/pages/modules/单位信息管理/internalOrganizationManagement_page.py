# -*- coding: UTF-8 -*-
"""
**    @Project :        PublicInstitutionSystem
**    @fileName         internalOrganizationManagement_page.py
**    @author           Echo
**    @EditTime         2024/4/1
"""
import time
from typing import *

import allure

from public.common.base_page import BasePage


class InternalOrganizationManagementPage(BasePage):
    """内设机构管理"""
    _org_manager_btn_loc = 'xpath->//span[text()="单位信息管理"]'
    _internal_org_manager_btn_loc = 'xpath->//a[@href="/test_bases/unit/dept-info"]'
    _input_internal_name_loc = "xpath->//input[@name='name']"
    _input_internal_phone_loc = "xpath->//input[@name='phone']"
    _create_btn_loc = "xpath->//button[@type='submit']"
    _create_success_msg_loc = "css->div.ant-message span"
    _modify_btn_loc = "xpath->//span[contains(text(),'修改')]"
    _edit_internal_name_loc = "xpath->//input[@name='editName']"
    _edit_internal_phone_loc = "xpath->//input[@name='editTel']"
    _save_modify_btn_loc = "xpath->//span[contains(text(),'保存')]"
    _del_btn_loc = "xpath->//span[contains(text(),'删除')]"
    _ensure_del_btn_loc = "xpath->//span[contains(text(),'确定')]"

    def swith_to_basic_unit(self, org_code):
        """
        进入基层单位
        """
        with allure.step("进入基层单位"):
            self.business_guidance_grass_roots(org_code)

    def switch_to_internal_organization_management(self):
        """
        进入内设机构管理
        """
        with allure.step("进入内设机构管理"):
            self.driver.move_to_element(self._org_manager_btn_loc)
            self.driver.click(self._internal_org_manager_btn_loc)

    def _input_internal_name(self, name):
        """输入内设机构名称"""
        with allure.step("输入内设机构名称"):
            self.driver.input(self._input_internal_name_loc, name)

    def _input_internal_phone(self, phone):
        """输入内设机构电话"""
        if phone is not None:
            with allure.step("输入内设机构电话"):
                self.driver.input(self._input_internal_phone_loc, phone)

    def _create_internal_organization(self):
        """点击保存按钮"""
        with allure.step("点击保存按钮"):
            self.driver.click(self._create_btn_loc)

    def _get_create_msg(self):
        """获取创建成功的提示信息"""
        with allure.step("获取创建成功的提示信息"):
            return self.driver.get_text(self._create_success_msg_loc)

    def _click_modify_btn(self):
        """点击修改按钮"""
        with allure.step("点击修改按钮"):
            self.driver.click(self._modify_btn_loc)

    def _edit_internal_name(self, name):
        """修改内设机构名称"""
        with allure.step("修改内设机构名称"):
            self.driver.clear_and_input(self._edit_internal_name_loc, name)

    def _edit_internal_phone(self, phone):
        """修改内设机构电话"""
        if phone is not None:
            with allure.step("修改内设机构电话"):
                self.driver.clear_and_input(self._edit_internal_phone_loc, phone)

    def _save_modify_btn(self):
        """
        点击保存
        """
        with allure.step("点击保存按钮"):
            self.driver.click(self._save_modify_btn_loc)

    def _click_del_btn(self):
        """
        点击删除
        """
        with allure.step("点击删除按钮"):
            self.driver.click(self._del_btn_loc)

    def _ensure_del_internal_organization(self):
        """
        确认删除
        """
        with allure.step("确认删除内设机构"):
            self.driver.click(self._ensure_del_btn_loc)

    def add_internal_organization(self, org_code, name, phone):
        """
        新增内设机构组装业务
        """
        self.swith_to_basic_unit(org_code)
        self.switch_to_internal_organization_management()
        self._input_internal_name(name)
        self._input_internal_phone(phone)
        self._create_internal_organization()
        return self._get_create_msg()

    def modify_internal_organization(self):
        """
        修改内设机构
        """
        self._click_modify_btn()
        self._edit_internal_name("Change the name of an internal organization")
        self._edit_internal_phone("028-98765423")
        self._save_modify_btn()

    def delete_internal_organization(self):
        """
        删除内设机构
        """
        self._click_del_btn()
        self._ensure_del_internal_organization()

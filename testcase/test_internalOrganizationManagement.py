# -*- coding: UTF-8 -*-
"""
**    @Project :        PublicInstitutionSystem
**    @fileName         test_internalOrganizationManagement.py
**    @author           Echo
**    @EditTime         2024/4/1
"""
import random
from typing import *

import allure
import pytest

from public.common.datainfo import get_xls_to_dict
from public.pages.modules.单位信息管理.internalOrganizationManagement_page import InternalOrganizationManagementPage

from public.common.base_util import BaseUtil


@allure.epic("单位信息管理")
@allure.story("内设机构管理")
class TestInternalOrganizationManagement(BaseUtil):
    """内设机构管理"""

    @allure.title("新增内设机构")
    @pytest.mark.parametrize("args", get_xls_to_dict("test_datas.xlsx", "create_internal_organization"))
    def test_add_internalOrganization(self, args):
        """新增内设机构"""
        iom = InternalOrganizationManagementPage(self.driver)
        msg = iom.add_internal_organization(
            org_code=str(args['org_code']),
            name=args['internal_name'],
            phone=args['internal_phone']
        )
        self.driver.assert_text("保存成功", msg)
        iom.modify_internal_organization()
        iom.delete_internal_organization()

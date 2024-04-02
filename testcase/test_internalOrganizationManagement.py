# -*- coding: UTF-8 -*-
"""
**    @Project :        PublicInstitutionSystem
**    @fileName         test_internalOrganizationManagement.py
**    @author           Echo
**    @EditTime         2024/4/1
"""
from typing import *

from ddt import ddt, data

from public.common.datainfo import get_xls_to_dict
from public.pages.modules.单位信息管理.internalOrganizationManagement_page import InternalOrganizationManagementPage

from public.common.base_util import BaseUtil


@ddt
class TestInternalOrganizationManagement(BaseUtil):
    """内设机构管理"""

    @data(*get_xls_to_dict("test_datas.xlsx", "create_internal_organization"))
    def test_add_internalOrganization(self, args):
        """新增内设机构"""
        iom = InternalOrganizationManagementPage(self.driver)
        iom.add_internal_organization(
            org_code=args['org_code'],
            name=args['internal_name'],
            phone=args['internal_phone']
        )
        iom.modify_internal_organization()
        iom.delete_internal_organization()

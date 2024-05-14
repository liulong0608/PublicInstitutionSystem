# -*- coding: UTF-8 -*-
"""
**    @Project :        PublicInstitutionSystem
**    @fileName         test_establishment_modification.py
**    @author           Echo
**    @EditTime         2024/3/5
"""
import random
from typing import *

import allure
import pytest

from public.common.base_util import BaseUtil
from public.pages.modules.单位信息管理.establishmentModification_page import EstablishmentModificationPage


@allure.epic("信息管理")
@allure.feature("单位信息管理")
@allure.story("单位编制信息")
class TestEstablishmentModification(BaseUtil):
    """修改单位编制信息"""

    @allure.title("修改单位编制信息")
    def test_establishment_modification(self):
        """修改单位编制信息"""
        em = EstablishmentModificationPage(self.driver)
        msg = em.establishment_modification(establishment=random.randint(1, 50))
        self.driver.assert_text("保存成功", msg)

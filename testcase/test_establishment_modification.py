# -*- coding: UTF-8 -*-
"""
**    @Project :        PublicInstitutionSystem
**    @fileName         test_establishment_modification.py
**    @author           Echo
**    @EditTime         2024/3/5
"""
import random
from typing import *

from public.common.base_util import BaseUtil
from public.pages.modules.单位信息管理.establishmentModification_page import EstablishmentModificationPage


class TestEstablishmentModification(BaseUtil):
    """修改单位编制信息"""
    def test_establishment_modification(self):
        """修改单位编制信息"""
        em = EstablishmentModificationPage(self.driver)
        msg = em.establishment_modification(establishment=random.randint(1, 50))
        self.driver.assert_text(msg, "保存成功")

# == Coding: UTF-8 ==
# @Project :        BusinessWageSystem
# @fileName         makeUnit_page.py  
# @version          v0.1
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/6/6
# @Software:        PyCharm
# ====/******/=====
from public.common.base_page import BasePage
from public.pages import *


class MakeUnitPage(BasePage):
    def make_unit(self, nest_messages_creditCode, unit_name, supervisor):
        self.open('http://192.168.2.194/console/home')
        self.click(makeUnit_btn_loc)
        self.send_keys(tyxy_code_loc, nest_messages_creditCode)  # 输入统一社会信用代码
        self.send_keys(unit_name_loc, unit_name)    # 输入单位名称
        self.htmlSelect(supervisor_loc, f'xpath->//div[@title="{supervisor}"]')  # 是否主管
        self.click(sava_btn)
        self.fuzzy_assert('保存成功，是否需要维护单位信息？', makeUnit_msg)
        self.click(qwwh_btn)

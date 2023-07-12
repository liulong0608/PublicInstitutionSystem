# == Coding: UTF-8 ==
# @Project :        BusinessWageSystem
# @fileName         datainfo.py  
# @version          v0.1
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/6/9
# @Software:        PyCharm
# ====/******/=====
import codecs
import os
import pprint

import xlrd
from config import globalparam

data_path = globalparam.data_path


def get_xls_to_dict(xlsname, sheetname):
    """
    读取excel表结果为dict，第一行为dict的key，后面的行为value
    :param xlsname: excel文件名
    :param sheetname: sheet表名
    :return: [{'title':'1','user':'root'},{'title':'2','user':'xiaoshitou'}]
    """
    datapath = os.path.join(data_path, xlsname)
    xls1 = xlrd.open_workbook(datapath)  # 创建excel对象
    table = xls1.sheet_by_name(sheetname)  # 创建表对象

    dataresult = [table.row_values(i) for i in range(0, table.nrows)]

    result = []
    keys = dataresult[0]  # 获取键值列表

    for i in range(1, len(dataresult)):
        temp = {}
        for j in range(len(keys)):
            if j < len(dataresult[i]):
                value = dataresult[i][j]
                if value == '':
                    value = None
                temp[keys[j]] = value
            else:
                temp[keys[j]] = None
        result.append(temp)
    return result




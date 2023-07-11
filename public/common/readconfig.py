# == Coding: UTF-8 ==
# @Project :        BusinessWageSystem
# @fileName         readconfig.py  
# @version          v0.1
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/6/9
# @Software:        PyCharm
# ====/******/=====
import configparser
import codecs


class ReadConfig:
    """
    专门读取配置文件的，.ini文件格式
    """

    def __init__(self, filename):
        configpath = filename
        fd = open(configpath)
        data = fd.read()
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            files = codecs.open(configpath, "w")
            files.write(data)
            files.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def getValue(self, env, name):
        return self.cf.get(env, name)

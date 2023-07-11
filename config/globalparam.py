# == Coding: UTF-8 ==
# @Project :        BusinessWageSystem
# @fileName         globalparam.py  
# @version          v0.1
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/4/9
# @Software:        PyCharm
# ====/******/=====
import os
from public.common.readconfig import ReadConfig

# 读取配置文件
config_file_path = os.path.split(os.path.realpath(__file__))[0]
read_config = ReadConfig(os.path.join(config_file_path, 'config.ini'))
# 项目参数设置
prj_path = read_config.getValue('projectConfig', 'project_path')
# 日志路径
log_path = os.path.join(prj_path, 'report', 'log')
# 截图文件路径
img_path = os.path.join(prj_path, 'report', 'image')
# 测试报告路径
report_path = os.path.join(prj_path, 'report', 'testreport')
# 默认浏览器
browser = 'Chrome'
# 附件地址
file_path = os.path.join(prj_path, 'data'+'\\')  # 输出：D:\PublicInstitutionSystem\data
# 测试数据路径
data_path = os.path.join(prj_path, 'data', 'testdata')

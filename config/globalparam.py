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
import time

from public.common.readconfig import ReadConfig

# 环境
node = "http://192.168.2.209"
env = f"{node}/test_console"
# 项目根路径
prj_path = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
# 日志路径
log_path = os.path.join(prj_path, 'report', 'logs', f'{time.strftime("%Y%m%d")}_run.log')
# 截图文件路径
img_path = os.path.join(prj_path, 'report', 'image')
# 测试报告根目录
report_root_path = os.path.join(prj_path, 'report')
# 测试报告json数据
report_temp_path = os.path.join(prj_path, 'report', 'temp')
# 测试报告路径
report_path = os.path.join(prj_path, 'report', 'html')
# 测试用例路径
case_path = os.path.join(prj_path, 'testcase')
# 默认浏览器
browser = 'Chrome'
# 配置文件根目录
config_path = os.path.join(prj_path, 'config')
# 浏览器驱动路径
driver_path = os.path.join(prj_path, 'config', 'chromedriver.exe')
linux_driver_path = os.path.join(prj_path, 'config', 'chromedriver')
# 数据目录
datas_path = os.path.join(prj_path, 'data')
# 附件地址
file_path = os.path.join(datas_path, '附件示例.png')  # 输出：D:\PublicInstitutionSystem\data
# 测试数据路径
data_path = os.path.join(prj_path, 'data', 'testdata')
# 测试截图
screenshot_path = os.path.join(prj_path, 'report', 'image')
# 下载路径
download_path = os.path.join(prj_path, 'data', 'files')

# == Coding: UTF-8 ==
# @Project :        PublicInstitutionSystem
# @fileName         sendmail.py
# @version          v0.1
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/7/15
# @Software:        PyCharm
# ====/******/=====
import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from public.common.log import Log
from config import globalparam

# 配置收发件人
sendaddr_name = 'liulong@3mencn.com'
sendaddr_pswd = 'Flzx3000c'  # 授权码
recvaddress = ['liulong@3mencn.com', '1873190160@qq.com']  # [发件人，收件人]

# 测试报告的路径
reportPath = globalparam.report_path
logger = Log().get_logger()


class SendMail:
    def __init__(self, file_path, recver=None):
        """初始化方法，接收文件路径和接收者邮箱地址列表"""
        self.file_path = file_path
        if recver is None:
            self.sendTo = recvaddress
        else:
            self.sendTo = recver

    def __create_message(self):
        """创建邮件消息"""
        self.msg = MIMEMultipart("mixed")
        self.msg['Subject'] = '文件传输'
        self.msg['From'] = sendaddr_name
        self.msg['To'] = ", ".join(self.sendTo)
        self.msg['Date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        # 添加文本内容
        text = MIMEText("请查看附件中的文件。")
        self.msg.attach(text)

        # 添加附件
        with open(self.file_path, "rb") as file:
            attach = MIMEApplication(file.read(), _subtype="octet-stream")
            attach.add_header('Content-Disposition', 'attachment', filename=os.path.basename(self.file_path))
            self.msg.attach(attach)

    def send(self):
        """发送邮件"""
        self.__create_message()
        try:
            smtp = smtplib.SMTP('smtp.exmail.qq.com', 465)  # SMTP服务器
            smtp.login(sendaddr_name, sendaddr_pswd)  # 登录验证
            smtp.send_message(self.msg)  # 发送邮件消息对象
            logger.success("邮件发送成功")
        except Exception as e:
            logger.error(f"发送邮件失败: {e}")
            raise


if __name__ == '__main__':
    # 指定要发送的文件路径
    file_to_send = 'D:\\PublicInstitutionSystem\\report\\testreport\\TestResult.html'  # 替换为你的文件路径
    sendMail = SendMail(file_path=file_to_send)
    sendMail.send()

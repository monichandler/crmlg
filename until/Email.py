#-*- coding:utf-8 -*-
import smtplib
from email.mime.text import  MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import os
from until.config import REPORT_PATH
from email.utils import formataddr
import time
import unittest

# ======查找测试目录，找到最新生成的测试报告文件======

def new_report(file):
    lists = os.listdir(REPORT_PATH)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(REPORT_PATH + "\\" + fn))  # 按时间排序
    file_new = os.path.join(REPORT_PATH, lists[-1])  # 获取最新的文件保存到file_new
    def inner_send():
        file(file_new)
    return inner_send


@new_report
def send_mail(file_new):
    #-----------1.跟发件相关的参数------
    smtpserver ="smtp.qq.com"                #发件服务器
    # 端口
    port = 465
    # 发件箱用户名
    username = "1139868129@qq.com"
    # 发件箱密码
    password = "vwsmrprfoojsjjjj"
    # 发件人邮箱
    sender = "1139868129@qq.com"
    # 收件人邮箱
    receiver = '1139868129@qq.com'

    # ----------2.编辑邮件的内容------
    #读文件
    f = open(file_new, 'rb')
    print(file_new)
    mail_body = f.read()
    f.close()
    # 邮件正文是MIMEText
    body = MIMEText(mail_body, 'html', 'utf-8')
    # 邮件对象
    msg = MIMEMultipart()
    msg['Subject'] = Header("自动化测试报告", 'utf-8').encode()#主题
    msg['From'] = Header(u'测试 <%s>'%sender)                #发件人
    msg['To'] = Header(u'测试负责人 <%s>'%receiver)            #收件人
    msg['To'] = ';'.join(receiver)
    msg['date'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    msg.attach(body)
    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att)
    # ----------3.发送邮件------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连服务器
        smtp.login(sender, password)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, password)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()
    # #发送邮件
    # smtp = smtplib.SMTP()
    # smtp.connect('smtp.mxhichina.com')  # 邮箱服务器
    # smtp.login(username, password)  # 登录邮箱
    # smtp.sendmail(sender, receiver, msg.as_string())  # 发送者和接收者
    # smtp.quit()
    print("邮件已发出！注意查收。")



# if __name__ == "__main__":
#     # 返回实例
#     # file_new = new_report(REPORT_PATH)
#     send_mail()  # 发送测试报告


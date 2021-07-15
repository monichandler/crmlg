import os
import logging
from logging.handlers import TimedRotatingFileHandler
from until.config import LOG_PATH
import os
import datetime

class logger:
    def login_log(self,name,pwd,text):
        with open(os.path.join(LOG_PATH,'crm_login_log.txt'),'a') as f:
            if 'Alert Text:' in text:
                f.write(f'{datetime.datetime.today()}登录名为：{name}，登录密码：{pwd} ,弹框信息：{text}。\n')
            else:
                f.write(f'{datetime.datetime.today()}登录名为：{name}，登录密码：{pwd} ,错误信息信息：{text}。\n')
    def query_log(self,query,mode,web_result,db_result):
        opt={'0':'当天','7':'一周内','15':'半月','30':'一月内'}
        with open(os.path.join(LOG_PATH, f'crm_query_log.txt'), 'a') as f:
            f.write(f'{datetime.datetime.today()}{query}:查询{opt[mode]}的：\n数据库结果：{db_result}网页查询结果:{web_result}\n\n')

    def common_log(self,file_name,text):
        with open(os.path.join(LOG_PATH, f'{file_name}_log.txt'), 'a') as f:
            f.write(f'{datetime.datetime.today()}:{text} \n')




# class Logger_1(object):
#     def __init__(self, logger_name='framework'):
#         self.logger = logging.getLogger(logger_name)
#         logging.root.setLevel(logging.NOTSET)
#         self.log_file_name = 'crm_log.log'
#         self.backup_count = 5
#         # 日志输出级别
#         self.console_output_level = 'WARNING'
#         self.file_output_level = 'DEBUG'
#         # 日志输出格式
#         self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
#     def get_logger(self):
#         """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
#         if not self.logger.handlers:  # 避免重复日志
#             console_handler = logging.StreamHandler()
#             console_handler.setFormatter(self.formatter)
#             console_handler.setLevel(self.console_output_level)
#             self.logger.addHandler(console_handler)
#
#             # 每天重新创建一个日志文件，最多保留backup_count份
#             file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, self.log_file_name),
#                                                     when='D',
#                                                     interval=1,
#                                                     backupCount=self.backup_count,
#                                                     delay=True,
#                                                     encoding='utf-8'
#                                                     )
#             file_handler.setFormatter(self.formatter)
#             file_handler.setLevel(self.file_output_level)
#             self.logger.addHandler(file_handler)
#         return self.logger

#-*- coding:utf-8 -*-
from until.config import REPORT_PATH
import time
from HTMLTestRunner import HTMLTestRunner
import os
def report(suite):
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    report = os.path.join(REPORT_PATH ,f'{now}report.html')
    with open(report, 'wb') as f:
        # 这里u 是用Unicode编码
        runner = HTMLTestRunner(f, verbosity=2, title=u'测试报告', description=u'crm测试报告')
        runner.run(suite)
        # return runner
import unittest
import time
import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
#src
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
# 3、把项目的根目录通过sys.path.append添加为执行时的环境变量
sys.path.append(root_path)
from until.mysql import connect_mysql
from until.crm_log import logger
from common.crm_frame_page import Frame
from common.crm_login_page import Loggin
from common.crm_workbench_page import WorkbenchCare
from common.fun import compare
from Report import report
db=connect_mysql()
log=logger()
class WorkbenchTestCase(unittest.TestCase):
    ff=Frame()
    wc=WorkbenchCare()

    def setUp(self) -> None:
        time.sleep(3)
        self.login=Loggin()
        time.sleep(1)
        self.wc.username().send_keys('admin')
        self.wc.password().send_keys('123456')
        self.wc.button().click()
        time.sleep(2)
        print('------开始测试工作台--------')


    def tearDown(self) -> None:
        # self.wc.quit()
        print('-------测试结束-----------')
        pass
    def test_WorkbenchCareTestCase1(self):
        '''查询当天客户关怀信息'''
        self.wc.switch_to_frame(self.ff.mainFrame())
        time.sleep(2)
        self.wc.searchselect('0')
        self.wc.searchquery().click()
        self.wc.screenshot('0')
        web_result = self.wc.searchtext()
        db_result=db.Care_reminders_sql('客户关怀','0')
        #日志信息
        text=f'查询当天客户关怀信息：网页结果：{web_result}，\n数据库结果：{db_result}\n'
        log.common_log('WorkbenchCare.txt',text)
        if web_result != 0:
            if db_result:
                result= compare(web_result,db_result)
                self.assertTrue(result, f'数据库与页面不匹配:{result}')
                log.common_log('WorkbenchCare.txt', result)
            else:
                self.assertTrue(0, '网页查询结果不为空，数据库为空')
        else:
            if db_result:
                self.assertTrue(0, '都为空')

    def test_WorkbenchCareTestCase2(self):
        ''' 查询一周内客户关怀信息'''
        self.wc.switch_to_frame(self.ff.mainFrame())

        self.wc.searchselect('7')
        self.wc.searchquery().click()
        web_result=self.wc.searchtext()
        db_result=db.Care_reminders_sql('客户关怀','7')
        #日志信息
        text=f'查询一周客户关怀信息：网页结果：{web_result}，\n数据库结果：{db_result}\n'
        log.common_log('WorkbenchCare.txt',text)
        if web_result != 0:
            if db_result:
                result = compare(web_result, db_result)
                self.assertTrue(result, f'数据库与页面不匹配:{result}')
                log.common_log('WorkbenchCare.txt', result)
            else:
                self.assertTrue(0, '网页查询结果不为空，数据库为空')
        else:
            if db_result:
                self.assertTrue(0, '都为空')

    def test_WorkbenchCareTestCase3(self):
        '''查询半月内客户关怀信息'''
        self.wc.switch_to_frame(self.ff.mainFrame())
        self.wc.searchselect('15')
        self.wc.searchquery().click()
        web_result=self.wc.searchtext()
        db_result=db.Care_reminders_sql('客户关怀','15')
        #日志信息
        text=f'查询半月内客户关怀信息：网页结果：{web_result}，\n数据库结果：{db_result}\n'
        log.common_log('WorkbenchCare.txt',text)
        if web_result != 0:
            if db_result:
                result = compare(web_result, db_result)
                self.assertTrue(result, f'数据库与页面不匹配:{result}')
            else:
                self.assertTrue(0, '网页查询结果不为空，数据库为空')
        else:
            if db_result:
                self.assertTrue(0, '都为空')
    def test_WorkbenchCareTestCase4(self):
        '''查询一月内客户关怀信息'''
        self.wc.switch_to_frame(self.ff.mainFrame())
        self.wc.searchselect('30')
        self.wc.searchquery().click()
        web_result=self.wc.searchtext()
        db_result=db.Care_reminders_sql('客户关怀','30')
        #日志信息
        text=f'查询一月内客户关怀信息：网页结果：{web_result}，\n数据库结果：{db_result}\n'
        log.common_log('WorkbenchCare.txt',text)
        if web_result != 0:
            if db_result:
                result = compare(web_result, db_result)
                self.assertTrue(result, f'数据库与页面不匹配:{result}')
            else:
                self.assertTrue(0, '网页查询结果不为空，数据库为空')
        else:
            if db_result:
                self.assertTrue(0,'都为空')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    test = [WorkbenchTestCase('test_WorkbenchCareTestCase1'), WorkbenchTestCase('test_WorkbenchCareTestCase2'),
            WorkbenchTestCase('test_WorkbenchCareTestCase3'), WorkbenchTestCase('test_WorkbenchCareTestCase4')]
    suite.addTests(test)
    # suite.addTest(WorkbenchTestCase('test_WorkbenchCareTestCase1'))
    # 生成测试报告
    report(suite)

    # unittest.main()

    # 发送邮件
    # send_mail()
#
#     def Contact_reminderTestCase(self):
#         '''联系提醒'''
#         opt = ['0', '7', '15', '30']
#         mode = random.choice(opt)
#         '''联系提醒'''
#         Contact_web_result = Contact_reminder(ll.driver, mode)
#         db_result = db.Care_reminders_sql('联系提醒', mode)
#         logger.query_log('客户关怀', mode, Contact_web_result, db_result)
#         print(Contact_web_result)
#
#
#     def Effective_announcementTestCase(self):
#         '''有效公告'''
#         pass
#
#
#     def Birthday_ReminderTestCase(self):
#         '''生日提醒'''
#         pass
#         opt = ['0', '7', '15', '30']
#         mode = random.choice(opt)
#         Birthday_web_result = Birthday_Reminder(ll.driver, mode)
#         print(Birthday_web_result)
#
# if __name__ == '__main__':
#     # unittest.main()
#     suite = unittest.TestSuite()
#     suite.addTest(MyTestCase('Care_remindersTestCase'))
#     suite.addTest(MyTestCase('Contact_reminderTestCase'))
#     suite.addTest(MyTestCase('Effective_announcementTestCase'))
#     suite.addTest(MyTestCase('Birthday_ReminderTestCase'))
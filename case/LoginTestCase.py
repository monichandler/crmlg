'''
     的登录测试，分下面几种情况：
(1)用户名、密码正确
(2)用户名正确、密码不正确
(3)用户名正确、密码为空
(4)用户名错误、密码正确
(5)用户名为空、密码正确（还有用户名和密码均为空时与此情况是一样的，这里就不单独测试了）
'''
import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
#src
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
# 3、把项目的根目录通过sys.path.append添加为执行时的环境变量
sys.path.append(root_path)
from selenium import webdriver
from time import sleep
import unittest
from common.crm_login_page import Loggin
from common.fun import logissucceed
from config import LOG_PATH
from Report import report
from until.crm_log import logger
from until.Email import send_mail
import time



class LoginCase(unittest.TestCase):
    lg=logger()#写入登录数据记录
    def setUp(self):
        url=r'http:\\127.0.0.1:8080\crm'
        self.user_xpath = '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/input'
        self.pwd_xpath = '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/input'
        self.button = '//*[@id="in1"]'
        self.ll = Loggin(url,self.user_xpath,self.pwd_xpath,self.button)

    def test_login_success(self):
        '''用户名、密码正确'''
        self.ll.posit('admin', '123456') #正确用户名和密码
        sleep(3)
        # message = self.ll.driver.switch_to_alert().text
        num=logissucceed(self.ll.driver)
        if num==1:
            print('登录成功')
            self.lg.login_log('admin', '123456','登录成功')
        else:
            print('登录失败')
            self.lg.login_log('admin', '123456', '登录失败')
        self.ll.driver.get_screenshot_as_file(os.path.join(LOG_PATH,'login_success.png'))  #截图  可自定义截图后的保存位置和图片命名
    def test_login_pwd_error(self):
        '''用户名正确、密码不正确'''
        try:
            self.ll.posit('admin', 'kemi')  #正确用户名，错误密码
            print('#正确用户名，错误密码')
            self.ll.driver.get_screenshot_as_file(os.path.join(LOG_PATH, 'login_pwd_error.png'))
            print('screenshot')
            time.sleep(1)
            error_message=self.ll.driver.switch_to_alert().text
            # self.assertIn('用户名或密码错误', error_message)  #用assertIn(a,b)方法来断言 a in b  '用户名或密码错误'在error_message里
        except Exception as e:
            self.lg.login_log('admin', 'kemi',e)
        else:
            self.lg.login_log('admin', 'kemi', error_message)


    def test_login_pwd_null(self):
        '''用户名正确、密码为空'''
        self.ll.posit('admin', '')  #密码为空
        time.sleep(1)
        try:
            self.ll.driver.get_screenshot_as_file(os.path.join(LOG_PATH, "login_pwd_null.jpg"))
        except Exception as e:
            print('截图',e)
        error_message = self.ll.driver.switch_to_alert().text
        # self.assertEqual(error_message,'请输入密码')  #用assertEqual(a,b)方法来断言  a == b  请输入密码等于error_message

        self.lg.login_log('admin', '', error_message)

    def test_login_user_error(self):
        '''用户名错误、密码正确'''
        self.ll.posit('kemixing', '123456')  #密码正确，用户名错误
        sleep(1)
        self.ll.driver.get_screenshot_as_file(os.path.join(LOG_PATH, "login_user_error.jpg"))
        error_message = self.ll.driver.switch_to_alert().text
        self.lg.login_log('kemixing', '123456', error_message)

    def test_login_user_null(self):
        '''用户名为空、密码正确'''
        self.ll.posit('', '123456')  #用户名为空，密码正确
        self.ll.driver.get_screenshot_as_file(os.path.join(LOG_PATH, "login_user_null.jpg"))
        error_message=self.ll.driver.switch_to_alert().text
        # self.assertEqual(error_message,'请输入登录用户名')  #用assertEqual(a,b)方法来断言  a == b
        self.lg.login_log('', '123456', error_message)

    def tearDown(self):
        sleep(2)
        print('登录自动测试完毕！')
        self.ll.driver.quit()


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTests([LoginCase('test_login_success'),LoginCase('test_login_pwd_error'),LoginCase('test_login_pwd_null'),LoginCase('test_login_user_error'),LoginCase('test_login_user_null')])
    # 生成测试报告
    report(suite)
    # 发送邮件
    send_mail()


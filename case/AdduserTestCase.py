import unittest
from common.crm_addstaff_page import adduser
from common.crm_frame_page import Frame
import time
from common.crm_login_page import Loggin
from until.Report import report
class MyTestCase(unittest.TestCase):
    ff = Frame()
    add=adduser()
    def setUp(self) -> None:
        time.sleep(3)
        self.login = Loggin()
        time.sleep(1)
        self.add.username().send_keys('admin')
        self.add.password().send_keys('123456')
        self.add.button().click()
        time.sleep(2)
        self.add.switch_to_frame(self.ff.lefframe())
        self.add.location().click()

        print('------开始测试添加员工--------')

    def tearDown(self) -> None:
        print('------测试添加员工结束--------')


    def test_something(self):
        self.add.switch_to_frame(self.ff.mainFrame())
        self.add.username().send_keys('admin')
        self.add.userAge().send_keys('22')
        self.add.userSex()[0].click()
        self.add.userDiploma()[0].click()
        self.add.departmentId()[2].click()
        self.add.userTel().send_keys('13623452234')
        self.add.userBankcard().send_keys('33323123434134343434344')
        self.add.userIdnum().send_keys('500345200103094565')
        self.add.userAddman().send_keys('李四')
        self.add.userNum().send_keys('4323')
        self.add.userPw().send_keys('password')
        self.add.userNation().send_keys('汉')
        self.add.isMarried()[1].click()
        self.add.roleId('1')
        self.add.userIntest().send_keys('羽毛球')
        self.add.userMobile().send_keys('13623452234')
        self.add.userAddress().send_keys('高新区')
        self.add.userEmail().send_keys('3762@qq.com')
        #截图
        self.add.screenshot('adduser')

        self.add.confirm().click()

        self.assertEqual(True, True)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    test = MyTestCase('test_something')
    suite.addTest(test)
    # suite.addTest(WorkbenchTestCase('test_WorkbenchCareTestCase1'))
    # 生成测试报告
    report(suite)
    # send_mail()

#-*- coding:utf-8 -*-
from Base import base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from common.crm_login_page import Loggin
class adduser(Loggin):
    def location(self):
        '''左侧添加员工'''
        return self.find(By.LINK_TEXT,'添加员工')

    def userName(self):
        return self.find(By.NAME,'userName')

    def userAge(self):
        return self.find(By.NAME,'userAge')


    def userSex(self):
        '''男、女'''
        selector=self.find(By.NAME,'userSex')
        return selector.find_elements(By.TAG_NAME,'option')

    def userDiploma(self):
        '''初中、高中、本科、博士、硕士'''
        selector=self.find(By.NAME,'userDiploma')
        return selector.find_elements(By.TAG_NAME,'option')

    def departmentId(self):
        '''初中、高中、本科、博士、硕士'''
        selector=self.find(By.NAME,'departmentId')
        return selector.find_elements(By.TAG_NAME,'option')

    def userTel(self):
        '''座机'''
        return self.find(By.NAME,'userTel')

    def userBankcard(self):
        '''工资卡号'''
        return self.find(By.NAME,'userBankcard')

    def userIdnum(self):
        '''身份证号'''
        return self.find(By.NAME,'userIdnum')

    def userAddman(self):
        '''添加人'''
        return self.find(By.NAME,'userAddman')

    def userNum(self):
        '''账号'''
        return self.find(By.NAME,'userNum')

    def userPw(self):
        '''密码'''
        return self.find(By.NAME,'userPw')

    def userNation(self):
        '''民族'''
        return self.find(By.NAME,'userNation')

    def isMarried(self):
        '''婚姻:已婚、未婚、离异'''
        selector = self.find(By.NAME, 'isMarried')
        return selector.find_elements(By.TAG_NAME, 'option')

    def roleId(self,value):
        '''1:管理员、2:员工、3:老板'''
        selector = self.find(By.NAME, 'roleId')
        return Select(selector).select_by_value(value)

    def userIntest(self):
        '''兴趣'''
        return self.find(By.NAME,'userIntest')

    def userMobile(self):
        '''手机'''
        return self.find(By.NAME,'userMobile')

    def userAddress(self):
        '''地址'''
        return self.find(By.NAME,'userAddress')

    def userEmail(self):
        '''E_mail'''
        return self.find(By.NAME,'userEmail')

    def confirm(self):
        return self.find(By.NAME,'/html/body/form/table[2]/tbody/tr/td[2]/input')

    def reset(self):
        return self.find(By.NAME,'reset')

    def backbutton(self):
        return self.find(By.XPATH, '/html/body/form/table[2]/tbody/tr/td[4]/input')
    #
    # def switch(self):
    #     return self.switch
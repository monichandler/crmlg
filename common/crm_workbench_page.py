from Base import base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from common.crm_login_page import Loggin

class WorkbenchCare(Loggin):
    '''客户关怀'''
    def searchselect(self, mode):
        selector = self.find(By.XPATH,'//*[@id="div1"]/table/tbody/tr[1]/td[1]/div/select')
        # selector.select_by_value(mode)
        return selector.find_element_by_xpath(f"//option[@value={mode}]")
    def searchquery(self):
        return self.find(By.XPATH,'//*[@id="div1"]/table/tbody/tr[1]/td[2]/div/input')

    def searchtext(self):
        data = []
        text = self.find(By.XPATH,'//*[@id="div1"]/table/tbody/tr[3]/td/div').text
        if text == '没有要关怀的对象！':
            return 0
        else:
            table_tr_list = self.find(By.XPATH, '//*[@id="div1"]/table/tbody').find_elements(By.TAG_NAME,
                                                                                                       "tr")
            for i in range(len(table_tr_list) - 2):
                count = 0
                l1 = self.find(By.XPATH,f'//*[@id="div1"]/table/tbody/tr[{3 + i}]/td[1]/div').text
                l2 = self.find(By.XPATH,f'//*[@id="div1"]/table/tbody/tr[{3 + i}]/td[2]/div').text
                l3 = self.find(By.XPATH,f'//*[@id="div1"]/table/tbody/tr[{3 + i}]/td[3]/div').text
                data.append({'关怀主题': l1, '关怀时间': l2[:19:], '关怀对象': l3})
        # driver.switch_to.default_frame()
        return data

class WorkbenchContact(base):
    '''联系提醒'''
    def searchselect(self, mode):
        selector = self.find(By.NAME, 'addTime1')
        Select(selector).select_by_value(mode)

    def searchquery(self):
        return self.find(By.XPATH,'/html/body/form/table/tbody/tr[2]/td[2]/div/table/tbody/tr[1]/td[2]/div/input')

    def searchtext(self):
        data = []
        text = self.find(By.XPATH, '//*[@id="div2"]/table/tbody/tr[3]/td/div/span').text
        if text == '没有要联系的对象！':
            return 0
        else:
            table_tr_list = self.find(By.XPATH, '//*[@id="div2"]/table/tbody').find_elements(By.TAG_NAME,
                                                                                                       "tr")
            for i in range(len(table_tr_list) - 2):
                l1 = self.find(By.XPATH,f'//*[@id="div2"]/table/tbody/tr[{3 + i}]/td[1]/div').text
                l2 = self.find(By.XPATH,f'//*[@id="div2"]/table/tbody/tr[{3 + i}]/td[2]/div').text
                l3 = self.find(By.XPATH,f'//*[@id="div2"]/table/tbody/tr[{3 + i}]/td[3]/div').text
                l4 = self.find(By.XPATH,f'//*[@id="div2"]/table/tbody/tr[{3 + i}]/td[4]/div').text
                data.append({'联系主题': l1, '联系方式': l2, '应联系时间': l3[:19:], '联系对象': l4})
        return data

class WorkbenchAnnouncement(base):
    '''有效公告'''
    def gettext(self):
        data = []
        table_tr_list = self.find(By.XPATH,
                                            '/html/body/form/table/tbody/tr[4]/td[1]/div/table/tbody').find_elements(
            By.TAG_NAME, "tr")
        for i in range(len(table_tr_list) - 2):
            '/html/body/form/table/tbody/tr[4]/td[1]/div/table/tbody/tr[1]/td[1]/div'
            '/html/body/form/table/tbody/tr[4]/td[1]/div/table/tbody/tr[2]/td[1]/div'
            l1 = self.find(By.XPATH,
                f'/html/body/form/table/tbody/tr[4]/td[1]/div/table/tbody/tr[{1 + i}]/td[1]/div').text
            l2 = self.find(By.XPATH,
                f'/html/body/form/table/tbody/tr[4]/td[1]/div/table/tbody/tr[{1 + i}]/td[2]/div').text
            l3 = self.find(By.XPATH,
                f'/html/body/form/table/tbody/tr[4]/td[1]/div/table/tbody/tr[{1 + i}]/td[3]/div').text
            l4 = self.find(By.XPATH,
                f'/html/body/form/table/tbody/tr[4]/td[1]/div/table/tbody/tr[{1 + i}]/td[4]/div').text
            data.append({'公告主题': l1, '公告内容': l2, '截止时间': l3[:19:], '公告人': l4})
        return data

class WorkbenchBirthday(base):
    '''生日提醒'''
    def searchselect(self, mode):
        selector = self.find(By.NAME, 'addTime2')
        Select(selector).select_by_value(mode)

    def searchquery(self):
        return self.find(By.XPATH,'//*[@id="div2"]/table/tbody/tr[1]/td[2]/div/input')

    def searchtext(self):
        data = []
        text = self.find(By.XPATH, '/html/body/form/table/tbody/tr[4]/td[2]/div/table/tbody/tr[3]/td/div').text
        if text == '没有要联系的对象！':
            return 0
        else:
            table_tr_list = self.find(By.XPATH, '//*[@id="div2"]/table/tbody').find_elements(By.TAG_NAME,
                                                                                                       "tr")
            for i in range(len(table_tr_list) - 2):
                l1 = self.find(By.XPATH,f'/html/body/form/table/tbody/tr[4]/td[2]/div/table/tbody/tr[{3 + i}]/td[1]/div').text
                l2 = self.find(By.XPATH,f'/html/body/form/table/tbody/tr[4]/td[2]/div/table/tbody/tr[{3 + i}]/td[2]/div').text
                l3 = self.find(By.XPATH,f'/html/body/form/table/tbody/tr[4]/td[2]/div/table/tbody/tr[{3 + i}]/td[3]/div').text
                l4 = self.find(By.XPATH,f'/html/body/form/table/tbody/tr[4]/td[2]/div/table/tbody/tr[{3 + i}]/td[4]/div').text
                data.append({'联系主题': l1, '联系方式': l2, '应联系时间': l3[:19:], '联系对象': l4})
        return data
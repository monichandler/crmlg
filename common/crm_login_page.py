from Base import base
from selenium.webdriver.common.by import By
# user_xpath = '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/input'
# pwd_xpath = '/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/input'
# button = '//*[@id="in1"]'
class Loggin(base):

    def username(self):
        return self.find(By.XPATH,'/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/input')

    def password(self):
        return self.find(By.XPATH,'/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/input')

    def button(self):
        return self.find(By.ID,'in1')
    # def __init__(self, url, user_xpath, pwd_xpath,button):
    #     # self.username = username
    #     # self.pwd = pwd
    #     self.user_xpath=user_xpath
    #     self.pwd_xpath=pwd_xpath
    #     self.button=button
    #
    #     self.driver = webdriver.Chrome()
    #     self.driver.get(url)
    #     self.driver.maximize_window()  # 窗口测最大化，展示出页面的全部元素
    #     time.sleep(2)  # 等界面全部生成完
    #
    # def posit(self,username,pwd):
    #     '''
    #     传入输入框的地址
    #     '''
    #     try:
    #         self.driver.find_element_by_xpath(self.user_xpath).send_keys(username)
    #         self.driver.find_element_by_xpath(self.pwd_xpath).send_keys(pwd)
    #         self.driver.find_element_by_xpath(self.button).click()
    #     except:
    #         print('定位失败')

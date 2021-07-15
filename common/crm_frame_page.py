#-*- coding:utf-8 -*-
from Base import base
from selenium.webdriver.common.by import By
class Frame(base):
    def topFrame(self):
        return self.find(By.NAME,'topFrame')
    def bottomFrame(self):
        return self.find(By.NAME,'bottomFrame')
    def lefframe(self):
        return self.find(By.NAME,'/html/frameset/frameset/frame[1]')
    def mainFrame(self):
        return self.find(By.NAME,'mainFrame')

import os
# from selenuim_py.作业.crm_test_framework.config import *
import config
import xlrd
import xlwt

# BASE_PATH = os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0]
# CONFIG_FILE = os.path.join(BASE_PATH, 'config')
# DATA_PATH = os.path.join(BASE_PATH, 'data')
# DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
# LOG_PATH = os.path.join(BASE_PATH, 'log')
# REPORT_PATH = os.path.join(BASE_PATH, 'report')


# xls=xlrd.open_workbook(r'F:\notes\pycharm\tmp\test_csv.xlsx')
# sheet=xls.sheet_by_index(0)
# print(sheet.nrows)
# print(sheet.ncols)
# print(sheet.row_values(0)[0])
# for i in range(sheet.nrows):
#     for j in range(sheet.ncols):
#         print(sheet.row_values(i)[j],end=' ')
#     print('')

class Reader:
    def __init__(self, file):
        if os.path.exists(file):
            self.file = file
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    def data(self):
        pass
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        # if not self._data:
        #     with open(self.yamlf, 'rb') as f:
        #         self._data = list(yaml.safe_load_all(f))  # load后是个generator，用list组织成列表
        # return self._data

    def Sql_data(self):
        if not self._data:
            lst=[]
            with open(self.file, 'r',encoding='utf-8') as f:
                lines=f.readlines()
                for i in lines:
                    if i.split(',')[0]=='mysql':
                        lst=i.split(',')
                    lst[len(lst)-1]=lst[len(lst)-1].split('\n')[0]
                    return lst
    def care_sql(self,query_mode):

        if not self._data:
            with open(self.file, 'r',encoding='utf-8') as f:
                lines = f.readlines()
                for i in lines:
                    if query_mode in i:
                        lst=i[5:]
        return lst
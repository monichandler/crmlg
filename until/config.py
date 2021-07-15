"""
读取配置，需在file_reader中添加相应的Reader进行处理。
"""
import os

# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
# 之前直接拼接的路径，修改了一下，用现在下面这种方法，可以支持linux和windows等不同的平台，也建议大家多用os.path.split()和os.path.join()，不要直接+'\\xxx\\ss'这样
BASE_PATH = os.path.split(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')


# class Path:
#     def __init__(self):
#         self.BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
#         self.CONFIG_FILE = os.path.join(self.BASE_PATH, 'config')
#         self.DATA_PATH = os.path.join(self.BASE_PATH, 'data')
#         self.DRIVER_PATH = os.path.join(self.BASE_PATH, 'drivers')
#         self.LOG_PATH = os.path.join(self.BASE_PATH, 'log')
#         self.REPORT_PATH = os.path.join(self.BASE_PATH, 'report')



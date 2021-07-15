import os
import sys
import  pymysql
current_directory = os.path.dirname(os.path.abspath(__file__))
# root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(current_directory)
from until import file_reader
from until import config


class connect_mysql:
    file = os.path.join(config.CONFIG_FILE, 'config.txt')
    def __init__(self):
        self.reader = file_reader.Reader(self.file)
        self.lst = self.reader.Sql_data()
        try:
            self.db = pymysql.connect(
                host=self.lst[1],
                user=self.lst[2],
                password=self.lst[3],
                db=self.lst[4],
                charset='utf8')
        except pymysql.err.OperationalError:
            print('数据库连接失败')
        self.cursor = self.db.cursor()
    def Care_reminders_sql(self,query_mode,day):
        statement=''.join(self.reader.care_sql(query_mode))
        self.cursor.execute(statement.format(day))
        data=self.cursor.fetchall()
        return data
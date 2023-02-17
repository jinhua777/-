import pymysql
import pandas as pd
from sqlalchemy import create_engine
from urllib import parse

class ToDataBase:
    def __init__(self):
        self.db_data = {
            'db_name': '****',
            'user': '****',
            'passwd': parse.quote_plus('****'),
            'host': '****',
            'port': '****',
            'database': '****'
        }

    ## 数据更新
    def to_dw_mysql_update(self, data):
        dw_mysql_con = create_engine(
            "mysql+pymysql://{}:{}@{}:{}/{}".format(self.db_data['user'], self.db_data['passwd'], self.db_data['host'], self.db_data['port'], self.db_data['database']))
        for item in data:
            sql = '''
                replace into t_crawl_hentaitv_info(
                    title,
                    href,
                    img,
                    release_date,
                    upload_date
                )
                values('%s','%s','%s','%s','%s')
            ''' % (item['title'], item['href'], item['img'], item['release_date'], item['upload_date'])

            dw_mysql_con.execute(sql)


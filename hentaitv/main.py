from hentai import HantaiTV
import time
import datetime
from to_db import ToDataBase
import pandas as pd

def main():
    res = []
    hantaitv = HantaiTV()
    db = ToDataBase()
    ## 首次爬取50条数据
    ## 后续每次爬取前3页
    for page in range(1,2):
        print("start page: %d %s" % (page,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        data = hantaitv.search(str(page))

        for list in data:
            url = list['href']
            date = hantaitv.dateinfo(url)
            list.update(date)
            res.append(list)
            ## time.sleep(1)

        ## time.sleep(2)
        print("end page: %d %s" % (page, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    ## db.to_dw_mysql_first(res)
    res.reverse()
    ## 写入数据库 
    db.to_dw_mysql_update(res)

if __name__ == '__main__':
    main()
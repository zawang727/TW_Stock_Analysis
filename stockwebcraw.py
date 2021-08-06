import requests
from io import StringIO
import pandas as pd
import numpy as np
import codecs
from datetime import datetime
import shutil

today = datetime.today()

def craw_day(days=1,year=int(today.strftime("%Y")),month=int(today.strftime("%m")),date=int(today.strftime("%d"))):
    dayinmonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    crawl_days = days
    
    for day in range(0, crawl_days):
        datestr = str(year * 10000 + month * 100 + date)
        #datestr = '20210723'
        csvstr = ""
        # 下載股價
        r = requests.get('https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')
        if (len(r.text) == 0):
            print("datestr" + datestr +" not exist/n")
        else:
            csvstr=r.text.replace("=","")
            csvstr=csvstr.replace('-","',"-")
            csvstr=csvstr.replace('+","',"")
            csvstr=csvstr.replace('","',"@")
            csvstr=csvstr.replace(',',"")
            csvstr=csvstr.replace('@',',')
            csvstr=csvstr.replace('"',"")
            csvstr=csvstr.split("本益比")[1]
            a=csvstr.split("00669R")
            #print(a[1])
            b=a[1].split("台泥乙特")[1]
            #print(b)
            csvstr=a[0]+"1101,台泥乙特"+b
            #print(csvstr)
    
            filestr='stock'+datestr+'.csv'
            pfile = codecs.open(filestr,'w','utf-16')
            pfile.write(csvstr)
            pfile.close()  
            shutil.move('./'+ filestr , './stockdata/'+ filestr)
        #day decrease
        if(date > 1):
            date = date - 1
        else:
            if (month > 1):
                month = month -1
                date = dayinmonth[(month - 1)]
            else:
                year = year - 1
                month = 12
                date = dayinmonth[(month - 1)]
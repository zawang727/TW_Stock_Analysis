
from IPython.display import display, clear_output
from urllib.request import urlopen
import pandas as pd
import datetime
import requests
import sched
import time
import json
import os

s = sched.scheduler(time.time, time.sleep)

def tableColor(val):
    if val > 0:
        color = 'red'
    elif val < 0:
        color = 'green'
    else:
        color = 'white'
    return 'color: %s' % color
    
def real_time_stock_crawler(targets,per_minutes):
    clear_output(wait=True)
    # 組成stock_list
    stock_list = '|'.join('tse_{}.tw'.format(target) for target in targets) 
    #　query data
    query_url = "http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch="+ stock_list
    data = json.loads(urlopen(query_url).read())
    # 過濾出有用到的欄位
    columns = ['c','n','z','tv','v','o','h','l','y']
    df = pd.DataFrame(data['msgArray'], columns=columns)
    df.columns = ['股票代號','公司簡稱','當盤成交價','當盤成交量','累積成交量','開盤價','最高價','最低價','昨收價']
    df.insert(9, "漲跌百分比", 0.0) 
    # 新增漲跌百分比
    for x in range(len(df.index)):
        if df['當盤成交價'].iloc[x] != '-':
            df.iloc[x, [2,3,4,5,6,7,8]] = df.iloc[x, [2,3,4,5,6,7,8]].astype(float)
            df['漲跌百分比'].iloc[x] = (df['當盤成交價'].iloc[x] - df['昨收價'].iloc[x])/df['昨收價'].iloc[x] * 100
    # 紀錄更新時間
    time = datetime.datetime.now()  
    print("爬蟲時間:" + str(time.hour)+":"+str(time.minute))
    return create_stocks_real_time_status_from_datafram(df,stock_list)
    # show table
    #df = df.style.applymap(tableColor, subset=['漲跌百分比'])
    #display(df)
        

#In other file

class a_stock_real_time_status():
    def __init__(self):
         self.code = ''
         self.name = ''
         self.price = 0.
         self.current_trade_count = 0
         self.day_trade_count = 0
         self.max_price = 0
         self.min_price = 0

def real_time_analysis(stocks_real_time, stocks_data):
    print('股泰驛站臥射預備爆大量通知')
    
def create_stocks_real_time_status_from_datafram(stocks_dataframe,stock_list):
    stocks_real_time=dict()
    for i in range (0,len(stock_list)):
        #need check if information valid !!!!!!!!!
        astock=a_stock_real_time_status()
        astock.code = stocks_dataframe.at(stock_list[i],'股票代號')
        astock.name = stocks_dataframe.at(stock_list[i],'股票代號')
        astock.price = stocks_dataframe.at(stock_list[i],'股票代號')
        astock.current_trade_count = stocks_dataframe.at(stock_list[i],'股票代號')
        astock.day_trade_count = stocks_dataframe.at(stock_list[i],'股票代號')
        astock.max_price = stocks_dataframe.at(stock_list[i],'股票代號')
        astock.min_price = stocks_dataframe.at(stock_list[i],'股票代號')
        stocks_real_time[stock_list[i]] = astock
        #股票代號','公司簡稱','當盤成交價','當盤成交量','累積成交量','開盤價','最高價','最低價','昨收價']
    return stocks_real_time

# 欲爬取的股票代碼
stock_list = ['1101','1102','1103','2330']
per_minutes = 20
real_time_stock_crawler(stock_list,per_minutes)
time = datetime.datetime.now()  
print("更新時間:" + str(time.hour)+":"+str(time.minute))
start_time = datetime.datetime.strptime(str(time.date())+'9:05', '%Y-%m-%d%H:%M')
end_time =  datetime.datetime.strptime(str(time.date())+'13:26', '%Y-%m-%d%H:%M')
# 判斷爬蟲終止條件
while(True):
    if time >= start_time and time <= end_time:
        real_time_stock_crawler(stock_list,per_minutes)
        time.sleep(per_minutes*60)
    else:
        break
    



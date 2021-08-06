# Created with Pyto
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dataclasses import dataclass
import codecs
import os
from datetime import datetime

today = datetime.today()

class a_day_stock():
    def __init__(self):
        self.date=0
        self.tradeshare=0
        self.tradecnt=0
        self.tradequant=0.
        self.iniprice=0.
        self.maxprice=0.
        self.minprice=0.
        self.endprice=0.
 
class a_day_stock_with_title():
    def __init__(self):
        self.code=""
        self.name=""
        self.day_stock_detail=a_day_stock()
        
class a_day_stock_analysis():
    def __init__(self):
        self.five_days_MA=0.;
        self.ten_days_MA=0.;
        self.twnty_days_MA=0.;
        self.sixty_days_MA=0.;
        self.twoh_fifty_days_MA=0.;
        self.twnty_days_max=0.;
        self.twnty_days_min=0.;
        self.sixty_days_max=0.;
        self.sixty_days_min=0.;
        self.twoh_fifty_days_max=0.;
        self.twoh_fifty_days_min=0.;
 
class a_stock_info():
    def __init__(self):
        self.code=""
        self.name=""
        self.history=list() #class a_day_stock()
        self.analysis=list() #class a_day_stock_analysis()
 	
def stock_csv_reader(filestr,datestr):
    day_stock_list=list()
    fp=codecs.open(filestr,'r','utf-16') 
    strread=fp.readline()
    str_list=list()
    while(True):
        strread= fp.readline()
        if(not strread): break
        else:
            str_list = strread.split(",")
            #print(str_list)
            day_stock = a_day_stock_with_title()
            day_stock.day_stock_detail.date=int(datestr)
            day_stock.code=str_list[0]	
            day_stock.name=str_list[1]		
            if str_list[2].isdigit(): day_stock.day_stock_detail.tradeshare=int(str_list[2])
            if str_list[3].isdigit(): day_stock.day_stock_detail.tradecnt=int(str_list[3])
            if(day_stock.day_stock_detail.tradecnt == 0): continue
        #check if string conertion is valid
            if str_list[4].isdigit(): day_stock.day_stock_detail.tradequant=int(str_list[4])
            if str_list[5].replace('.','',1).isdigit() and str_list[5].count('.') < 2: day_stock.day_stock_detail.iniprice=float(str_list[5])
            if str_list[6].replace('.','',1).isdigit() and str_list[6].count('.') < 2: day_stock.day_stock_detail.maxprice=float(str_list[6])
            if str_list[7].replace('.','',1).isdigit() and str_list[7].count('.') < 2:day_stock.day_stock_detail.minprice=float(str_list[7])
            if str_list[8].replace('.','',1).isdigit() and str_list[8].count('.') < 2:day_stock.day_stock_detail.endprice=float(str_list[8])
            day_stock_list.append(day_stock)
            #if(day_stock.code=="1101"): 
                #print(datestr+' '+str_list[7])
    return day_stock_list

def fetch_all_stock_data(): #read new to old
    stockdata=list()
    year = int(today.strftime("%Y"))
    month = int(today.strftime("%m"))
    date = int(today.strftime("%d"))
    dayinmonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for day in range(0, 300):
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
        
        datestr = str(year * 10000 + month * 100 + date)
        filestr = '.\\stockdata\\stock'+datestr+'.csv'
        if (not os.path.exists(filestr)): continue
        stockdata.append(stock_csv_reader(filestr,datestr))
    return stockdata

def transfer_day_struct_2_stock_stock(read_stock_info): #input:  list: a_day_stock_with_title
    stocks_data=dict()
    for i in range (0,len(read_stock_info[0])): #initialize every stock in data
        single_stock_data = a_stock_info()
        single_stock_data.name=read_stock_info[0][i].name
        single_stock_data.code=read_stock_info[0][i].code
        single_stock_data.history.append(read_stock_info[0][i].day_stock_detail)
        single_stock_data.analysis.append(a_day_stock_analysis())
        stocks_data[read_stock_info[0][i].code]=single_stock_data
    
    for i in range (1,len(read_stock_info)): #day iterations
        #print('transfer_day_struct_2_stock_stock '+str(i)+' '+str(read_stock_info[i][0].day_stock_detail.date)+ ' '+read_stock_info[i][0].code)
        for j in range (0,len(read_stock_info[i])): #stock iteration
            if (stocks_data.get(read_stock_info[i][j].code, 0) == 0): continue
            stocks_data[read_stock_info[i][j].code].history.append(read_stock_info[i][j].day_stock_detail)
            stocks_data[read_stock_info[i][j].code].analysis.append(a_day_stock_analysis())
            #if(read_stock_info[i][j].code=="0050"): 
                #print(read_stock_info[i][j].day_stock_detail.endprice)
    return stocks_data
        

def plot_a_stock_over_all_data_date_based(startdate,enddate,a_stock_info): # This function should ensure the input is a trade day
    startdate_index = -1
    enddate_index = 0
    end_price_list = list()
    date_list = list()
    ten_days_MA = list()
    twnty_days_MA = list()
    sixty_days_MA = list()
    for i in range (len(a_stock_info.history)-1,-1,-1):
        if(a_stock_info.history[i].date==int(startdate)): 
            startdate_index = i
        if(a_stock_info.history[i].date==int(enddate)): 
            enddate_index = i
            end_price_list.append(a_stock_info.history[i].endprice)
            ten_days_MA.append(a_stock_info.analysis[i].ten_days_MA)
            twnty_days_MA.append(a_stock_info.analysis[i].twnty_days_MA)
            sixty_days_MA.append(a_stock_info.analysis[i].sixty_days_MA)
            datstr=str(a_stock_info.history[i].date)[0:4]+'-'+str(a_stock_info.history[i].date)[4:6]+'-'+str(a_stock_info.history[i].date)[6:8]
            date_list.append(datetime.datetime(int(datstr[0:4]),int(datstr[5:7]),int(datstr[8:10])))
            break
        if (startdate_index != -1): 
            end_price_list.append(a_stock_info.history[i].endprice)
            ten_days_MA.append(a_stock_info.analysis[i].ten_days_MA)
            twnty_days_MA.append(a_stock_info.analysis[i].twnty_days_MA)
            sixty_days_MA.append(a_stock_info.analysis[i].sixty_days_MA)
            datstr=str(a_stock_info.history[i].date)[0:4]+'-'+str(a_stock_info.history[i].date)[4:6]+'-'+str(a_stock_info.history[i].date)[6:8]
            date_list.append(datetime.datetime(int(datstr[0:4]),int(datstr[5:7]),int(datstr[8:10])))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
    plt.plot(date_list,end_price_list,color='black',linewidth=3)
    plt.plot(date_list,ten_days_MA,'g')
    plt.plot(date_list,twnty_days_MA,'b')
    plt.plot(date_list,sixty_days_MA,'y')
    plt.gcf().autofmt_xdate()
    plt.show()
    
def plot_a_stock_over_all_data_index_based(startdate_index,enddate_index,a_stock_info):
    end_price_list = list()
    date_list = list()
    ten_days_MA = list()
    twnty_days_MA = list()
    sixty_days_MA = list()
    for i in range (startdate_index,enddate_index,-1):
        end_price_list.append(a_stock_info.history[i].endprice)
        ten_days_MA.append(a_stock_info.analysis[i].ten_days_MA)
        twnty_days_MA.append(a_stock_info.analysis[i].twnty_days_MA)
        sixty_days_MA.append(a_stock_info.analysis[i].sixty_days_MA)
        datstr=str(a_stock_info.history[i].date)[0:4]+'-'+str(a_stock_info.history[i].date)[4:6]+'-'+str(a_stock_info.history[i].date)[6:8]
        date_list.append(datetime(int(datstr[0:4]),int(datstr[5:7]),int(datstr[8:10])))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
    plt.plot(date_list,end_price_list,color='black',linewidth=3)
    plt.plot(date_list,ten_days_MA,'g')
    plt.plot(date_list,twnty_days_MA,'b')
    plt.plot(date_list,sixty_days_MA,'y')
    plt.gcf().autofmt_xdate()
    plt.show()


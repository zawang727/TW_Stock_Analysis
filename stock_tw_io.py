# Created with Pyto
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from dataclasses import dataclass
import codecs
  
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
        self.history=list()
 	
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
            if(day_stock.code=="1101"): 
                print(datestr+' '+str_list[7])
    return day_stock_list

def plot_a_stock_over_all_data(startdate,enddate,stockcode):
    

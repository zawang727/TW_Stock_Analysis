# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 20:44:55 2021

@author: RogerWang
"""
import importlib
from os import path

IOModuleFile = "stock_tw_io"
IOModule = importlib.import_module(IOModuleFile)


def fetch_all_stock_data():
    stockdata=list()
    year = 2020
    month = 7
    date = 28
    dayinmonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for day in range(0, 900):
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
        if (not path.exists(filestr)): continue
        stockdata.append(IOModule.stock_csv_reader(filestr,datestr))
        
def draw_all_month_moving_average(stockdata):
    
        
fetch_all_stock_data()



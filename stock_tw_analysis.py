# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 20:44:55 2021

@author: RogerWang
"""
import importlib
from os import path

IOModuleFile = "stock_tw_io"
IOModule = importlib.import_module(IOModuleFile)

def five_days_MA_generation_for_a_stock(a_stock_info):
    five_days_list = list()
    for i in range (0,len(a_stock_info.history)):
        five_days_list.append(a_stock_info.history[i].endprice)
        if (len(five_days_list)>5): del five_days_list[0]
        a_stock_info.analysis.append(IOModule.a_day_stock_analysis());
        a_stock_info.analysis[i]=sum(five_days_list)/float(len(five_days_list))
    

stockdata_in_days = IOModule.fetch_all_stock_data()
stockdata_in_stock_struct = IOModule.transfer_day_struct_2_stock_stock(stockdata_in_days)
for i in stockdata_in_stock_struct.keys():
    five_days_MA_generation_for_a_stock(stockdata_in_stock_struct[i])
    


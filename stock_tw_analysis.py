# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 20:44:55 2021

@author: RogerWang
"""
import importlib
from os import path
from datetime import datetime
import time
from joblib import Parallel, delayed

IOModuleFile = "stock_tw_io"
IOModule = importlib.import_module(IOModuleFile)

def five_days_MA_generation_for_a_stock(a_stock_info):
    days = 5
    days_list = list()
    for i in range (len(a_stock_info.history)-1,-1,-1): #days loop
        days_list.append(a_stock_info.history[i].endprice)
        if (len(days_list)>days): del days_list[0]
        a_stock_info.analysis[i].five_days_MA=sum(days_list)/float(len(days_list))
    
def ten_days_MA_generation_for_a_stock(a_stock_info):
    days = 10
    days_list = list()
    for i in range (len(a_stock_info.history)-1,-1,-1): #days loop
        days_list.append(a_stock_info.history[i].endprice)
        if (len(days_list)>days): del days_list[0]
        a_stock_info.analysis[i].ten_days_MA=sum(days_list)/float(len(days_list))
        
def twnty_days_MA_generation_for_a_stock(a_stock_info):
    days = 20
    days_list = list()
    for i in range (len(a_stock_info.history)-1,-1,-1): #days loop
        days_list.append(a_stock_info.history[i].endprice)
        if (len(days_list)>days): del days_list[0]
        a_stock_info.analysis[i].twnty_days_MA=sum(days_list)/float(len(days_list))
        
def sixty_days_MA_generation_for_a_stock(a_stock_info):
    days = 60
    days_list = list()
    for i in range (len(a_stock_info.history)-1,-1,-1): #days loop
        days_list.append(a_stock_info.history[i].endprice)
        if (len(days_list)>days): del days_list[0]
        a_stock_info.analysis[i].sixty_days_MA=sum(days_list)/float(len(days_list))
        
def twoh_fifty_MA_generation_for_a_stock(a_stock_info):
    days = 250
    days_list = list()
    for i in range (len(a_stock_info.history)-1,-1,-1): #days loop
        days_list.append(a_stock_info.history[i].endprice)
        if (len(days_list)>days): del days_list[0]
        a_stock_info.analysis[i].twoh_fifty_days_MA=sum(days_list)/float(len(days_list))
        
def twnty_days_max_generation(a_stock_info):
    days = 20
    maxprice = 0.0;
    days_list = list()
    for i in range (len(a_stock_info.history)-1,-1,-1): #days loop
        if (a_stock_info.history[i].maxprice>maxprice): 
             days_list.append(a_stock_info.history[i].maxprice)
             if (len(days_list)>days): del days_list[0]
             a_stock_info.analysis[i].twnty_days_max=max(days_list)
             
def twnty_days_min_generation(a_stock_info):
    days = 20
    minprice = 100000.0;
    days_list = list()
    for i in range (len(a_stock_info.history)-1,-1,-1): #days loop
        if (a_stock_info.history[i].minprice<minprice): 
             days_list.append(a_stock_info.history[i].minprice)
             if (len(days_list)>days): del days_list[0]
             a_stock_info.analysis[i].twnty_days_min=min(days_list)
             
def sixty_days_max_generation(a_stock_info):
    days = 60
    maxprice = 0.0;
    days_list = list()
    for i in range (len(a_stock_info.history)-1,-1,-1): #days loop
        if (a_stock_info.history[i].maxprice>maxprice): 
             days_list.append(a_stock_info.history[i].maxprice)
             if (len(days_list)>days): del days_list[0]
             a_stock_info.analysis[i].sixty_days_max=max(days_list)
             
def sixty_days_min_generation(a_stock_info):
    days = 60
    minprice = 100000.0;
    days_list = list()
    for i in range (len(a_stock_info.history)-1,-1,-1): #days loop
        if (a_stock_info.history[i].minprice<minprice): 
             days_list.append(a_stock_info.history[i].minprice)
             if (len(days_list)>days): del days_list[0]
             a_stock_info.analysis[i].sixty_days_min=min(days_list)
             
def twoh_fifty_days_max_generation(a_stock_info):
    days = 250
    maxprice = 0.0;
    days_list = list()
    for i in range (len(a_stock_info.history)-1,-1,-1): #days loop
        if (a_stock_info.history[i].maxprice>maxprice): 
             days_list.append(a_stock_info.history[i].maxprice)
             if (len(days_list)>days): del days_list[0]
             a_stock_info.analysis[i].twoh_fifty_days_max=max(days_list)
             
def twoh_fifty_days_min_generation(a_stock_info):
    days = 250
    minprice = 100000.0;
    days_list = list()
    for i in range (len(a_stock_info.history)-1,-1,-1): #days loop
        if (a_stock_info.history[i].minprice<minprice): 
             days_list.append(a_stock_info.history[i].minprice)
             if (len(days_list)>days): del days_list[0]
             a_stock_info.analysis[i].twoh_fifty_days_min=min(days_list)  
     
def single_stock_analysis(stockdata_in_stock_struct):
    five_days_MA_generation_for_a_stock(stockdata_in_stock_struct)
    ten_days_MA_generation_for_a_stock(stockdata_in_stock_struct)
    twnty_days_MA_generation_for_a_stock(stockdata_in_stock_struct)
    sixty_days_MA_generation_for_a_stock(stockdata_in_stock_struct)
    twoh_fifty_MA_generation_for_a_stock(stockdata_in_stock_struct)
    twnty_days_max_generation(stockdata_in_stock_struct)
    twnty_days_min_generation(stockdata_in_stock_struct)
    sixty_days_max_generation(stockdata_in_stock_struct)
    sixty_days_min_generation(stockdata_in_stock_struct)
    twoh_fifty_days_max_generation(stockdata_in_stock_struct)
    twoh_fifty_days_min_generation(stockdata_in_stock_struct)
    
    
def analysis_generation():
    stockdata_in_days = IOModule.fetch_all_stock_data()
    stockdata_in_stock_struct = IOModule.transfer_day_struct_2_stock_stock(stockdata_in_days)
    del stockdata_in_days
    for i in stockdata_in_stock_struct.keys():
        single_stock_analysis(stockdata_in_stock_struct[i])
    return stockdata_in_stock_struct

def if_all_above_MA(single_stock_data):
    score = 0.
    if (single_stock_data.history[0].endprice>single_stock_data.analysis[0].five_days_MA): score+=1.
    if (single_stock_data.history[0].endprice>single_stock_data.analysis[0].ten_days_MA): score+=1.
    if (single_stock_data.history[0].endprice>single_stock_data.analysis[0].twnty_days_MA): score+=2.
    if (single_stock_data.history[0].endprice>single_stock_data.analysis[0].sixty_days_MA): score+=3.
    if (single_stock_data.history[0].endprice>single_stock_data.analysis[0].twoh_fifty_days_MA): score+=1.
    if (single_stock_data.history[0].endprice*1.01 >single_stock_data.analysis[0].twnty_days_max): score+=1.
    if (single_stock_data.history[0].endprice*1.01 >single_stock_data.analysis[0].sixty_days_max): score+=1.5
    if (single_stock_data.history[0].endprice*1.01 >single_stock_data.analysis[0].twoh_fifty_days_max): score+=2.
    return score
    


#IOModule.plot_a_stock_over_all_data_date_based(20210623,20210723,tw_stockdata['1213'])
    
    


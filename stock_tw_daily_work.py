# Created with Pyto
import importlib
from os import path
from datetime import datetime
from joblib import Parallel, delayed

IOModuleFile = "stock_tw_io"
IOModule = importlib.import_module(IOModuleFile)
WebCrawModuleFile = "stockwebcraw"
WebCrawModule = importlib.import_module(WebCrawModuleFile)
AnalysisModuleFile = "stock_tw_analysis"
AnalysisModule = importlib.import_module(AnalysisModuleFile)

def daily_work():
    if (datetime.now().day >=5): 
        return 0 #stop if holiday
    WebCrawModule.craw_day()
    tw_stockdata = AnalysisModule.analysis_generation()
    pick_list=list()
    for i in tw_stockdata.keys():
        if (AnalysisModule.if_all_above_MA(tw_stockdata[i])>11.6): 
            print(i +' '+ tw_stockdata[i].name )
            pick_list.append(i +' '+ tw_stockdata[i].name)
            #IOModule.plot_a_stock_over_all_data_index_based(30,0,tw_stockdata[i])
    print(pick_list)
    
daily_work()
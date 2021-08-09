# Created with Pyto
import importlib
from os import path
from datetime import datetime
from joblib import Parallel, delayed
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

IOModuleFile = "stock_tw_io"
IOModule = importlib.import_module(IOModuleFile)
WebCrawModuleFile = "stockwebcraw"
WebCrawModule = importlib.import_module(WebCrawModuleFile)
AnalysisModuleFile = "stock_tw_analysis"
AnalysisModule = importlib.import_module(AnalysisModuleFile)

def send_email(content):
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("zawang727@gapp.nthu.edu.tw", "vzbxlzfsrvgydish")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)

def daily_work():
    if (datetime.now().weekday() >=5): 
        return 0 #stop if holiday
    WebCrawModule.craw_day()
    tw_stockdata = AnalysisModule.analysis_generation()
    text_result='Strong growing stock pick:\n'
    for i in tw_stockdata.keys():
        score = AnalysisModule.if_all_above_MA(tw_stockdata[i])
        if(score>11.6): 
            print(i +' '+ tw_stockdata[i].name+ ' score '+ str(score))
            text_result += (i +' '+ tw_stockdata[i].name+ ' score '+ str(score) +'\n')
            #IOModule.plot_a_stock_over_all_data_index_based(30,0,tw_stockdata[i])
    print(text_result)
    content = MIMEMultipart()  # 建立MIMEMultipart物件
    content["subject"] = "Daily Stock report"  # 郵件標題
    content["from"] = "zawang727@gapp.nthu.edu.tw"  # 寄件者
    content.attach(MIMEText(text_result))  # 郵件純文字內容
    content.attach(MIMEText('Score: \n+1: \nAbove 5 days MA, 10 days MA, 250 days MA\nIs month or season max\n+3:\nAbove 20 days MA\nIs 250 days max\n+2:\nAbove season MA'))  # 郵件純文字內容
    content["to"] = "<zawang727@gapp.nthu.edu.tw> " + "<zoe450283@gmail.com> " + "<StrooWang@gmail.com> " + "<zawang727@gmail.com> "  # 收件者
    send_email(content)
    
    
daily_work()
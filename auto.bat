@echo off
:check
"C:\Users\RogerWang\AppData\Local\Programs\Python\Python39\python.exe" "C:\Users\RogerWang\Desktop\StockProject\stock_tw_daily_work.py"

timeout /t 86400 /nobreak
GOTO :Check
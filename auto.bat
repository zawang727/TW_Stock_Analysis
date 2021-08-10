@echo off
:check
SET Hour=%NowTime:~0,2%
IF %Hour% EQU 17 (
"C:\Users\RogerWang\AppData\Local\Programs\Python\Python39\python.exe" "C:\Users\RogerWang\Desktop\StockProject\stock_tw_daily_work.py"
) 

timeout /t 3600 /nobreak
GOTO :Check
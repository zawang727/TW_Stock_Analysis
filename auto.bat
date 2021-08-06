@echo off
:check
if "%time%"==" 4:30 PM" (
"C:\Users\RogerWang\AppData\Local\Programs\Python\Python39\python.exe" "C:\Users\RogerWang\Desktop\StockProject\python stock_tw_daily_work.py"
pause
) 

timeout /t 30 /nobreak
GOTO :Check
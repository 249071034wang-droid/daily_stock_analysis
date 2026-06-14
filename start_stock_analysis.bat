@echo off
title Stock Analysis System - Starting...

echo ==================================
echo  Stock Analysis System WebUI
echo ==================================
echo.

:: Check if already running
netstat -ano | find "8000" >nul 2>&1
if %errorlevel%==0 (
    echo [WARNING] Port 8000 is already in use. Service may be running.
    echo Open browser at http://127.0.0.1:8000
    pause
    exit /b
)

:: Start service (background)
echo [INFO] Starting Web service...
start "" "C:\Users\24907\.workbuddy\binaries\python\versions\3.13.12\python.exe" main.py --webui-only

:: Wait for service to start (about 5-10 seconds)
echo [INFO] Waiting for service to start (about 10 seconds)...
timeout /t 10 /nobreak >nul

:: Auto-open browser
echo [INFO] Opening browser...
start http://127.0.0.1:8000

echo.
echo ==================================
echo  Service started!
echo  Browser opened: http://127.0.0.1:8000
echo  Closing this window will NOT stop the service.
echo ==================================
echo.
pause

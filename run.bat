@echo off
title Zyre Downloader Setup

echo Installing required packages and PyInstaller...
pip install -r requirements.txt pyinstaller -q

echo.
echo Building executable... (This might take a minute)
pyinstaller --onefile ytdownload.py

echo.
set /p choice="Would you like to install Zyre Downloader so you can just type 'ytdownload' in your Command Prompt anytime? (y/n): "
if /i "%choice%"=="y" (
    echo Moving ytdownload.exe to your User folder...
    copy /Y "dist\ytdownload.exe" "%USERPROFILE%\ytdownload.exe" >nul
    echo Done! Now whenever you open Command Prompt, you can just type 'ytdownload' to start it!
) else (
    echo.
    echo Okay! You can find the exe in the 'dist' folder.
)

pause

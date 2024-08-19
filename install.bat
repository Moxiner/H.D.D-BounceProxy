@echo off


setlocal enabledelayedexpansion
cd /d "%~dp0"
pip install -r requirements.txt -i  https://pypi.tuna.tsinghua.edu.cn/simples
echo ================================
echo  Requirements install Done.
echo ================================

copy ".\Font\black.ttf" "%windir%\Fonts" > nul


REM 更新字体缓存
echo Updating font cache...
rundll32.exe /s %windir%\System32\spool\DRIVERS\Color\fontcache.dll
echo ================================
echo  Font installed Done.
echo ================================

pause
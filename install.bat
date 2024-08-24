@echo off
chcp 65001 >nul

setlocal enabledelayedexpansion
cd /d "%~dp0"
pip install -r requirements.txt -i  https://pypi.tuna.tsinghua.edu.cn/simples
echo ================================
echo  Requirements install Done.
echo         环境安装完成
echo ================================

copy ".\Font\black.ttf" "%windir%\Fonts" > nul


REM 更新字体缓存

rundll32.exe /s %windir%\System32\spool\DRIVERS\Color\fontcache.dll
echo ================================
echo  Font installed Done.
echo      字体安装完成
echo ================================


echo ================================
echo  看控制台有没有报错,有的话就是没安装成功,多试几次

echo  记得右键使用管理员模式打开此脚本

echo  对了,记得在游戏中将副攻击键设置为Y

echo ================================

pause
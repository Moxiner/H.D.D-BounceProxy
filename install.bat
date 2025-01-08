@echo off
chcp 65001 2>&1

rem 检查是否以管理员权限运行
net session 2>&1
if %errorlevel% neq 0 (
    echo -------------------------------
    echo 尝试获取管理员权限中...
    echo -------------------------------
    rem 增加延迟时间，如遇无限循环，则可在此终止程序运行
    timeout /t 2
    PowerShell -Command "Start-Process '%~dpnx0' -Verb RunAs"
    exit /b
)

echo -------------------------------
echo 正在以管理员权限运行...
echo -------------------------------

set "MAINPATH=main.py"
set "ENV_DIR=%~dp0.env"

REM 调用环境配置脚本
set "APPPATH=%~dp0"
set "CURRENT_DIR=%APPPATH%"

REM 获取Python版本
python --version
if %errorlevel% neq 0 (
    echo [ERR] 获取 Python 版本失败。
    pause
    exit /b 1
)
for /f "tokens=*" %%i in ('python --version 2^>^&1') do set "PYTHON_VERSION=%%i"
REM 打印信息
echo [PASS] Python 版本: %PYTHON_VERSION%
echo [PASS] APPPATH: %APPPATH%
echo [PASS] MAINPATH: %MAINPATH%

REM 使用 PowerShell 检查路径中是否有中文字符
powershell -command "if ('%~dp0' -match '[\u4e00-\u9fff]') { exit 1 } else { exit 0 }"
if %errorlevel% equ 1 (
    echo [WARN] 当前路径包含中文字符
)

REM 检查路径中是否有空格
set "path_check=%~dp0"
if "%path_check%" neq "%path_check: =%" (
    echo [WARN] 路径中包含空格
)

REM 获取当前日期并格式化为 YYYYMMDD
for /f "tokens=2-4 delims=/ " %%a in ('echo %date%') do (
    set year=%%c
    set month=%%a
    set day=%%b
)

REM 获取当前时间
for /f "tokens=1-3 delims=/: " %%i in ('echo %time%') do (
    set hour=%%i
    set minute=%%j
    set second=%%k
)

REM 将小时和分钟格式化为两位数
set hour=%hour: =0%
set minute=%minute: =0%
set second=%second: =0%

REM 生成日志目录和文件名，格式为 YYYYMMDD 和 HH.MM.SS
set log_dir=%~dp0.log\%year%%month%%day%
set timestamp=%hour%.%minute%.%second%
set "BAT_LOG=%log_dir%\bat_%timestamp%.log"
set "PYTHON_LOG=%log_dir%\python_%timestamp%.log"



echo [PASS] Python已安装并配置正确。

REM 检查应用程序脚本路径
set "PYTHON_SCRIPT=%APPPATH%\%MAINPATH%"
if not exist "%PYTHON_SCRIPT%" (
    echo [WARN] 无法找到 Python 脚本文件: %PYTHON_SCRIPT%
    pause
    exit /b 1
)
cd /d "%APPPATH%"

REM 升级 pip 并检查是否成功
echo -------------------------------
echo 正在升级 pip...
echo -------------------------------
python -m pip install -i https://mirrors.aliyun.com/pypi/simple/ --upgrade pip
if %errorlevel% neq 0 (
    echo [ERR] 升级 pip 失败。
    pause
    exit /b 1
)
echo [PASS] pip 升级成功。

REM 安装 requirements.txt 并检查是否成功
echo -------------------------------
echo 正在安装 依赖包

echo [INFO] 正在安装 requirements.txt
echo -------------------------------
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
if %errorlevel% neq 0 (
    echo -------------------------------
    echo [ERR] 安装 requirements.txt 失败。
    echo 请重试或手动安装。
    echo -------------------------------
    
    pause
    exit /b 1
)

echo -------------------------------
echo [PASS] requirements.txt 安装成功。
echo -------------------------------

REM 安装字体
set "FONT_FILE_PATH=.\Font\black.ttf"  
set "SYSTEM_FONTS_DIR=%windir%\Fonts"

echo -------------------------------
echo 正在安装字体...
echo -------------------------------
%FONT_FILE_PATH%
if %errorlevel% neq 0 (
    echo [ERR] 字体安装失败。
    pause
    exit /b 1
)
echo [PASS] 字体安装成功。

REM 确认字体是否安装成功
setlocal enabledelayedexpansion
set "font_installed=false"
for /f "delims=" %%F in ('dir "%SYSTEM_FONTS_DIR%\black.ttf" /b 2^>nul') do (
    set "font_installed=true"
)
if "%font_installed%"=="false" (
    echo [ERR] 字体未正确安装
    pause
    exit /b 1
)
echo [PASS] 字体已成功安装并确认。

echo -------------------------------
echo 1. 请双击 run.bat 以启动 H.D.D 弹反
echo 2. 请在游戏中将攻击的辅助键位设置为 Y
echo -------------------------------

pause
exit /b 0
import threading
import keyboard
import time
import Evasion
import os
import art
from rich.spinner import Spinner
from rich.live import Live
from loguru import logger
import sys

logger.remove(0)
logger.add(
    sys.stderr,
    format="[\033[32m{time:YYYY-MMMM-D HH:mm:ss!UTC}\033[0m] [\033[34mH.D.D 代理\033[0m] [{level}] {message}",
)
# 创建一个事件对象，用于控制线程的运行和重启
event = threading.Event()
thread = None


def startlog():
    os.system("cls")
    art.tprint("H.D.D System")
    print("/" * 50)
    print("H.D.D代理已接入")
    print("/" * 50)


def my_task():
    """定义一个线程执行的任务"""
    while True:
        if event.is_set():
            Evasion.evasion()
        else:
            event.wait()  # 等待事件被设置


def print_task():
    """定义一个线程执行的任务"""

    while True:
        if event.is_set():

            logger.info("H.D.D代理运行中")

            time.sleep(1)
        else:
            logger.info("H.D.D代理已停止")
            event.wait()  # 等待事件被设置


def on_f8_pressed():
    """当按下F8时，如果线程暂停，则重新启动线程"""
    if not event.is_set():
        event.set()  # 设置事件，通知线程开始运行
        logger.info("H.D.D代理正在启动...")


def on_f9_pressed():
    """当按下F9时，停止线程"""
    event.clear()  # 清除事件，通知线程暂停
    logger.info("H.D.D代理正在停止...")
    time.sleep(1)
    os.system("cls")

    startlog()


startlog()
# 创建线程并启动
thread_evasion = threading.Thread(target=my_task)
thread_evasion.start()
thread_log = threading.Thread(target=print_task)
thread_log.start()
# 注册键盘事件
keyboard.on_press_key("f8", lambda _: on_f8_pressed())
keyboard.on_press_key("f9", lambda _: on_f9_pressed())


logger.info("按 F8 启动H.D.D代理，按 F9 停止H.D.D代理")
keyboard.wait()  # 等待键盘事件，使程序持续运行

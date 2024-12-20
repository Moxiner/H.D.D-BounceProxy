import threading
import keyboard
import time
from zzz_Bounceproxy import Evasion
import os
import art
from rich.spinner import Spinner
from rich.live import Live
from loguru import logger
import sys
from zzz_Bounceproxy import info
from ZZZSoundTrigger.Trigger import DodgingTrigger

SAMPLE_PATH = "./ZZZSoundTrigger/sample.wav"
COM_NAME = "COM3"
THRESHOLD = 0.1  # 阈值
EXPANSION_RATIO = 1.0  # 最大NCC系数

logger.remove(0)
logger.add(
    sys.stderr,
    format="[\033[32m{time:YYYY-MMMM-D HH:mm:ss!UTC}\033[0m] [\033[34mH.D.D 代理\033[0m] [{level}] {message}",
)
# 创建一个事件对象，用于控制线程的运行和重启
status = threading.Event()
thread = None
first = True
stop = threading.Event()


def initconfig():
    global evasion
    global bounce
    global determinemode
    global operationmode
    global outtone
    global intone
    config = info.read_config("./config.ini")
    evasion = config["setting"]["evasion"]
    bounce = config["setting"]["bounce"]
    determinemode = config["setting"]["determinemode"]
    operationmode = config["setting"]["operationmode"]
    outtone = config["setting"]["outtone"]
    intone = config["setting"]["intone"]


def startlog():
    initconfig()
    os.system("cls")
    art.tprint("H.D.D System")
    print("/" * 50)
    logger.critical("本项目完全开源免费")
    logger.critical("如果你是买来的，可凭此截图退款！")
    logger.critical("拒绝退款的，请举报该商家！")
    logger.critical("必要时请使用法律武器维护自己的合法权益！")
    logger.critical("本项目严禁任何人打着幌子倒卖或收取知识费，服务费，安装费等！")
    print("/" * 50)
    logger.info("H.D.D代理已接入")
    print("/" * 50)
    time.sleep(1)
    logger.info("H.D.D 代理初始化...")
    if first:
        info.play_sound("./Sound/Info.wav", int(outtone))


def my_task():
    """定义一个线程执行的任务"""

    while True:
        if status.is_set():
            if determinemode == "0":
                Evasion.evasion(evasion, bounce, operationmode, intone)
            if determinemode == "1":

                et = DodgingTrigger(
                    SAMPLE_PATH,
                    threshold=THRESHOLD,
                    ratio=EXPANSION_RATIO,
                    is_monitor=True,
                )
                et.online_listening(evasion, operationmode)

        else:
            status.wait()  # 等待事件被设置


def print_task():
    """定义一个线程执行的任务"""

    while True:
        if status.is_set():
            if determinemode == "0":
                logger.info("H.D.D 视觉代理运行中")

            if determinemode == "1":
                logger.info("H.D.D 音频代理运行中")
            evasion_list = ["极限弹反", "极限支援", "极限闪避"]
            bounce_list = ["同轴闪避", "极限双闪", "极限闪避"]
            operationmode_list = ["自动", "键鼠", "手柄"]
            operationmode_list = ["自动", "键鼠", "手柄"]
            operationmode_list = ["自动", "键鼠", "手柄"]
            outtone_list = ["开启", "关闭"]
            intone_list = ["开启", "关闭"]
            logger.info("=" * 20)
            logger.info(f"弹反  {evasion_list[int(evasion)]}")
            logger.info(f"闪避  {bounce_list[int(bounce)]}")
            logger.info(f"操作模式  {operationmode_list[int(operationmode)]}")
            logger.info(f"局外提示语音  {outtone_list[int(outtone)]}")
            logger.info(f"局内提示语音  {intone_list[int(intone)]}")
            time.sleep(3)
        else:
            status.wait()  # 等待事件被设置


startlog()


# 创建线程并启动
# thread_evasion = threading.Thread(target=my_task)
# thread_evasion.start()
# thread_log = threading.Thread(target=print_task)
# thread_log.start()
# # 注册键盘事件
# keyboard.on_press_key("f8", lambda _: on_f8_pressed())
# keyboard.on_press_key("f9", lambda _: on_f9_pressed())

# logger.info("按 F8 启动H.D.D代理，按 F9 停止H.D.D代理")
# keyboard.wait()  # 等待键盘事件，使程序持续运行

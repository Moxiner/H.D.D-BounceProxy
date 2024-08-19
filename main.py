from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QStackedWidget,
    QVBoxLayout,
    QApplication,
)
from PySide6.QtGui import QPixmap, QPainter, QIcon
import sys
from UI import main_ui
from UI import setting_ui
from UI import about_ui
from core import *
import webbrowser
from zzz_Bounceproxy.info import *
import threading
import keyboard

import multiprocessing
from soundcard.mediafoundation import SoundcardRuntimeWarning
from ZZZSoundTrigger.Trigger import DodgingTrigger

import warnings


VERSION = "v0.0.2 beta"
SAMPLE_PATH = "./ZZZSoundTrigger/sample.wav"

COM_NAME = "COM3"

THRESHOLD = 0.1  # 阈值
EXPANSION_RATIO = 1.0  # 最大NCC系数


class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建 UI
        self.ui = main_ui.Ui_Form()
        self.ui.setupUi(self)


class Setting(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建 UI
        self.ui = setting_ui.Ui_Form()
        self.ui.setupUi(self)


class About(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建 UI
        self.ui = about_ui.Ui_Form()
        self.ui.setupUi(self)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"H.D.D 弹反代理 {VERSION}")
        self.setWindowIcon(QIcon("./Image/Icon.ico"))
        self.initUI()
        self.initStart()

    def initUI(self):

        self.main_layout = QVBoxLayout(self)
        # 创建 QStackedWidget
        self.stacked_widget = QStackedWidget()
        self.home = Home()
        self.setting = Setting()
        self.about = About()
        self.about.ui.version_pushButton.setText(VERSION)
        self.stacked_widget.addWidget(self.home)
        self.stacked_widget.addWidget(self.setting)
        self.stacked_widget.addWidget(self.about)
        self.main_layout.addWidget(self.stacked_widget)
        self.stacked_widget.setCurrentIndex(0)
        self.BindKey()
        self.home.ui.stop_pushButton.hide()
        self.setting.ui.Evasion_comBox.setCurrentIndex(
            int(info.read_config("./config.ini")["setting"]["evasion"])
        )
        self.setting.ui.bounce_comboBox.setCurrentIndex(
            int(info.read_config("./config.ini")["setting"]["bounce"])
        )
        self.setting.ui.determineMode_comboBox.setCurrentIndex(
            int(info.read_config("./config.ini")["setting"]["determinemode"])
        )
        self.setting.ui.operationMode_comboBox.setCurrentIndex(
            int(info.read_config("./config.ini")["setting"]["operationmode"])
        )
        self.setting.ui.outTone_comboBox.setCurrentIndex(
            int(info.read_config("./config.ini")["setting"]["outtone"])
        )
        self.setting.ui.inTone_comboBox.setCurrentIndex(
            int(info.read_config("./config.ini")["setting"]["intone"])
        )

    def start(self):
        initconfig()
        if not status.is_set():
            status.set()  # 设置事件，通知线程开始运行
            logger.info("H.D.D代理正在启动...")
            info.play_sound("./Sound/Start.wav")
            first = False
            self.home.ui.start_pushButton.hide()
            self.home.ui.stop_pushButton.show()

    def stop(self):
        """当按下F9时，停止线程"""
        status.clear()  # 清除事件，通知线程暂停
        logger.info("H.D.D代理正在停止...")
        info.play_sound("./Sound/Stop.wav")

        self.home.ui.start_pushButton.show()
        self.home.ui.stop_pushButton.hide()

    def closeEvent(self, event):
        status.clear()  # 清除事件，通知线程暂停
        logger.info("H.D.D代理正在停止...")
        stop.set()

    def initStart(self):
        thread_evasion = threading.Thread(target=my_task)
        thread_evasion.start()
        thread_log = threading.Thread(target=print_task)
        thread_log.start()
        multiprocessing.freeze_support()
        # kbm = HardKbMouse(COM_NAME)  # 硬模拟

        et = DodgingTrigger(
            SAMPLE_PATH,
            threshold=THRESHOLD,
            ratio=EXPANSION_RATIO,
            is_monitor=True,
        )

    # et.online_listening()
    def BindKey(self):
        self.home.ui.setting_pushButton.clicked.connect(self.goto_SettingUI)
        self.setting.ui.back_pushButton.clicked.connect(self.goto_HomeUI)
        self.home.ui.exit_pushButton.clicked.connect(self.close)
        self.home.ui.start_pushButton.clicked.connect(self.start)
        self.home.ui.stop_pushButton.clicked.connect(self.stop)
        self.home.ui.about_pushButton.clicked.connect(self.goto_AboutUI)
        self.about.ui.back_pushButton.clicked.connect(self.goto_HomeUI)
        self.about.ui.xigua__pushButton.clicked.connect(
            lambda: webbrowser.open(
                "https://www.bilibili.com/video/BV1QUb6eYEA5/?share_source=copy_web&vd_source=cb6401bb53217ef7b31c26ec63b95347"
            )
        )
        self.about.ui.ImLaoBJie_pushButton.clicked.connect(
            lambda: webbrowser.open("https://github.com/ImLaoBJie/ZZZSoundTrigger")
        )
        self.about.ui.PPicku__pushButton.clicked.connect(
            lambda: webbrowser.open("https://github.com/PPicku/H.D.D-System")
        )
        self.about.ui.author_pushButton.clicked.connect(
            lambda: webbrowser.open("https://github.com/Moxiner")
        )
        # self.about.ui.openLog_pushButton.clicked.connect(self.openLog)
        self.setting.ui.Evasion_comBox.currentIndexChanged.connect(
            lambda: modify_config(
                "./config.ini",
                "setting",
                "evasion",
                str(self.setting.ui.Evasion_comBox.currentIndex()),
            )
        )
        self.setting.ui.bounce_comboBox.currentIndexChanged.connect(
            lambda: modify_config(
                "./config.ini",
                "setting",
                "bounce",
                str(self.setting.ui.bounce_comboBox.currentIndex()),
            )
        )
        self.setting.ui.determineMode_comboBox.currentIndexChanged.connect(
            lambda: modify_config(
                "./config.ini",
                "setting",
                "determinemode",
                str(self.setting.ui.determineMode_comboBox.currentIndex()),
            )
        )
        self.setting.ui.operationMode_comboBox.currentIndexChanged.connect(
            lambda: modify_config(
                "./config.ini",
                "setting",
                "operationmode",
                str(self.setting.ui.operationMode_comboBox.currentIndex()),
            )
        )
        self.setting.ui.outTone_comboBox.currentIndexChanged.connect(
            lambda: modify_config(
                "./config.ini",
                "setting",
                "outtone",
                str(self.setting.ui.outTone_comboBox.currentIndex()),
            )
        )
        self.setting.ui.inTone_comboBox.currentIndexChanged.connect(
            lambda: modify_config(
                "./config.ini",
                "setting",
                "intone",
                str(self.setting.ui.inTone_comboBox.currentIndex()),
            )
        )

    def goto_SettingUI(self):
        self.stacked_widget.setCurrentIndex(1)

    def goto_HomeUI(self):
        self.stacked_widget.setCurrentIndex(0)
        initconfig()

    def goto_AboutUI(self):
        self.stacked_widget.setCurrentIndex(2)

    def paintEvent(self, __):
        painter = QPainter(self)
        pixmap = QPixmap("./Image/bg.png")
        painter.drawPixmap(self.rect(), pixmap)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    logger.info("H.D.D 代理初始化完成...")
    keyboard.on_press_key("f8", lambda _: window.start())
    keyboard.on_press_key("f9", lambda _: window.stop())
    # keyboard.wait()  # 等待键盘事件，使程序持续运行
    # 应用字体到应用程序
    sys.exit(app.exec())

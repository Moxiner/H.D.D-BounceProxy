import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
from keyboad import *
from loguru import logger
import sys
import threading

# 创建一个事件对象，用于控制线程的运行和重启


# 捕捉怪物颜色攻击特效
class GetImgContours:
    def __init__(self, lower_hsv, upper_hsv, screenshot):
        self.screenshot = screenshot
        self.img = cv2.cvtColor(np.array(self.screenshot), cv2.COLOR_RGB2BGR)
        self.hsv_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        self.lower_hsv = lower_hsv
        self.upper_hsv = upper_hsv

    def get_contours(self):
        mask = cv2.inRange(self.hsv_img, self.lower_hsv, self.upper_hsv)
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        return contours

    def get_rectangle(self, contours):
        rectangle_info = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            # print(f"矩形框的宽：{w},高：{h}")
            rectangle_info.append((w, h))
        return rectangle_info


def evasion(evasion, bounce, operationmode, intone):
    time.sleep(0.02)
    width, height = pyautogui.size()
    # 传入自定义的光效颜色范围参数，为黄色
    lower_hsv_yellow = np.array([30, 108, 236])
    upper_hsv_yellow = np.array([30, 235, 255])
    # 传入自定义的光效颜色范围参数，为红色
    lower_hsv_red = np.array([0, 70, 240])
    upper_hsv_red = np.array([10, 160, 250])
    # 截取指定区域的图像
    screenshot = ImageGrab.grab((0, 0, width, height))
    # 创建类的实例
    contours_yellow = GetImgContours(lower_hsv_yellow, upper_hsv_yellow, screenshot)
    contours_red = GetImgContours(lower_hsv_red, upper_hsv_red, screenshot)
    w_h_list_yellow = contours_yellow.get_rectangle(contours_yellow.get_contours())
    w_h_list_red = contours_red.get_rectangle(contours_red.get_contours())

    if any(w > 300 and h <= 20 or w <= 20 and h > 300 for w, h in w_h_list_yellow):
        logger.info("\033[34mH.D.D 代理视觉触发 - 极限支援\033[0m")
        if int(operationmode) == 0:
            thread_keyboard = threading.Thread(
                target=keyboad, args=(int(evasion), 0, 1)
            )
            thread_joypad = threading.Thread(target=keyboad, args=(int(evasion), 0, 2))
            thread_keyboard.start()
            thread_joypad.start()
        else:
            keyboad(int(evasion), 0, int(operationmode))

        time.sleep(0.5)

    elif any(w > 300 and h <= 20 or w <= 20 and h > 300 for w, h in w_h_list_red):
        logger.info("\033[34mH.D.D 代理视觉触发 - 极限闪避\033[0m")
        if int(operationmode) == 0:
            thread_keyboard = threading.Thread(target=keyboad, args=(int(bounce), 1, 1))
            thread_joypad = threading.Thread(target=keyboad, args=(int(bounce), 1, 2))
            thread_keyboard.start()
            thread_joypad.start()
        else:
            keyboad(int(bounce), 1, int(operationmode))

        time.sleep(0.5)


def evasion_debug():
    time.sleep(0.02)
    width, height = pyautogui.size()
    # 传入自定义的光效颜色范围参数，为黄色
    lower_hsv_yellow = np.array([30, 108, 236])
    upper_hsv_yellow = np.array([30, 235, 255])
    # 传入自定义的光效颜色范围参数，为红色
    lower_hsv_red = np.array([0, 70, 240])
    upper_hsv_red = np.array([10, 160, 250])
    # 截取指定区域的图像
    screenshot = ImageGrab.grab((0, 0, width, height))
    # 创建类的实例
    contours_yellow = GetImgContours(lower_hsv_yellow, upper_hsv_yellow, screenshot)
    contours_red = GetImgContours(lower_hsv_red, upper_hsv_red, screenshot)
    w_h_list_yellow = contours_yellow.get_rectangle(contours_yellow.get_contours())
    w_h_list_red = contours_red.get_rectangle(contours_red.get_contours())

    # 查看捕捉结果
    if any(w > 0 and h > 0 for w, h in w_h_list_red):
        cv2.namedWindow("light contours", cv2.WINDOW_NORMAL)

        # 设置窗口大小为图像的大小
        cv2.resizeWindow("light contours", screenshot.width, screenshot.height)
        # 在原始图像上绘制轮廓
        cv2.drawContours(
            contours_red.img, contours_red.get_contours(), -1, (0, 0, 255), 1
        )

        # 绘制矩形相
        for contour in contours_red.get_contours():
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(contours_red.img, (x, y), (x + w, y + h), (255, 0, 0), 1)
        # 显示结果
        cv2.imshow("light contours", contours_red.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("未捕捉到目标")

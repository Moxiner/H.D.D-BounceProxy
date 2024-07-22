import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import time
import pydirectinput

import vgamepad

gamepad = vgamepad.VX360Gamepad()
# 定义所有的XBox360游戏手柄按键
UP = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
DOWN = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
LEFT = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
RIGHT = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT

START = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_START
BACK = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_BACK
GUIDE = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE

LEFT_THUMB = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB
RIGHT_THUMB = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB
LEFT_SHOULDER = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER
RIGHT_SHOULDER = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER

A = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A
B = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B
X = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X
Y = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_Y
from loguru import logger
import sys

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


def evasion():
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
        pydirectinput.press("space")
        gamepad.press_button(RIGHT_SHOULDER)
        gamepad.update()
        time.sleep(0.2)
        gamepad.release_button(RIGHT_SHOULDER)
        gamepad.update()
        logger.info("\033[34mH.D.D代理操作 - 格挡反击\033[0m")
        time.sleep(0.5)

    elif any(w > 300 and h <= 20 or w <= 20 and h > 300 for w, h in w_h_list_red):
        pydirectinput.press("shift")
        gamepad.press_button(A)
        gamepad.update()
        time.sleep(0.2)
        gamepad.release_button(A)
        gamepad.update()
        logger.info("\033[34mH.D.D代理操作 - 极限闪避\033[0m")

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

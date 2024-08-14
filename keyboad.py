import pydirectinput
import vgamepad
import time
from loguru import logger

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


def keyboad(moves, mode, operationmode):

    # 键盘模式
    if operationmode == 1:
        # 支援
        if mode == 0:
            # 同轴弹反（三弹）
            if moves == 3:
                pydirectinput.press("shift")
                time.sleep(0.04)
                pydirectinput.press("y")
                time.sleep(0.04)
                pydirectinput.press("space")
                time.sleep(0.08)
                pydirectinput.press("y")
                time.sleep(0.08)
                pydirectinput.press("space")
                logger.info("\033[34mH.D.D代理操作 -  同轴弹反\033[0m")
            # 极限弹反（弹一闪）
            elif moves == 0:
                pydirectinput.press("shift")
                time.sleep(0.04)
                pydirectinput.press("y")
                time.sleep(0.04)
                pydirectinput.press("space")
                time.sleep(0.08)
                pydirectinput.press("y")
                logger.info("\033[34mH.D.D 代理键盘操作 -  极限弹反\033[0m")
            # 极限支援
            elif moves == 1:
                pydirectinput.press("space")
                time.sleep(0.08)
                pydirectinput.press("y")
                logger.info("\033[34mH.D.D 代理键盘操作 -  极限支援\033[0m")
            # 极限闪避
            elif moves == 2:
                pydirectinput.press("shift")
                time.sleep(0.08)
                pydirectinput.press("y")

        # 闪避
        elif mode == 1:
            # 同轴闪避（三闪）
            if moves == 0:
                pydirectinput.press("shift")
                time.sleep(0.05)
                pydirectinput.press("y")
                time.sleep(0.08)
                pydirectinput.press("space")
                time.sleep(0.05)
                pydirectinput.press("y")
                time.sleep(0.08)
                pydirectinput.press("space")
                logger.info("\033[34mH.D.D 代理键盘操作 -  同轴闪避\033[0m")
            # 极限双闪（双反闪）
            elif moves == 1:
                pydirectinput.press("shift")
                time.sleep(0.05)
                pydirectinput.press("y")
                time.sleep(0.08)
                pydirectinput.press("space")
                time.sleep(0.05)
                pydirectinput.press("y")
                logger.info("\033[34mH.D.D 代理键盘操作 -  极限双闪\033[0m")
            # 极限闪避
            elif moves == 2:
                pydirectinput.press("shift")
                time.sleep(0.05)
                pydirectinput.press("y")
                logger.info("\033[34mH.D.D 代理键盘操作 -  极限闪避\033[0m")

    elif operationmode == 2:
        # 支援
        if mode == 0:
            # 同轴弹反（三弹）
            if moves == 3:
                gamepad.press_button(A)
                gamepad.update()
                time.sleep(0.05)
                gamepad.release_button(A)
                gamepad.update()
                time.sleep(0.02)
                gamepad.press_button(X)
                gamepad.update()
                time.sleep(0.05)
                gamepad.release_button(X)
                gamepad.update()
                time.sleep(0.02)
                gamepad.press_button(RIGHT_SHOULDER)
                gamepad.update()
                time.sleep(0.05)
                gamepad.release_button(RIGHT_SHOULDER)
                gamepad.update()
                time.sleep(0.02)
                gamepad.press_button(A)
                gamepad.update()
                time.sleep(0.05)
                gamepad.release_button(A)
                gamepad.update()
                time.sleep(0.02)
                gamepad.press_button(RIGHT_SHOULDER)
                gamepad.update()
                time.sleep(0.05)
                gamepad.release_button(RIGHT_SHOULDER)
                gamepad.update()
                time.sleep(0.02)
                logger.info("\033[34mH.D.D 代理手柄操作 -  同轴弹反\033[0m")

            # 极限弹反（弹一闪）
            elif moves == 0:
                gamepad.press_button(A)
                gamepad.update()
                time.sleep(0.05)
                gamepad.release_button(A)
                gamepad.update()
                time.sleep(0.02)
                gamepad.press_button(X)
                gamepad.update()
                time.sleep(0.05)
                gamepad.release_button(X)
                gamepad.update()
                time.sleep(0.02)
                gamepad.press_button(RIGHT_SHOULDER)
                gamepad.update()
                time.sleep(0.02)
                gamepad.release_button(RIGHT_SHOULDER)
                gamepad.update()
                time.sleep(0.05)
                logger.info("\033[34mH.D.D 代理手柄操作 -  极限弹反\033[0m")

            # 极限支援
            elif moves == 1:
                gamepad.press_button(RIGHT_SHOULDER)
                gamepad.update()
                time.sleep(0.02)
                gamepad.release_button(RIGHT_SHOULDER)
                gamepad.update()
                time.sleep(0.05)
                logger.info("\033[34mH.D.D 代理手柄操作 -  极限支援\033[0m")
            # 极限闪避
            elif moves == 2:
                gamepad.press_button(A)
                gamepad.update()
                time.sleep(0.02)
                gamepad.release_button(A)
                gamepad.update()
                time.sleep(0.05)
                logger.info("\033[34mH.D.D 代理手柄操作 -  极限闪避\033[0m")

        # 闪避
        elif mode == 1:
            # 同轴闪避（三闪）
            if moves == 0:
                gamepad.press_button(A)
                gamepad.update()
                time.sleep(0.02)
                gamepad.release_button(A)
                gamepad.update()
                time.sleep(0.05)
                gamepad.press_button(X)
                gamepad.update()
                time.sleep(0.02)
                gamepad.release_button(X)
                gamepad.update()
                time.sleep(0.05)
                gamepad.press_button(RIGHT_SHOULDER)
                gamepad.update()
                time.sleep(0.02)
                gamepad.release_button(RIGHT_SHOULDER)
                gamepad.update()
                time.sleep(0.05)
                gamepad.press_button(A)
                gamepad.update()
                time.sleep(0.02)
                gamepad.release_button(A)
                gamepad.update()
                time.sleep(0.05)
                gamepad.press_button(RIGHT_SHOULDER)
                gamepad.update()
                time.sleep(0.02)
                gamepad.release_button(RIGHT_SHOULDER)
                gamepad.update()
                time.sleep(0.05)
                logger.info("\033[34mH.D.D 代理手柄操作 -  同轴闪避\033[0m")
            # 极限双闪（双反闪）
            elif moves == 1:
                gamepad.press_button(A)
                gamepad.update()
                time.sleep(0.02)
                gamepad.release_button(A)
                gamepad.update()
                time.sleep(0.05)
                gamepad.press_button(X)
                gamepad.update()
                time.sleep(0.02)
                gamepad.release_button(X)
                gamepad.update()
                time.sleep(0.05)
                gamepad.press_button(RIGHT_SHOULDER)
                gamepad.update()
                time.sleep(0.02)
                gamepad.release_button(RIGHT_SHOULDER)
                gamepad.update()
                logger.info("\033[34mH.D.D 代理手柄操作 -  极限双闪\033[0m")
            # 极限闪避
            elif moves == 2:
                gamepad.press_button(A)
                gamepad.update()
                time.sleep(0.02)
                gamepad.release_button(A)
                gamepad.update()
                logger.info("\033[34mH.D.D 代理手柄操作 -  极限闪避\033[0m")

import pygame
import time


def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


import os
import configparser

config_file_path = "config.ini"


def read_config(file_path):
    # 创建 configparser 对象
    config = configparser.ConfigParser()

    # 检查文件是否存在
    if not os.path.exists(file_path):
        # 如果文件不存在，则创建一个默认的配置文件
        with open(file_path, "w") as configfile:
            # 添加默认的配置项
            config["setting"] = {
                "evasion": "0",
                "bounce": "0",
                "determineMode": "true",
                "operationMode": "auto",
                "outTone": "true",
                "inTone": "true",
            }
            # 写入配置文件
            config.write(configfile)
    # 读取配置文件
    config.read(file_path)

    # 将配置转换为字典
    config_dict = {section: dict(config[section]) for section in config.sections()}

    return config_dict


def modify_config(file_path, filecofig, fileitem, filevalue):
    # 创建 configparser 对象
    config = configparser.ConfigParser()

    # 读取配置文件
    config.read(file_path)

    # 修改配置
    config.set(filecofig, fileitem, filevalue)

    # 保存修改后的文件
    with open(file_path, "w") as configfile:
        config.write(configfile)



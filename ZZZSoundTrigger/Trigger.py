import time
import random

import serial

import numpy as np

import librosa

import pydirectinput

import win32con
import win32api
from loguru import logger
import ctypes
from ctypes import wintypes

from ZZZSoundTrigger.Listener import GameAudioListener
import threading
from keyboad import *
from loguru import logger


class DodgingTrigger(GameAudioListener):
    monitor_time = 5  # 秒

    def __init__(self, sample_path: str, threshold=0.1, ratio=1.0, is_monitor=False):
        self.threshold = threshold
        self.is_monitor = is_monitor
        if self.is_monitor:
            self.len_samples = int(self.monitor_time / self.sample_len)
            # self.monitor = WaveMonitor(self.len_samples, self.threshold)
            self.monitor_array = np.zeros(shape=(self.len_samples,), dtype=np.float64)
        super().__init__(sample_path, ratio)

    def online_listening(
        self,
        evasion,
        operationmode,
    ):

        last_frames = np.empty(shape=(0,), dtype=np.float64)
        is_past_triggered = False

        with self.audio_instance as audio_recorder:
            current_frame = np.empty(shape=(0,), dtype=np.float64)
            for index in range(int(self.used_sr / self.chunk_size * self.sample_len)):
                stream_data = audio_recorder.record(numframes=self.chunk_size)
                read_chunks = librosa.to_mono(stream_data.T)

                current_frame = np.append(current_frame, read_chunks)

            # 积累完成,计算匹配分数
            combined_frames = np.append(last_frames, current_frame)
            max_score = self.matching(combined_frames)
            if self.is_monitor:
                self.monitor_array[:-1] = self.monitor_array[1:]
                self.monitor_array[-1] = max_score
            #     self.monitor.update_array(self.monitor_array)

            if max_score >= self.threshold:
                logger.info("\033[34mH.D.D 代理音频触发 - 极限支援/极限支援\033[0m")
                # if not is_past_triggered:  # 应该可以连续激发
                if int(operationmode) == 0:
                    thread_keyboard = threading.Thread(
                        target=keyboad, args=(int(evasion), 0, 1)
                    )
                    thread_joypad = threading.Thread(
                        target=keyboad, args=(int(evasion), 0, 2)
                    )
                    thread_keyboard.start()
                    thread_joypad.start()
                else:
                    keyboad(int(evasion), 0, int(operationmode))

                time.sleep(0.5)
                is_past_triggered = True
            else:
                is_past_triggered = False

            last_frames = current_frame

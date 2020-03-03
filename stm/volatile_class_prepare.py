import cv2
import numpy as np
import serial
from stm.send_serial import SendSerial


class VolatileClassPrepare(SendSerial):
    one_egg_img = cv2.imread("data\\one_egg.png")

    def __init__(self):
        self.next_state = 'None'
        self.number_of_egg = -1
        self.hatched_egg = 0
        self.shiny_number = 0
        #one_egg_img = cv2.imread("data\\one_egg.png")
        self._control_flg = 0
        #self._ser = serial.Serial('COM5', 9600)
        self._control_frame_count = 0
        self.send_command = 'None'

    def count_egg(self, frame, key):
        if key == ord('g'):
            self.number_of_egg = self.detect_egg(frame)
            self._control_flg = 1
            #self.next_state = 'RUN'

    def detect_egg(self, frame):
        detect_egg_cnt = 0
        egg_tmprate = np.int8(VolatileClassPrepare.one_egg_img)
        egg1 = np.int8(frame[211:290, 57:450, :])
        egg2 = np.int8(frame[307:386, 57:450, :])
        egg3 = np.int8(frame[403:482, 57:450, :])
        egg4 = np.int8(frame[499:578, 57:450, :])
        egg5 = np.int8(frame[595:674, 57:450, :])
        egg1_dif = np.amax(abs(egg_tmprate - egg1))
        egg2_dif = np.amax(abs(egg_tmprate - egg2))
        egg3_dif = np.amax(abs(egg_tmprate - egg3))
        egg4_dif = np.amax(abs(egg_tmprate - egg4))
        egg5_dif = np.amax(abs(egg_tmprate - egg5))

        if egg1_dif <= 100:
            detect_egg_cnt = detect_egg_cnt + 1
        if egg2_dif <= 100:
            detect_egg_cnt = detect_egg_cnt + 1
        if egg3_dif <= 100:
            detect_egg_cnt = detect_egg_cnt + 1
        if egg4_dif <= 100:
            detect_egg_cnt = detect_egg_cnt + 1
        if egg5_dif <= 100:
            detect_egg_cnt = detect_egg_cnt + 1
        # print(detect_egg_cnt)
        return detect_egg_cnt

    def state_action(self, frame, key, num_egg, htc_egg, shiny_number):
        #print('open menu -> pokemon')
        # print("prepare")
        self.count_egg(frame, key)
        if self._control_flg == 1:
            if self._control_frame_count == 0:
                self.send_command = 'Button B'
            #if self._control_frame_count == 6:
            #    self.send_command = 'Stop'
            elif self._control_frame_count == 170:
                self.send_command = 'Button B'
            elif self._control_frame_count == 230:
                #    self.send_command = 'Stop'
                self._control_frame_count = 0
                self._control_frame_count = 0
                self.next_state = 'RUN'
            else:
                self.send_command = 'None'
            self._control_frame_count += 1

        self.action_frame = frame

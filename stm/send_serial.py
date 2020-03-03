import argparse
import serial
from time import sleep


class SendSerial(object):
    def __init__(self):
        self._ser = serial.Serial('COM3', 38400)

    def send_command_start(self, msg):
        # print(msg)
        self._ser.write(f'{msg}\r\n'.encode('utf-8'))

    def send_command_stop(self):
        # print('STOP')
        self._ser.write(b'0 0 8 128 128 128 128\r\n')

    def command_cont(self, k, send_command):
        if k == ord('v') or send_command == 'Button A':
            self.send_command_start('0 4 8 128 128 128 128')
            sleep(0.1)
            self.send_command_stop()
        if k == ord('b') or send_command == 'Button B':
            self.send_command_start('0 2 8 128 128 128 128')
            sleep(0.1)
            self.send_command_stop()
        if k == ord('x') or send_command == 'Button X':
            self.send_command_start('0 8 8 128 128 128 128')
            sleep(0.1)
            self.send_command_stop()
        if k == ord('y') or send_command == 'Button Y':
            self.send_command_start('0 1 8 128 128 128 128')
            sleep(0.1)
            self.send_command_stop()
        if k == ord('r') or send_command == 'Button R':
            self.send_command_start('0 32 8 128 128 128 128')
            sleep(0.1)
            self.send_command_stop()
        if k == ord('w'):
            self.send_command_start('0 0 8 128 1 128 128')
            sleep(0.1)
            self.send_command_stop()
        if k == ord('a'):
            self.send_command_start('0 0 8 1 128 128 128')
            sleep(0.1)
            self.send_command_stop()
        if k == ord('s'):
            self.send_command_start('0 0 8 128 255 128 128')
            sleep(0.1)
            self.send_command_stop()
        if k == ord('d'):
            self.send_command_start('0 0 8 255 128 128 128')
            sleep(0.1)
            self.send_command_stop()
        if k == ord('h'):
            self.send_command_start('16 0 8 128 128 128 128')
            sleep(0.1)
            self.send_command_stop()
        if k == ord('p') or send_command == 'Button START':
            self.send_command_start('1 0 8 128 128 128 128')
            sleep(0.1)
            self.send_command_stop()
        if k == ord('i') or send_command == 'HAT TOP':
            self.send_command_start('0 0 0 128 128 128 128')
            sleep(0.07)
            self.send_command_stop()
        if k == ord('l') or send_command == 'HAT RIGHT':
            self.send_command_start('0 0 2 128 128 128 128')
            sleep(0.1)
            self.send_command_stop()
        if k == ord('k') or send_command == 'HAT BOTTOM':
            self.send_command_start('0 0 4 128 128 128 128')
            sleep(0.07)
            self.send_command_stop()
        if k == ord('j') or send_command == 'HAT LEFT':
            self.send_command_start('0 0 6 128 128 128 128')
            sleep(0.1)
            self.send_command_stop()
        if send_command == 'SEL SORA':
            self.send_command_start('0 0 8 128 1 128 128')
            sleep(0.04)
            self.send_command_start('0 0 8 255 128 128 128')
            sleep(0.03)
            self.send_command_stop()
        if send_command == 'RUN BRE':
            self.send_command_start('0 0 8 1 128 128 128')
            sleep(0.08)
            self.send_command_stop()
            sleep(0.08)
            self.send_command_start('0 0 8 128 1 128 128')
            sleep(0.3)
            self.send_command_stop()
        if send_command == 'RUN 2 RUN_R':
            self.send_command_start('0 0 8 128 255 128 128')
            sleep(0.15)
            self.send_command_start('0 0 8 255 128 128 128')
            sleep(0.4)
            self.send_command_start('0 0 8 128 1 128 128')
            sleep(0.04)
            self.send_command_stop()
        if send_command == 'LX MIN':
            self.send_command_start('0 0 8 1 128 128 128')
        if send_command == 'LX MAX':
            self.send_command_start('0 0 8 255 128 128 128')
        if send_command == 'LY MIN':
            self.send_command_start('0 0 8 128 1 128 128')
        if send_command == 'LY MAX':
            self.send_command_start('0 0 8 128 255 128 128')
        if send_command == 'I B':
            self.send_command_start('0 2 8 128 128 128 128')
        if send_command == 'I LX MIN':
            self.send_command_start('0 0 8 1 128 128 128')
            sleep(0.05)
            self.send_command_stop()
        if send_command == 'I LX MAX':
            self.send_command_start('0 0 8 255 128 128 128')
            sleep(0.05)
            self.send_command_stop()
        if send_command == 'STOP':
            self.send_command_stop()

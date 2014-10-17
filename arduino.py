#!/usr/bin/env python

import serial

class arduinocoms:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600)
        self.ser.open()
        self.ser.write(b'H')
        
    def blink(self):
        self.ser.write(b'D')

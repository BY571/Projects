import RPi.GPIO as GPIO
from time import sleep
#from PIL import Image
import picamera.array
import numpy as np
#import picamera
import thread
import curses
#import argparse
import sys
#import csv
import os


class Controller:

    MotorFront1 = 23
    MotorFront2 = 24
    MotorFront = 20

    MotorBack1 = 17
    MotorBack2 = 22
    MotorBack = 26
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.MotorFront1, GPIO.OUT)
        GPIO.setup(self.MotorFront2, GPIO.OUT)
        GPIO.setup(self.MotorFront, GPIO.OUT)
        GPIO.output(self.MotorFront, 0)

        GPIO.setup(self.MotorBack1, GPIO.OUT)
        GPIO.setup(self.MotorBack2, GPIO.OUT)
        GPIO.setup(self.MotorBack, GPIO.OUT)
        GPIO.output(self.MotorBack, 0)
        self.BackPWM = GPIO.PWM(self.MotorBack,100)
        self.BackPWM.start(0)
        self.BackPWM.ChangeDutyCycle(0)
        
        self.direction = 0
    
    def front(self,f1,f2,f):
        GPIO.output(self.MotorFront1, f1)
        GPIO.output(self.MotorFront2, f2)
        GPIO.output(self.MotorFront, f)

    def rear(self,b1,b2,b):
        GPIO.output(self.MotorBack1, b1)
        GPIO.output(self.MotorBack2, b2)
        self.BackPWM.ChangeDutyCycle(b)
    
    def steering(self):
        while True:
            char = screen.getch()
            if char == ord('d'):
                self.front(0, 1, 1)
                self.direction = 1
            elif char == ord('a'):
                self.front(1, 0, 1)
                self.direction = 2
            elif char == ord('s'):
                self.front(0, 0, 0)
                self.direction = 0 
            if char == ord('w'):
                self.rear(0, 1, 50)#70
            if char == ord(' '):
                self.rear(1, 0, 1)
                sleep(0.1)
                self.rear(0, 0, 0)
            if char == ord("q"):
                break


if __name__ == '__main__':
    try:
        screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        screen.keypad(True)
        carCtrl = Controller()
        carCtrl.steering()
        curses.nocbreak()
        screen.keypad(0)
        curses.echo()
        curses.endwin()
        #carCtrl.BackPWM.stop()
        GPIO.cleanup()

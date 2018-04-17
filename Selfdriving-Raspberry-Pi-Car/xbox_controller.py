#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:09:21 2018

@author: sebastian
"""

import xbox
#import RPi.GPIO as gpio
 #Right trigger position (values 0 to 1.0)

def control():
    joy = xbox.Joystick()

    #(x,y)    = joy.leftStick()    #Returns tuple containing left X and Y axes (values -1.0 to 1.0)
    #trigger  = joy.rightTrigger()
    while True:
        if joy.leftX():
            print("X: {}".format(joy.leftX()))
            #acc = joy.leftX() * 50
            #print(acc)
        if joy.leftY():
            print("Y: {}".format(joy.leftY()))
        
        if joy.B():
            joy.close()
            #gpio.cleanup()
            break
        
        if joy.A():                   #Test state of the A button (1=pressed, 0=not pressed)
            print ('A button pressed')
        else:
            pass

def main():
    control()

if __name__ == "__main__":
    main()

import RPi.GPIO as GPIO
from time import sleep
import xbox

class Controller:

    MotorFront1 = 17 #23
    MotorFront2 = 22 #24
    MotorFront = 26 #20

    MotorBack1 = 23 #17
    MotorBack2 = 24 #22
    MotorBack = 20 #26
    
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
        self.FrontPWM = GPIO.PWM(self.MotorFront,50)
        self.FrontPWM.start(0)
        self.FrontPWM.ChangeDutyCycle(0)
        self.BackPWM = GPIO.PWM(self.MotorBack,100)
        self.BackPWM.start(0)
        self.BackPWM.ChangeDutyCycle(0)
        
        #self.direction = 0
    
    def front(self,f1,f2,f):
        GPIO.output(self.MotorFront1, f1)
        GPIO.output(self.MotorFront2, f2)
        #GPIO.output(self.MotorFront, f)
        self.FrontPWM.ChangeDutyCycle(f)

    def rear(self,b1,b2,b):
        GPIO.output(self.MotorBack1, b1)
        GPIO.output(self.MotorBack2, b2)
        self.BackPWM.ChangeDutyCycle(b)
    
    def steering(self):
        joy = xbox.Joystick()
        while True:
            if joy.leftX():
                # an dem Wert fr die Lenkung spielen.. was macht sinn wo laesst sich das auto gut steuern
                steer = 40 * joy.leftX()*abs(joy.leftX())
                print("X-Axis: {}".format(steer))
                if steer >= 0:
                    #Powering steering right
                    self.front(1, 0, steer)
                    #self.direction = 1

                if steer < 0:
                    #Powering steering
                    self.front(0, 1, -1*steer)
                    #self.direction = 2
                else:
		    pass
                
            if joy.leftY():
                # 50 - max power for acceleration (TUNING PARAMETER!)
                acceleration = 100 * joy.leftY()*abs(joy.leftY())
                print("Y-Axis: {}".format(acceleration))
                if acceleration >= 0:
                    #Powering forward
                    self.rear(1, 0, acceleration)
                if acceleration < 0:
                    #Powering backwards attention power hast to be positiv _ output is negative-> *-1
                    self.rear(0, 1, -1*acceleration)
		else:
		    pass
			
            if joy.B():
                print("B pressed! Goodbye!")
                joy.close()
                GPIO.cleanup()
                break



if __name__ == '__main__':
    try:
        carCtrl = Controller()
        carCtrl.steering()
        
    except OSError as err:
        print(err)
        pass


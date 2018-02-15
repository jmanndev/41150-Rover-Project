import os#importing os library so as to communicate with the system
import time #importing time library to make Rpi wait because its too impatient
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library

RIGHT_MOTOR = 18
LEFT_MOTOR = 17
idle_throttle = 1500
off_throttle = 0
clockwise_throttle = 1900
anticlock_throttle = 1100

class Motor:
    
    pi = ""
    
    def __init__(self):
        time.sleep(1)
        self.pi = pigpio.pi()

        
    def off(self, timer):
        print('OFF')
        self.log('both', 'off', off_throttle)
        self.adjust_motor(LEFT_MOTOR, off_throttle)
        self.adjust_motor(RIGHT_MOTOR, off_throttle)
        time.sleep(timer)
        self.pi.stop()
        return


    def idle(self, timer):
        self.log('both', 'idle', idle_throttle)
        self.adjust_motor(LEFT_MOTOR, idle_throttle)
        self.adjust_motor(RIGHT_MOTOR, idle_throttle)
        time.sleep(timer)
        return


    def right(self, timer):
        print("RIGHT")
        self.idle(2)
        self.log('both', 'right', clockwise_throttle)
        self.adjust_motor(LEFT_MOTOR, clockwise_throttle)
        self.adjust_motor(RIGHT_MOTOR, clockwise_throttle)
        time.sleep(timer)
        return


    def left(self, timer):
        print("LEFT")
        self.idle(2)
        self.log('both', 'left', anticlock_throttle)
        self.adjust_motor(LEFT_MOTOR, anticlock_throttle)
        self.adjust_motor(RIGHT_MOTOR, anticlock_throttle)
        time.sleep(timer)
        return


    def forward(self, timer):
        print("FORWARD")
        self.idle(2)
        self.log('right', 'forward', clockwise_throttle)
        self.log('left', 'forward', anticlock_throttle)
        self.adjust_motor(LEFT_MOTOR, anticlock_throttle)
        self.adjust_motor(RIGHT_MOTOR, clockwise_throttle)
        time.sleep(timer)
        return


    def backward(self, timer):
        print("BACKWARD")
        self.idle(2)
        self.log('right', 'backward', anticlock_throttle)
        self.log('left', 'backward', clockwise_throttle)
        self.adjust_motor(LEFT_MOTOR, clockwise_throttle)
        self.adjust_motor(RIGHT_MOTOR, anticlock_throttle)
        time.sleep(timer)
        return


    def adjust_motor(self, motor, rpm):
        self.pi.set_servo_pulsewidth(motor, rpm)
        return


    def log(self, motor, direction, rpm):
        print(str(motor) + " " + str(direction) + " with " + str(rpm))
        return



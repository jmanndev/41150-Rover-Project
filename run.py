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


def off(timer):
    print('OFF')
    log('both', 'off', off_throttle)
    adjust_motor(LEFT_MOTOR, off_throttle)
    adjust_motor(RIGHT_MOTOR, off_throttle)
    time.sleep(timer)
    return


def idle(timer):
    log('both', 'idle', idle_throttle)
    adjust_motor(LEFT_MOTOR, idle_throttle)
    adjust_motor(RIGHT_MOTOR, idle_throttle)
    time.sleep(timer)
    return


def right(timer):
    print("RIGHT")
    idle(2)
    log('both', 'right', clockwise_throttle)
    adjust_motor(LEFT_MOTOR, clockwise_throttle)
    adjust_motor(RIGHT_MOTOR, clockwise_throttle)
    time.sleep(timer)
    return


def left(timer):
    print("LEFT")
    idle(2)
    log('both', 'left', anticlock_throttle)
    adjust_motor(LEFT_MOTOR, anticlock_throttle)
    adjust_motor(RIGHT_MOTOR, anticlock_throttle)
    time.sleep(timer)
    return


def forward(timer):
    print("FORWARD")
    idle(2)
    log('right', 'forward', clockwise_throttle)
    log('left', 'forward', anticlock_throttle)
    adjust_motor(LEFT_MOTOR, anticlock_throttle)
    adjust_motor(RIGHT_MOTOR, clockwise_throttle)
    time.sleep(timer)
    return


def backward(timer):
    print("BACKWARD")
    idle(2)
    log('right', 'backward', anticlock_throttle)
    log('left', 'backward', clockwise_throttle)
    adjust_motor(LEFT_MOTOR, clockwise_throttle)
    adjust_motor(RIGHT_MOTOR, anticlock_throttle)
    time.sleep(timer)
    return


def adjust_motor(motor, rpm):
    pi.set_servo_pulsewidth(motor, rpm)
    return


def log(motor, direction, rpm):
    print(str(motor) + " " + str(direction) + " with " + str(rpm))
    return

responce = raw_input("press Enter to continue")
print ("Switch ON the ESC")
responce = raw_input("press Enter to continue")

time.sleep(1)
pi = pigpio.pi()
idle(3)
forward(5)
backward(5)
left(5)
right(5)
off(1)
pi.stop()


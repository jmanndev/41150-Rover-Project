# Tags generated with -     http://patorjk.com/software/taag/#p=display&f=Big

import logging
import sys
import time                             
import os
import RPi.GPIO as SONIC_GPIO
import pigpio    



RIGHT_MOTOR_GPIO = 12
LEFT_MOTOR_GPIO = 16
PROPELLOR_MOTOR_GPIO = 19


SONIC_GPIO_TRIGGER = 23
SONIC_GPIO_ECHO = 24


#  __  __       _             
# |  \/  |     | |            
# | \  / | ___ | |_ ___  _ __ 
# | |\/| |/ _ \| __/ _ \| '__|
# | |  | | (_) | || (_) | |   
# |_|  |_|\___/ \__\___/|_|   

    
class Motor:
    idle_throttle = 1500
    off_throttle = 0
    clockwise_throttle = 1900
    anticlock_throttle = 1100
    
    def __init__(self, motorName, gpio):
        self.name = motorName
        self.gpioPin = gpio
        self.pi = pigpio.pi()
        self.idle()

        
    def off(self):
        self.log('off', self.off_throttle)
        self.adjust_motor(self.off_throttle)
        self.pi.stop()
        return


    def idle(self):
        self.log('idle', self.idle_throttle)
        self.adjust_motor(self.idle_throttle)
        return


    def clockwise(self):
        self.log('CW', self.clockwise_throttle)
        self.adjust_motor(self.clockwise_throttle)
        return


    def anticlock(self):
        self.log('ACW', self.anticlock_throttle)
        self.adjust_motor(self.anticlock_throttle)
        return

    
    def adjust_motor(self, rpm):
        self.pi.set_servo_pulsewidth(self.gpioPin, rpm)
        return
    
    def getState(self):
        return self.pi.get_servo_pulsewidth(self.gpioPin)


    def log(self, direction, rpm):
        print('{0} spinning {1} ({2})'.format(self.name, direction, rpm))
        return


    

#  ______             _            
# |  ____|           (_)           
# | |__   _ __   __ _ _ _ __   ___ 
# |  __| | '_ \ / _` | | '_ \ / _ \
# | |____| | | | (_| | | | | |  __/
# |______|_| |_|\__, |_|_| |_|\___|
#                __/ |             
#               |___/              
    
class Engine:
    # Assumes spinning motor in clockwise direction pushes ROVER forward
    
    def __init__(self):
        self.rightMotor = Motor('right', RIGHT_MOTOR_GPIO)
        self.leftMotor = Motor('left', LEFT_MOTOR_GPIO)
        self.propellorMotor = Motor('propellor', PROPELLOR_MOTOR_GPIO)
    
    
    def off(self):
        print('\tOFF')
        self.rightMotor.off()
        self.leftMotor.off()
        self.propellorMotor.off()
        return
    
    
    def idle(self):
        print('\tIDLE')
        self.rightMotor.idle()
        self.leftMotor.idle()
        self.propellorMotor.idle()
        return
        
        
    def forward(self):
        print('\tFORWARD')
        self.leftMotor.idle()
        self.rightMotor.idle()
        time.sleep(1.5)
        self.rightMotor.anticlock()
        self.leftMotor.anticlock()
        return
        
    
    def backward(self):
        print('\tBACKWARD')
        self.leftMotor.idle()
        self.rightMotor.idle()
        time.sleep(1.5)
        self.rightMotor.clockwise()
        self.leftMotor.clockwise()
        return
        
        
    def right(self):
        print('\tRIGHT')
        self.leftMotor.idle()
        self.rightMotor.idle()
        time.sleep(1.5)
        self.rightMotor.anticlock()
        self.leftMotor.clockwise()
        return
    
    
    def left(self):
        print('\tLEFT')
        self.leftMotor.idle()
        self.rightMotor.idle()
        time.sleep(1.5)
        self.rightMotor.clockwise()
        self.leftMotor.anticlock()
        return
    
    
    def up(self):
        print('\tUP')
        self.propellorMotor.idle()
        time.sleep(1.5)
        self.propellorMotor.clockwise()
        return
    
    
    def down(self):
        print('\tDOWN')
        self.propellorMotor.idle()
        time.sleep(1.5)
        self.propellorMotor.anticlock()
    
    
    def getDataAsDict(self):
        d = {
            "right" : self.rightMotor.getState(),
            "left" : self.leftMotor.getState(),
            "propellor" : self.propellorMotor.getState()
        }
        return d
    
    


#   _____                           
#  / ____|                          
# | (___   ___ _ __  ___  ___  _ __ 
#  \___ \ / _ \ '_ \/ __|/ _ \| '__|
#  ____) |  __/ | | \__ \ (_) | |   
# |_____/ \___|_| |_|___/\___/|_|

from Adafruit_BNO055 import BNO055

class Sensor:
    def __init__(self):
        self.sys = None
        self.gyro = None
        self.accel = None
        self.mag = None
        
        self.heading = None
        self.roll = None
        self.pitch = None
        self.temp_c = None
        
        self.bno = BNO055.BNO055(serial_port='/dev/ttyUSB0', rst=18) # apparently rst value is not needed
        
        if not self.bno.begin():
            raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')
            # Print system status and self test result.
        
        status, self_test, error = self.bno.get_system_status()
        print('System status: {0}'.format(status))
        print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
        
        # Print out an error if system status is in error mode.
        if status == 0x01:
            print('System error: {0}'.format(error))
            print('See datasheet section 4.3.59 for the meaning')
        print('Reading BNO055 data...')
        print('')
        self.readAll()
    
    
    def readAll(self):
        self.readOrientation();
        # Orientation as a quaternion:
        #x,y,z,w = bno.read_quaterion()
        
        self.readCalibration();
        self.readTemperature();
        
        # Magnetometer data (in micro-Teslas):
        #x,y,z = bno.read_magnetometer()
        
        # Gyroscope data (in degrees per second):
        #x,y,z = bno.read_gyroscope()
        
        # Accelerometer data (in meters per second squared):
        #x,y,z = bno.read_accelerometer()
        
        # Linear acceleration data (i.e. acceleration from movement, not gravity--
        # returned in meters per second squared):
        #x,y,z = bno.read_linear_acceleration()
        
        # Gravity acceleration data (i.e. acceleration just from gravity--returned
        # in meters per second squared):
        #x,y,z = bno.read_gravity()
        return
    
    
    def readOrientation(self):
        # Read the Euler angles for heading, roll, pitch (all in degrees).
        self.heading, self.roll, self.pitch = self.bno.read_euler()
        return
    
    
    def readCalibration(self):
        # Read the calibration status, 0=uncalibrated and 3=fully calibrated.
        self.sys, self.gyro, self.accel, self.mag = self.bno.get_calibration_status()
        return
    
    
    def readTemperature(self):
        # Sensor temperature in degrees Celsius:
        self.temp_c = self.bno.read_temp()
        return
    
    
    def updateGetHeading(self):
        self.readOrientation()
        return self.getHeading()
    
    
    def updateGetRoll(self):
        self.readOrientation()
        return self.getRoll()
    
    
    def updateGetPitch(self):
        self.readOrientation()
        return self.getPitch()
    
    
    def updateGetTemperature(self):
        self.readTemperature()
        return self.getTemperature()
    
    
    def displayData(self):
        print(self.getDataAsString())
        return
    
    
    def displayCalibration(self):
        print('Sys_cal={0} Gyro_cal={1} Accel_cal={2} Mag_cal={3}'.format(self.sys, self.gyro, self.accel, self.mag))
        return
    
    
    def getDataAsString(self):
        data = time.strftime("%H:%M:%S - %Y-%m-%d", time.gmtime())
        data += ('\nHeading={0:0.2f} Roll={1:0.2f} Pitch={2:0.2f}').format(self.heading, self.roll, self.pitch)
        data += '\nTemp_c={0}'.format(self.temp_c)
        return data
    
    
    def getDataAsDict(self):
        d = {
            "heading" : self.heading,
            "roll" : self.roll,
            "pitch" : self.pitch,
            "tempC" : self.temp_c
        }
        return d
    


#  _    _ _ _              _____             _      
# | |  | | | |            / ____|           (_)     
# | |  | | | |_ _ __ __ _| (___   ___  _ __  _  ___ 
# | |  | | | __| '__/ _` |\___ \ / _ \| '_ \| |/ __|
# | |__| | | |_| | | (_| |____) | (_) | | | | | (__ 
#  \____/|_|\__|_|  \__,_|_____/ \___/|_| |_|_|\___|

class UltraSonic:
    def __init__(self):
        SONIC_GPIO.setmode(SONIC_GPIO.BCM)
        #set GPIO direction (IN / OUT)
        SONIC_GPIO.setup(SONIC_GPIO_TRIGGER, SONIC_GPIO.OUT)
        SONIC_GPIO.setup(SONIC_GPIO_ECHO, SONIC_GPIO.IN)
        
    def distance(self):
        # set Trigger to HIGH
        SONIC_GPIO.output(SONIC_GPIO_TRIGGER, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        SONIC_GPIO.output(SONIC_GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while SONIC_GPIO.input(SONIC_GPIO_ECHO) == 0:
            StartTime = time.time()

        # save time of arrival
        while SONIC_GPIO.input(SONIC_GPIO_ECHO) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
        return distance
    
    def getDataAsDict(self):
        d = {
            "distance" : self.distance()
        }
        return d
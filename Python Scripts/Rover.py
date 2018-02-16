# Tags generated with -     http://patorjk.com/software/taag/#p=display&f=Big

import logging
import sys
import time



#  __  __       _             
# |  \/  |     | |            
# | \  / | ___ | |_ ___  _ __ 
# | |\/| |/ _ \| __/ _ \| '__|
# | |  | | (_) | || (_) | |   
# |_|  |_|\___/ \__\___/|_|   
                             
import os
os.system ("sudo pigpiod")
time.sleep(2)
import pigpio    
    
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
    
    def __init__(self, rightGPIO, leftGPIO):
        self.rightMotor = Motor('Right', rightGPIO)
        self.leftMotor = Motor('Left', leftGPIO)
    
    
    def off(self):
        print('\tOFF')
        self.rightMotor.off()
        self.leftMotor.off()
        return
    
    
    def idle(self):
        print('\tIDLE')
        self.rightMotor.idle()
        self.leftMotor.idle()
        return
        
        
    def forward(self):
        print('\tFORWARD')
        self.rightMotor.clockwise()
        self.leftMotor.clockwise()
        return
        
    
    def backward(self):
        print('\tBACKWARD')
        self.rightMotor.anticlock()
        self.leftMotor.anticlock()
        return
        
        
    def right(self):
        print('\tRIGHT')
        self.rightMotor.anticlock()
        self.leftMotor.clockwise()
        return
    
    
    def left(self):
        print('\tLEFT')
        self.rightMotor.clockwise()
        self.leftMotor.anticlock()
        return
    
    


#   _____                           
#  / ____|                          
# | (___   ___ _ __  ___  ___  _ __ 
#  \___ \ / _ \ '_ \/ __|/ _ \| '__|
#  ____) |  __/ | | \__ \ (_) | |   
# |_____/ \___|_| |_|___/\___/|_|

from Adafruit_BNO055 import BNO055

class Sensor:
    def __init__(self):
        self.bno = None
        self.heading = None
        self.roll = None
        self.pitch = None
        self.sys = None
        self.gyro = None
        self.accel = None
        self.mag = None
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
        self.readOrientationEuler();
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
    
    
    def readOrientationEuler(self):
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
    
    
    def getHeading(self):
        return self.heading
    
    
    def getRoll(self):
        return self.roll
    
    
    def getPitch(self):
        return self.pitch
    
    
    def getTemperature(self):
        return self.temp_c
    
    
    def getDataAsString(self):
        data = time.strftime("%H:%M:%S - %Y-%m-%d", time.gmtime())
        data += ('\nHeading={0:0.2f} Roll={1:0.2f} Pitch={2:0.2f}').format(self.heading, self.roll, self.pitch)
        data += '\nTemp_c={0}'.format(self.temp_c)
        return data
    
    def displayData(self):
        print(self.getData())
        return
    
    
    def displayCalibration(self):
        print('Sys_cal={0} Gyro_cal={1} Accel_cal={2} Mag_cal={3}'.format(self.sys, self.gyro, self.accel, self.mag))
        return
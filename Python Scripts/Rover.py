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
    
    def __init__(self, gpio):
        self.gpioPin = gpio
        self.pi = pigpio.pi()
        self.idle()

        
    def off(self, timer):
        print('OFF')
        self.log('off', self.off_throttle)
        self.adjust_motor(self.off_throttle)
        self.pi.stop()
        return


    def idle(self):
        self.log('idle', self.idle_throttle)
        self.adjust_motor(self.idle_throttle)
        return


    def right(self):
        print("RIGHT")
        self.log('right', self.clockwise_throttle)
        self.adjust_motor(self.clockwise_throttle)
        return


    def left(self):
        print("LEFT")
        self.log('left', self.anticlock_throttle)
        self.adjust_motor(self.anticlock_throttle)
        return


    def forward(self):
        print("FORWARD")
        self.log('forward', self.clockwise_throttle)
        self.adjust_motor(self.clockwise_throttle)
        return


    def backward(self):
        print("BACKWARD")
        self.log('backward', self.anticlock_throttle)
        self.adjust_motor(self.anticlock_throttle)
        return


    def adjust_motor(self, rpm):
        self.pi.set_servo_pulsewidth(self.gpioPin, rpm)
        return


    def log(self, direction, rpm):
        print(str(direction) + " with " + str(rpm))
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
    
    
    def readAll(self):
        self.readOrientation();
        self.readCalibration();
        self.readTemperature();
        # Other values you can optionally read:
        # Orientation as a quaternion:
        #x,y,z,w = bno.read_quaterion()
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
    
    
    def getHeading(self):
        return self.heading
    
    
    def getRoll(self):
        return self.roll
    
    
    def getPitch(self):
        return self.pitch
    
    
    def getTemperature(self):
        return self.temp_c
    
    
    def displayData(self):
        print(time.strftime("%H:%M:%S - %Y-%m-%d", time.gmtime()))
        print('Heading={0:0.2F} Roll={1:0.2F} Pitch={2:0.2F}'.format(self.heading, self.roll, self.pitch))
        print('Sys_cal={0} Gyro_cal={1} Accel_cal={2} Mag_cal={3}'.format(self.sys, self.gyro, self.accel, self.mag))
        print('Temp_c={0}'.format(self.temp_c))
        return
    
    
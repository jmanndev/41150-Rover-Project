import logging
import sys
import time

from Adafruit_BNO055 import BNO055

class Sensor:
    bno = ""
    heading = ""
    roll = ""
    pitch = ""
    sys = ""
    gyro = ""
    accel = ""
    mag = ""
    temp_c = ""

    def __init__(self):
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
    
    def readPhil(self):
        readOrientation();
        readCalibrationStatus();
        readTemperature();
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
    
    
    
    def displayPhilData(self):
        print('Heading={0:0.2F} Roll={1:0.2F} Pitch={2:0.2F}\tSys_cal={3} Gyro_cal={4} Accel_cal={5} Mag_cal={6}'.format(
            self.heading, self.roll, self.pitch, self.sys, self.gyro, self.accel, self.mag))
        return

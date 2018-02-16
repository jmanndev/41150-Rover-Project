import time
import Rover


RIGHT_MOTOR = 18
LEFT_MOTOR = 17

engine = Rover.Engine(RIGHT_MOTOR, LEFT_MOTOR)
phil = Rover.Sensor()
time.sleep(1)
engine.idle()


def setDirection():
    #change code here to determine direction
    engine.forward()
        

def run():
    print('  ~~~~\t~~~~\t~~~~\t') #makes output pretty :)
    while True:
        phil.readAll()
        setDirection()
        phil.displayData()
        time.sleep(1)
        print('  ~~~~\t~~~~\t~~~~\t') #makes output pretty :)
        
        
run()
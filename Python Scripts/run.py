import time
import Rover



RIGHT_MOTOR = 18
LEFT_MOTOR = 17

right = Rover.Motor('right', RIGHT_MOTOR)#test
left = Rover.Motor('left', LEFT_MOTOR)
phil = Rover.Sensor()

while True:
    phil.readAll()
    phil.displayData()
    right.idle()
    left.forward()
    time.sleep(2)
    print('\t~~~~\t~~~~\t~~~~\t') #makes output pretty :)
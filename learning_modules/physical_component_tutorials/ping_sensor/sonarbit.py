

""" Sonarbit Distance Program
Written by Brogan Pratt & Improvements made by u/mirusz9
"""

import time
import board
import digitalio
from math import floor

def sonar(pin, prev_distance = 570):
    ''' Get a ping reading from 5cm>568cm from the Elecfreaks Ping Sensor. Trigger & Echo are on the 'same pin'.
    pin = board.pin with the ping sensor attached
    prev_distance: accepts an int between 0>568. This sensor will output false 568 high readings if the object is <5cm to sensor.
        The default value is only given for the initial run, after this initial call you should input a previous distance
    returns: Distance in cm between 0 & 568
    '''

    usleep = lambda x: x/1000000

    pin.direction = digitalio.Direction.OUTPUT

    #send trigger signal
    pin.value = 0
    time.sleep(usleep(2))
    pin.value = 1
    time.sleep(usleep(10))
    pin.value = 0

    #recieve echo signal
    pin.direction = digitalio.Direction.INPUT
    original_time = time.monotonic_ns()

    while pin.value == 0:
        start_time = time.monotonic_ns()
        #this stops an infinite loop sometimes caused by rapid movements in front of the sensor. I am unsure of why
        #this happens, but this "safety check" breaks the infinite loop
        if (start_time - original_time > 50000000):
            break

    while pin.value == 1:
        end_time = time.monotonic_ns()

    #If an object is too close, start_time will never be assigned because pin.value will never equal 0, causing a variable assignment error & crash.
    try:
        # Distance is defined as time/2 (there and back) * speed of sound 34000 cm/s
        distance = floor((end_time - start_time) * 34000/2/1000000000)
    except:
        distance = 0

    #check if user has entered a previous distance
    if prev_distance == 570:
        pass
    else:
        #if our previous distance was close, and suddenly we register a VERY FAR object, we clearly are reading a false high 568cm, return the previously read value.
        if prev_distance < 15 and distance > 150:
            distance = prev_distance

    return distance

#init a prev_distance value for sonar func
prev_distance = 300
pin = digitalio.DigitalInOut(board.D2)
while True:
    distance = sonar(pin, prev_distance)
    print("the object is " + str(distance) + " cm away")
    prev_distance = distance



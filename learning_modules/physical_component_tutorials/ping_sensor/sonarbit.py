# sonarbit.py

"""
Sonarbit Distance Program Library
Original code by Brogan Pratt & Improvements by u/mirusz9
Converted to a library by [Your Name]
"""

import time
import digitalio
from math import floor

class Sonarbit:
    

    def __init__(self, pin_init):
        self.pin = pin_init
        self.d_sensor = digitalio.DigitalInOut(self.pin)

    def get_distance(self, prev_distance=570):
        ''' Get a ping reading from 5cm>568cm from the Elecfreaks Ping Sensor. Trigger & Echo are on the 'same pin'.
        prev_distance: accepts an int between 0>568. This sensor will output false 568 high readings if the object is <5cm to sensor.
        The default value is given for the initial run; after this initial call, you should input a previous distance.
        returns: Distance in cm between 0 & 568
        '''
        usleep = lambda x: x / 1000000
        self.d_sensor.direction = digitalio.Direction.OUTPUT
        
        # Send trigger signal
        self.d_sensor.value = False
        time.sleep(usleep(2))
        self.d_sensor.value = True
        time.sleep(usleep(10))
        self.d_sensor.value = False
        
        # Receive echo signal
        self.d_sensor.direction = digitalio.Direction.INPUT
        original_time = time.monotonic_ns()
        
        while not self.d_sensor.value:
            start_time = time.monotonic_ns()
            # This stops an infinite loop sometimes caused by rapid movements in front of the sensor.
            if (start_time - original_time > 50000000):
                break
        
        while self.d_sensor.value:
            end_time = time.monotonic_ns()
        
        # If an object is too close, start_time will never be assigned because pin.value will never be False, causing a variable assignment error & crash.
        try:
            # Distance is defined as time/2 (there and back) * speed of sound 34000 cm/s
            distance = floor((end_time - start_time) * 34000 / 2 / 1000000000)
        except:
            distance = 0
        
        # Check if user has entered a previous distance
        if prev_distance != 570:
            # If our previous distance was close, and suddenly we register a VERY FAR object, we clearly are reading a false high 568cm, return the previously read value.
            if prev_distance < 15 and distance > 150:
                distance = prev_distance
        
        return distance
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Analog In example"""
import time
import board
from analogio import AnalogIn
from math import *
from adafruit_simplemath import map_range

analog_in = AnalogIn(board.A1)

new_min = 0
new_max = 100

def get_voltage(pin):
    #maps our current 0>65536 along sensor to sometime more useful, like 0>100
    return map_range(pin.value, 0, 65536, new_min, new_max)

    #If we want to get a round number instead of a floating decimal, we could use "floor" to "floor" or bring down, any floating decimal number. 
    #uncomment the next line, and comment out the above return value
    #return floor(map_range(pin.value, 0, 65536, new_min, new_max))


while True:
    print(get_voltage(analog_in))
    time.sleep(0.1)

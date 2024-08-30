# Sonarbit_class Example
# SPDX-FileCopyrightText: 2024 Brogan Pratt
#
# SPDX-License-Identifier: MIT

import board
from sonarbit import Sonarbit
import time

pin = board.D2
distance_sensor = Sonarbit(pin)

prev_distance = 570  # Initial value

while True:
    distance = distance_sensor.get_distance(prev_distance)
    print("The object is: " + distance +  " cm away")
    prev_distance = distance
    time.sleep(1)
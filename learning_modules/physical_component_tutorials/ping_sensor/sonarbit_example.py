# Sonarbit_class Example
# SPDX-FileCopyrightText: 2024 Brogan Pratt
#
# SPDX-License-Identifier: MIT

import board
from sonarbit import Sonarbit
import time

distance_sensor = Sonarbit(board.D2)

prev_distance= 570  # Initial value

while True:
    distance = distance_sensor.get_distance(prev_distance)
    print("The object is: " + str(distance) +  " cm away")

    prev_distance = distance
    time.sleep(1)

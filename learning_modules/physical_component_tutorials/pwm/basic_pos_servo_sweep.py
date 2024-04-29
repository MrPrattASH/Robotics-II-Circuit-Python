# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo sweep example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin D2
pwm = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
pos_servo = servo.Servo(pwm)

#set Servo to starting position prior to main loop
pos_servo.angle = 0
time.sleep(1)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        pos_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        pos_servo.angle = angle
        time.sleep(0.05)

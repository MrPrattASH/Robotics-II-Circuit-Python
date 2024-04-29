# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT
# Slightly modified by Brogan Pratt for HS Robotics II

"""CircuitPython Essentials Servo standard servo sweep example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin D3 (notice no duty cycle)
pwm = pwmio.PWMOut(board.D3, frequency=50)

# Create a servo object, rot_servo.
rot_servo = servo.ContinuousServo(pwm)

while True:
    print("forward")
    rot_servo.throttle = 1.0
    time.sleep(2.0)
    print("stop")
    rot_servo.throttle = 0.0
    time.sleep(2.0)
    print("reverse")
    rot_servo.throttle = -1.0
    time.sleep(2.0)
    print("stop")
    rot_servo.throttle = 0.0
    time.sleep(2.0)

# SPDX-FileCopyrightText: 2024 Brogan Pratt
#
# SPDX-License-Identifier: MIT

"""ervo continuous rotation calibration example"""
import time
import board
import pwmio
from adafruit_motor import servo

# ----------------- INIT DEVICES -------------------------

# create a PWMOut object on Pin D0.
pwm = pwmio.PWMOut(board.D0, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.ContinuousServo(pwm)

# watch your serial port to see what value causes the servo to stop. 
# note this stop value for each specific motor
while True:
    
    print("starting calibration test")
    i = -3.0
    while i <= 3.0:
        print("Servo Throttle: ", str(i))
        my_servo.throttle = i
        time.sleep(2)
    print("Calibration completed\nRestarting...")
    time.sleep(2)
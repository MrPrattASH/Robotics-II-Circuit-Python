# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo sweep example"""
import time
import board
import pwmio
import pulseio
from adafruit_motor import servo

#p2 is S2
#p3 is S1
#P7 is pos servo

servo = pwmio.PWMOut(board.D7, frequency=50)

def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

min = 1.250
max = 1.750
stop = 1.500

while True:
    servo.duty_cycle = servo_duty_cycle(max)
    print(max)
    time.sleep(2)

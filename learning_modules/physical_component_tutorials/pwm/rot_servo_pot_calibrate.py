# Calibrate rot_servo using a pot sensor as input


import time
import board
import pwmio
from analogio import AnalogIn
from adafruit_motor import servo
from adafruit_simplemath import map_range

# create const rotation servo object
pwm = pwmio.PWMOut(board.D3, frequency=50)
rot_servo = servo.ContinuousServo(pwm)

#create pot sensor object
pot = AnalogIn(board.A1)
rot_min = -1.0
rot_max = 1.0

def get__mapped_analog_voltage(pin, min, max):
    #gets current voltage at an analog pin, returns a mapped value
    # pin - Analog pin number
    # min - new mapped min value
    # max - new mapped max value
    return map_range(pin.value, 0, 65535, min, max)

while True:
    volt_mapped = get__mapped_analog_voltage(pot, rot_min, rot_max)
    print(volt_mapped)
    rot_servo.throttle = volt_mapped

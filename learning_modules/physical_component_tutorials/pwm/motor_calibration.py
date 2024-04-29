'''Motor calibration
Use the following code to callibrate motors on roboclaw to within a 5us accuracy. 

Pin Diagram: 
D0 > S1/M1 on Roboclaw
D1 > S2/M2 on Roboclaw

Roboclaw:
Running Mode 1, Opt 4 for tank style driving (non-differential)
S1 = M1 direction/speed
S2 = M2 direction/speed

MCU mode is enabled, so the RC will not auto-calibrate itself to a centre point on an RC controller initially, instead, it uses to following servo pulses:
Theoretically, in a world of infinite torque...
Min: 1120us
Stop: 1520us
Max: 1920us

'''

import time
import board
import digitalio
import pwmio
import neopixel
from math import floor
from adafruit_simplemath import map_range

rc_m1 = pwmio.PWMOut(board.D0, frequency=50)
rc_m2 = pwmio.PWMOut(board.D1, frequency=50)

def ms_duty_cycle_convert(pulse_ms, frequency=50):
    '''converts a millisecond pulse command into a duty cycle value (0>65535) that circuitpython understands
    pulse_ms = a value in ms. In this case, us are desired, so 1520us = 1.520ms
    frequency = 50, the default argument we want to send servo pulses in. In the roboclaw and standard servo case, this is 50Hz. 

    returns converted ms > duty_cycle value between 0>65535 that circuitpy understands, and outputs as a PWM 
    '''

    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

def stop_motors():
    '''stops both motors'''
    stop = 1.52
    rc_m1.duty_cycle = ms_duty_cycle_convert(stop)
    rc_m2.duty_cycle = ms_duty_cycle_convert(stop)

def motor_calibrate_forward(pin):
    print('starting forward test' + str(pin))
    for i in range(0,400,5):
        pin.duty_cycle = ms_duty_cycle_convert(map_range(i,0,400,1.52,1.92))
        #print i + 1520 to show actual value being parsed
        print('current motor ms command = ' + (i+1520))
        time.sleep(1.5)
    #stop motor
    pin.duty_cycle = ms_duty_cycle_convert(1.52)
    print("test end")

def motor_calibrate_backward(pin):
    print('starting backward test' + str(pin))
    for i in range(400,0,-5):
        pin.duty_cycle = ms_duty_cycle_convert(map_range(i,400,0,1.52,1.12))
        #print i + 1520 to show actual value being parsed
        print('current motor ms command = ' + (i+1120))
        time.sleep(1.5)
    #stop motor
    pin.duty_cycle = ms_duty_cycle_convert(1.52)
    print("test end")

while True:
    #while tests are running, view your serial port and write down what values the motors begin turning at. This will be different for every motor.
    # for example, m1 may start at 1680, where as m2 may start at 1720. This can later be used to map different start/end values for each motor.  
    motor_calibrate_forward(rc_m1)
    motor_calibrate_forward(rc_m2)
    motor_calibrate_backward(rc_m1)
    motor_calibrate_backward(rc_m2)
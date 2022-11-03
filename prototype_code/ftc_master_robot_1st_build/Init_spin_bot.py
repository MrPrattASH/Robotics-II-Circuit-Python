""" This code is for after the initial GoBuilda FTC Kit Build test:

The robot has basic functions for:
forward
backwards
left/right
90*, 180*, 360*

Lift arm up, down

RoboClaw is programmed:
Button mode 1 (RC)
Option 4 (Tank Style) - intended state to run this program
"""

import time
import board
import pwmio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_motor import servo
from adafruit_simplemath import map_range
from math import floor
import rc
from arcade_drive import servo_duty_cycle, arcade_drive

# init DC motors as pwm objects
motor1 = pwmio.PWMOut(board.D0, frequency=50)
motor2 = pwmio.PWMOut(board.D1, frequency=50)

# init lift arm D2
pwm = pwmio.PWMOut(board.D2, frequency=50)
main_arm = servo.ContinuousServo(pwm)
# + is down, - is Up

# init Gripper arms
# d3 left
# d4 right
pwm1 = pwmio.PWMOut(board.D3, frequency=50)
left_servo = servo.Servo(pwm1)
pwm2 = pwmio.PWMOut(board.D4, frequency=50)
right_servo = servo.Servo(pwm2)

# motor speed commands
stop = 1.520
full_forward = 1.920  # +400us (microseconds)
full_reverse = 1.120  # -400us (microseconds)

# init RC Controller
# R joystick LR
ch1 = DigitalInOut(board.D5)
ch1.direction = Direction.INPUT
ch1.pull = Pull.DOWN

# R joystick UD
ch2 = DigitalInOut(board.D6)
ch2.direction = Direction.INPUT
ch2.pull = Pull.DOWN

# SwB 2 way toggle
ch5 = DigitalInOut(board.D7)
ch5.direction = Direction.INPUT
ch5.pull = Pull.DOWN

# SwC 3 way toggle
ch6 = DigitalInOut(board.D8)
ch6.direction = Direction.INPUT
ch6.pull = Pull.DOWN

def arm_up():
    main_arm.throttle = -1


def arm_down():
    main_arm.throttle = 1


def arm_stop():
    main_arm.throttle = 0


def claw_open():
    left_servo.angle = 118
    right_servo.angle = 0


def claw_close():
    left_servo.angle = 0
    right_servo.angle = 118

#moving average lists
x_moving = [0,0]
y_moving = [0,0]
#actual output to motors
x_out = 0
y_out = 0

while True:
    # Get RC Readings
    sw_c = rc.read_3way_switch(ch6)
    sw_b = rc.read_2way_switch(ch5)
    y_joy = rc.read_analog(ch2, -1.361, 1.302)
    x_joy = rc.read_analog(ch1, -1.361, 1.302)
    #update
    rc.upd_mov_avg(x_moving, x_joy)
    rc.upd_mov_avg(y_moving, y_joy)

    if rc.all_equal(x_moving):
        x_out = x_moving[0]
    if rc.all_equal(y_moving):
        y_out = y_moving[0]


    print("b" + str(sw_b) + "c" + str(sw_c) + " x " + str(x_joy) + " y " + str(y_joy))

    # control grabber arm - 2 way toggle switch
    if sw_b == 1:
        claw_open()
    else:
        claw_close()

    # control lift arm - 3way toggle switch
    if sw_c == 0:
        arm_stop()
    elif sw_c == 1:
        arm_down()
    else:
        arm_up()

    #drive motors
    arcade_drive(x_out, y_out, motor1, motor2)

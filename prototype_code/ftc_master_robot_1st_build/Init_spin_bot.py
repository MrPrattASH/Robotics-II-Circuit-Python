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

# init DC motors as pwm objects
motor1 = pwmio.PWMOut(board.D2, frequency=50)
motor2 = pwmio.PWMOut(board.D3, frequency=50)

# init lift arm
pwm = pwmio.PWMOut(board.D4, frequency=50)
main_arm = servo.ContinuousServo(pwm)
# + is down, - is Up

# init Gripper arms
# d5 left
# d6 right
pwm1 = pwmio.PWMOut(board.D5, frequency=50)
left_servo = servo.Servo(pwm1)
pwm2 = pwmio.PWMOut(board.D6, frequency=50)
right_servo = servo.Servo(pwm2)

# init BUTTONS
# D7 Yellow
# D8 Red
red_button = DigitalInOut(board.D8)
yellow_button = DigitalInOut(board.D7)
red_button.direction = Direction.INPUT
yellow_button.direction = Direction.INPUT
red_button.pull = Pull.UP
yellow_button.pull = Pull.UP

red_cur_state = False
red_prev_state = False
yellow_cur_state = False
yellow_prev_state = False


#motor speed commands
stop = 1.520
full_forward = 1.920 #+400us (microseconds)
full_reverse = 1.120 #-400us (microseconds)

def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

def forward(speed):
    '''moves robot forward at a specific speed
    speed: int  between 0 - 100
    '''
    global full_forward, stop
    #speed = int between 0-100
    max_speed = full_forward
    min_speed = stop + 0.01
    map_speed = map_range(speed, 0, 100, min_speed, max_speed)
    motor1.duty_cycle = servo_duty_cycle(map_speed)
    motor2.duty_cycle = servo_duty_cycle(map_speed)

def reverse(speed):
    '''moves robot reverse at a specific speed
    speed: int  between 0 - 100
    '''
    global full_reverse, stop
    max_speed = full_reverse
    min_speed = stop - 0.01
    map_speed = map_range(speed, 0, 100, min_speed, max_speed)
    motor1.duty_cycle = servo_duty_cycle(map_speed)
    motor2.duty_cycle = servo_duty_cycle(map_speed)

def stop():
    motor1.duty_cycle = servo_duty_cycle(1.5)
    motor2.duty_cycle = servo_duty_cycle(1.5)

def arm_full_up():
    main_arm.throttle = -1
    time.sleep(12.2)
    main_arm.throttle = 0

def arm_full_down():
    main_arm.throttle = 1
    time.sleep(12.2)
    main_arm.throttle = 0

def grab():
    pass

while True:
    # button logic
    yellow_cur_state = yellow_button.value
    red_cur_state = red_button.value

    if yellow_cur_state != yellow_prev_state:
        if not yellow_cur_state: #button is down
            print("forward")
            forward(50)
            time.sleep(2)
            stop()

    if red_cur_state != red_prev_state:
        if not red_cur_state: #button is down
            print("backward")
            backward(50)
            time.sleep(2)
            stop()

    yellow_prev_state = yellow_cur_state
    red_prev_state = red_cur_state



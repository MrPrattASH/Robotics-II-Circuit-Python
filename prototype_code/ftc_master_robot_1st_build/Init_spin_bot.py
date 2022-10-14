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

# init lift arm D4
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
# D1 Yellow
# D8 Red
red_button = DigitalInOut(board.D8)
yellow_button = DigitalInOut(board.D1)
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
    motor1.duty_cycle = servo_duty_cycle(1.52)
    motor2.duty_cycle = servo_duty_cycle(1.52)

def arm_full_up():
    main_arm.throttle = -1
    time.sleep(12.2)
    main_arm.throttle = 0

def arm_full_down():
    main_arm.throttle = 1
    time.sleep(12.2)
    main_arm.throttle = 0

def grab():
    #R servo, 145 @ rest
    #R servo, 30 @ grab
    #L servo, 145 @ rest
    #L servo, 5 @ rest
    pass

#init grabber arms to centre
left_servo.angle = 0
right_servo.angle = 0

angle = 0

while True:
    #get button inputs, True if unpresed, False if Pressed
    yellow_cur_state = yellow_button.value
    red_cur_state = red_button.value
    print(yellow_cur_state)

    #Drive forward 4s, move arm full up
    if yellow_cur_state != yellow_prev_state:
        if yellow_cur_state: #button is down
            '''forward(75)
            time.sleep(4)
            stop()
            arm_full_up()'''
            angle+=5

    if red_cur_state != red_prev_state:
        if not red_cur_state: #button is down
            '''grab()
            arm_full_down()
            reverse(75)'''
            angle-=5

    left_servo.angle = angle
    right_servo.angle = angle
    print("angle" + str(angle))
    yellow_prev_state = yellow_cur_state
    red_prev_state = red_cur_state



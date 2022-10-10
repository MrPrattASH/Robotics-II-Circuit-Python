import time
import board
import pwmio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_motor import servo

"""
Button mode 1 (RC)
Option 4 (Tank Style) - intended state to run this program
Option 5 (Differential Steering Style)
"""

# init DC motors as pwm objects
motor1 = pwmio.PWMOut(board.D2, frequency=50)
motor2 = pwmio.PWMOut(board.D3, frequency=50)

# init servo main arm up/down control
pwm = pwmio.PWMOut(board.D4, frequency=50)
main_arm = servo.ContinuousServo(pwm)
# + is down, - is Up
# 8sec to top of arm, 7 sec down

# servo gripper arms
# d5 left
# d6 right
pwm1 = pwmio.PWMOut(board.D5, frequency=50)
left_servo = servo.Servo(pwm1)
pwm2 = pwmio.PWMOut(board.D6, frequency=50)
right_servo = servo.Servo(pwm2)

# buttons
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


def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle


# Define Min/Max/Stop commands
min_speed = 1.0  # full forward
max_speed = 2.0  # full backward
stop = 1.5  # needs to be calibrated by motor.


def motor_test():
    SLEEP_DURATION = 2
    # Main motor move forward, stop, backwards, stop
    motor1.duty_cycle = servo_duty_cycle(min_speed)
    motor2.duty_cycle = servo_duty_cycle(min_speed)
    print("Full forward")
    time.sleep(SLEEP_DURATION)

    motor1.duty_cycle = servo_duty_cycle(stop)
    motor2.duty_cycle = servo_duty_cycle(stop)
    print("stop")
    time.sleep(SLEEP_DURATION)

    motor1.duty_cycle = servo_duty_cycle(max_speed)
    motor2.duty_cycle = servo_duty_cycle(max_speed)
    print("Full backward")
    time.sleep(SLEEP_DURATION)

    motor1.duty_cycle = servo_duty_cycle(stop)
    motor2.duty_cycle = servo_duty_cycle(stop)
    print("stop")


def arm_full_up(cur_time, start_time):
    goal_time = 12.2
    if not cur_time >= start_time + goal_time:
        main_arm.throttle = -1
        return True
    else:
        main_arm.throttle = 0
        return False


def arm_full_return(cur_time, start_time):
    goal_time = 12.2
    if not cur_time >= start_time + goal_time:
        main_arm.throttle = 1
        return True
    else:
        main_arm.throttle = 0
        return False


def grab():
    pass

arm_up = False
arm_up_goal_time = 12.2

while True:
    now = time.monotonic()
    # button logic
    yellow_cur_state = yellow_button.value
    red_cur_state = red_button.value

    if yellow_cur_state != yellow_prev_state:
        #push button, begin start time, start arm up
        if not yellow_cur_state: #button is down
            if not arm_full_up


    if red_cur_state != red_prev_state:
        if not red_cur_state:
            red_start_time = now

    yellow_prev_state = yellow_cur_state
    red_prev_state = red_cur_state

    #move movement arm
    arm_full_up(now, yellow_start_time)



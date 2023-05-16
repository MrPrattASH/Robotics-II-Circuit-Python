import board
from digitalio import DigitalInOut, Direction, Pull
import time
import pwmio
from adafruit_motor import servo

#on/off button
button = DigitalInOut(board.D0)
button.direction = Direction.INPUT
button.pull = Pull.UP

#setup servos
# Create a rotational servo object, my_servo.
pwm1 = pwmio.PWMOut(board.D1, duty_cycle=2 ** 15, frequency=50)
left_servo = servo.ContinuousServo(pwm1)

pwm2 = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50)
mid_servo = servo.ContinuousServo(pwm2)

pwm3 = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=50)
right_servo = servo.ContinuousServo(pwm3)

#init variables
cur_button_state = False
prev_button_state = False
run_motors = False
timer_length = 3.000
timer_started = False
start_time = 0.0
winch_up = True
winches_on = False

while True:
    #get current reading
    cur_button_state = button.value
    now = time.monotonic()

    #toggle button
    if cur_button_state != prev_button_state:
        if cur_button_state and not winches_on:
            winches_on = True
            print("motors running")
        elif cur_button_state and winches_on:
            winches_on = False
            print("motors stopped")

    #on and off motor function
    if winches_on:
        #start the timer for the winch
        if not timer_started:
            start_time = now
            timer_started = True

        #has our timer elapsed?
        if now >= start_time + timer_length:
            timer_started = False
            if winch_up:
                winch_up = False
            else:
                winch_up = True

        #drive the winch
        if winch_up:
            left_servo.throttle = 1.0
            mid_servo.throttle = 1.0
            right_servo.throttle = 1.0
        else:
            left_servo.throttle = -1.0
            mid_servo.throttle = -1.0
            right_servo.throttle = -1.0

    #stop the motors
    else:
        left_servo.throttle = 0
        mid_servo.throttle = 0
        right_servo.throttle = 0
        timer_started = False




    #setup check
    prev_button_state = cur_button_state
    time.sleep(0.01)

''' 
1. Setup our RC controller
2. setup our DC motor controllers
3. create a helper function that converts ms to duty cycle pulses
4. create a helper function that normalizes the joystick input
5. create a drive function that takes our normalized inputs and outputs mecanum drive motor commands
'''

import time
import board
from rc import RC
import pwmio

# create the rc object
rc = RC(ch1=board.D10, ch2=board.D11, ch3=None, ch4=board.D9, ch5=None, ch6=None)

# ---------------    DC motor controller setup ----------------

m_fl = pwmio.PWMOut(board.D0, frequency=50)
m_fr = pwmio.PWMOut(board.D1, frequency=50)
m_rl = pwmio.PWMOut(board.D2, frequency=50)
m_rr = pwmio.PWMOut(board.D3, frequency=50)

stop_ms = 1.5
max_ms = 1.9
min_ms = 1.1
# 400ms range +/- to control max power of motors

def ms_to_duty_cycle(ms, freq=50):
    period_ms = 1.0/ freq * 1000
    duty_cycle = int(ms / (period_ms/ 65535.0))
    return min(65535, max(0, duty_cycle)) # clamps the duty cycle to 0-65535

def stop_all_motors():
    m_fl.duty_cycle = ms_to_duty_cycle(stop_ms)
    m_fr.duty_cycle = ms_to_duty_cycle(stop_ms)
    m_rl.duty_cycle = ms_to_duty_cycle(stop_ms)
    m_rr.duty_cycle = ms_to_duty_cycle(stop_ms)

# ---------------    Joystick input normalization ----------------

# expects a range of 0-100 from the joystick
# mecanum kinematics expects -1.0-1.0

def normalize_input(value):
    deadzone_min = 45
    deadzone_max = 55

    if value == None:
        return 0.0
    
    if deadzone_min <= value <= deadzone_max:
        return 0.0
    elif value < deadzone_min:
        return (value - deadzone_min) / (deadzone_min)
    elif value > deadzone_max:
        return (value - deadzone_max) / (100 - deadzone_max)

def drive(throttle_sp, strafe_sp, rotate_sp, input_scale(0.5)):
    fwd = normalize_input(throttle_sp)
    strafe = normalize_input(strafe_sp)
    rotate = normalize_input(rotate_sp)

    if fwd == 0 and strafe == 0 and rotate == 0:
        stop_all_motors()
        return

    fwd = fwd * input_scale
    strafe = strafe * input_scale
    rotate = rotate * input_scale

    # mecanum kinematics
    m_fl_pwr = fwd + strafe + rotate
    m_fr_pwr = fwd - strafe - rotate
    m_rl_pwr = fwd - strafe + rotate
    m_rr_pwr = fwd + strafe - rotate

    max_power = max(abs(m_fl_pwer), abs(m_fr_pwr), abs(m_rl_pwr), abs(m_rr_pwr))
    if max_power > 1.0:
        m_fl_pwr /= max_power
        m_fr_pwr /= max_power
        m_rl_pwr /= max_power
        m_rr_pwr /= max_power

    # move the motors (and convert to ms)
    m_fl.duty_cycle = stop_ms + m_fl_pwr * .4
    m_fr.duty_cycle = stop_ms + m_fr_pwr * .4
    m_rl.duty_cycle = stop_ms + m_rl_pwr * .4
    m_rr.duty_cycle = stop_ms + m_rr_pwr * .4


while True:
    throttle = rc.read_channel(1)
    strafe = rc.read_channel(2)
    rotate = rc.read_channel(4)

    drive(throttle, strafe, rotate)

    time.sleep(0.02) # keeps us in cycle with PWM of the rc controller
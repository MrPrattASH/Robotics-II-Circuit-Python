"""Basic RC Library import
Provides functions for:
- converting arbitrary -1 > 1 signal to ms output
- outputting to roboclaw motorcontroller via arcade-style drive
"""


import time
from math import floor
from adafruit_simplemath import map_range

def servo_duty_cycle(pulse_ms, frequency=50):
    ''' 
    Converts a ms_pulse length into a duty cycle value

    :pulse_ms: float: 
    
    '''
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

def arcade_drive(rotate, drive, left_motor, right_motor):
    """Drives the robot using arcade drive."""
    # variables to determine the quadrants

    maximum = max(abs(drive), abs(rotate))
    total, difference = drive + rotate, drive - rotate
    # print("max " + str(maximum) + " total " + str(total) + " dif " + str(difference))

    # set speed according to the quadrant that the values are in
    # proper servo motor values are sent from get_analog_ch func
    if drive >= 0:
        if rotate >= 0:  # I quadrant FWD + Right
            left = arbitrary_scale_to_ms(maximum)
            right = arbitrary_scale_to_ms(difference)
        else:  # II quadrant FWD + Left
            left = arbitrary_scale_to_ms(total)
            right = arbitrary_scale_to_ms(maximum)
    else:
        if rotate >= 0:  # IV quadrant REV + Left
            left = arbitrary_scale_to_ms(total)
            right = arbitrary_scale_to_ms(-maximum)
        else:  # III quadrant REV + Right
            left = arbitrary_scale_to_ms(-maximum)
            right = arbitrary_scale_to_ms(difference)
    left = round(left, 3)
    right = round(right, 3)
    left_motor.duty_cycle = servo_duty_cycle(left)
    right_motor.duty_cycle = servo_duty_cycle(right)

def arbitrary_scale_to_ms(val):
    #convert an arbitrary number scale -1 > 1 into PWM ms outputs
    #stop value
    if val == 0:
        return 1.520
    # fwd
    elif val > 0:
        return map_range(val, 0, 1, 1.520, 1.920)
    #rev
    else:
        return map_range(val,0, -1, 1.520, 1.120)
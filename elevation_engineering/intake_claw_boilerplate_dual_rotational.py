# ROTATIONAL SERVO BOILER PLATE

import time
import board
from rc import RCReceiver
from arcade_drive_dc import Drive
import pwmio
from adafruit_motor import servo

rc = RCReceiver(ch1=board.D10, ch2=board.D11, ch3=None, ch4=None, ch5=board.D12, ch6=board.D13)
drive = Drive(left=board.D0, right=board.D1)

# Create a positional servo object, my_pos_servo.
pwm0 = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50)
intake_servo = servo.ContinuousServo(pwm0)

pwm1 = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=50)
intake_servo2 = servo.ContinuousServo(pwm1)

# Main code
while True:
    # Read joystick channels
    spin = rc.read_channel(1) # spin
    throttle = rc.read_channel(2) # throttle
    ch6 = rc.read_channel(6)

    if spin is not None and throttle is not None: # must not be None to do something with the output
        drive.drive(spin,throttle) # move our motors arcade drive style

    if ch6 is not None: # valid reading from switch
        if ch6 == 0:  # switch down
            intake_servo.throttle = 0.8  # TODO: Calibrate this speed + direction
            intake_servo2.throttle = -0.8
        elif ch6 == 1: # switch mid point
            intake_servo.throttle = 0 
            intake_servo2.throttle = 0
        else:  # switch up
            intake_servo.throttle = -0.8  # TODO: Calibrate this speed + direction
            intake_servo2.throttle = 0.8
            


    time.sleep(0.02) # keep timer in sync with flysky receiver

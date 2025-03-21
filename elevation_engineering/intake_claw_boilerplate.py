# POSITIONAL SERVO BOILER PLATE

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
intake_servo = servo.Servo(pwm0)

# Main code
while True:
    # Read joystick channels
    spin = rc.read_channel(1) # spin
    throttle = rc.read_channel(2) # throttle
    ch5 = rc.read_channel(5)

    if spin is not None and throttle is not None: # must not be None to do something with the output
        drive.drive(spin,throttle) # move our motors arcade drive style

    if ch5 is not None:
        if ch5 == 1:  # switch up
            intake_servo.angle = 90  # TODO: Calibrate this angle
        else:  # switch down
            intake_servo.angle = 5  # TODO: Calibrate this angle


    time.sleep(0.02) # keep timer in sync with flysky receiver

# ROTATIONAL SERVO BOILER PLATE

import time
import board
import pwmio
from rc import RCReceiver
from arcade_drive_dc import Drive
import pwmio
from adafruit_motor import servo

rc = RCReceiver(ch1=board.D10, ch2=board.D11, ch3=board.D9, ch4=None, ch5=board.D12, ch6=board.D13)
drive = Drive(left=board.D0, right=board.D1)

# ---------------- SERVO OBJECTS ----------------
# Create a positional servo object, intake_servo
pwm0 = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50)
intake_servo = servo.ContinuousServo(pwm0)

pwm1 = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=50)
intake_servo2 = servo.ContinuousServo(pwm1)

# Create a servo object for your lift arm, but with a different pin & variable name
pwm2 = pwmio.PWMOut(board.D4, duty_cycle=2 ** 15, frequency=50)
lift_arm_servo = servo.ContinuousServo(pwm2)

# Do the same again, but for your extension mechanism, again with a different pin & variable name
pwm3 = pwmio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=50)
extension_mech_servo = servo.ContinuousServo(pwm3)

# Main code
while True:
    # Read joystick channels
    spin = rc.read_channel(1) # spin
    throttle = rc.read_channel(2) # throttle
    lift_arm = rc.read_channel(3) # lift arm
    ch5_pot = rc.read_channel(5, ch5_mode="pot") # VRA pot dial
    ch6 = rc.read_channel(6) # intake servo 3way switch

    # Arcade Drive
    if spin is not None and throttle is not None: # must not be None to do something with the output
        drive.drive(spin,throttle) # move our motors arcade drive style

    # Lift Arm (Left stick Up/down
    if lift_arm is not None:
        if lift_arm == 50:  # Left stick centered
            lift_arm_servo.throttle = 0  # TODO: Calibrate this speed + direction
        elif lift_arm > 60:  # Left stick up
            lift_arm_servo.throttle = 0.5 # TODO: Calibrate this speed + direction
        elif lift_arm < 40:  # Left stick down
            lift_arm_servo.throttle = -0.5 # TODO: Calibrate this speed + direction

    # Extension Mechanism (VRA pot)
    if ch5_pot is not None:
        if ch5_pot == 0:  # pot centered
            extension_mech_servo.throttle = 0  # TODO: Calibrate this speed + direction
        elif ch5_pot == 1:  # pot turned up
            extension_mech_servo.throttle = 0.5 # TODO: Calibrate this speed + direction
        elif ch5_pot == 2:  # pot turned down
            extension_mech_servo.throttle = -0.5 # TODO: Calibrate this speed + direction
    
    # Intake Mechanism (right side 3-way switch)
    if ch6 is not None:
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

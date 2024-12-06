'''
Boiler plate code for Intake Mechanism

PINOUT:
D0 - Servo
D1 - Open Claw button
D2 - Close Claw button

'''

# ------------- LIBRARIES -----------------

from time import sleep
import board
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull

# ------------- INIT SERVO -----------------

# Create a positional servo object, claw_servo.
pwm = pwmio.PWMOut(board.D0, duty_cycle=2 ** 15, frequency=50)
claw_servo = servo.Servo(pwm)

# ------------- INIT BUTTONS -----------------

button_open = DigitalInOut(board.D1)  # create button instance
button_open.direction = Direction.INPUT  # set as an INPUT sensor
button_open.pull = Pull.UP   # Pull up to always read 3.3v unless pressed

button_close = DigitalInOut(board.D2)
button_close.direction = Direction.INPUT
button_close.pull = Pull.UP

# ------------- MAIN LOOP -----------------

print("Starting Loop")
sleep(1)

while True:
    # read button sensors, and store values in variables
    open_claw = button_open.value
    close_claw = button_close.value

    # if our buttons are pressed, actuate servo the correct direction
    if not open_claw:  # open button pressed
        print("open pressed! opening claw")
        claw_servo.angle = 0  # TODO - CALIBRATE

    elif not close_claw: # close button pressed
        print("close pressed! closing claw")
        claw_servo.angle = 90  # TODO - CALIBRATE

    sleep(.2)  # add a minor sleep to prevent button debounces


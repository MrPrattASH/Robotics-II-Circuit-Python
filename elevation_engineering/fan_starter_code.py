import board
from digitalio import DigitalInOut, Direction, Pull
import time
import pwmio
from adafruit_motor import servo

# ----------------- INIT DEVICES -------------------------

led = DigitalInOut(board.D0)
led.direction = Direction.INPUT

switch = DigitalInOut(board.D3)
switch.direction = Direction.INPUT  # input for sensors
switch.pull = Pull.UP   # Pull.Up/Down is used for switches

# create a PWMOut object on Pin D0.
pwm = pwmio.PWMOut(board.D6, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.ContinuousServo(pwm)

while True:
    button1 = switch.value
    # add your 2nd button reading
    if not button1:  
        print("Pressed button 1!")
        # add your servo control
        my_servo.throttle = 0.33
        led.value = True
        # turn off your other LED
    # add your 2nd button condition, servo control, and 2nd LED logic, and repeat for all x4 buttons

    time.sleep(0.01)  # add a small sleep to prevent overrunning loops
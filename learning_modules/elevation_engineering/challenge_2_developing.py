''' 

DEVELOPING LEVEL PROGRAM

'''

# import Libraries
import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
from adafruit_motor import servo
import time

# ------------ BUTTONS INIT ---------------
up_button = DigitalInOut(board.D5)
up_button.direction = Direction.INPUT # input for sensors
up_button.pull = Pull.UP   # Pull.Up/Down is used for switches

# repeat x5 for your other buttons

# --------------- SERVOS INIT -------------
# Create a positional servo object, my_pos_servo.
pwm0 = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50)
my_pos_servo = servo.Servo(pwm0)

# Create a rotational servo object, my_servo.
pwm1 = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=50)
my_rot_servo1 = servo.ContinuousServo(pwm1) 

# repeat x your number of rotational servos 


# ----------- INIT VARIABLES ------------

# button states
up = True
# down = True
# left = True
# right = True
# photo_button = True

# directional states
z_state = "stop"
y_state = "stop"
take_photo = False

# servo throttles set to stop positions
my_rot_servo1.throttle = 0.0
# servo 2, 3, and so on

# stylus positional servo angles, CALIBRATE these to your specific needs
stylus_rest = 30
stylus_actuate = 120

my_pos_servo.angle = stylus_rest 

# Main Loop Start
print("starting loop")
while True:
    # read x5 buttons, replace your read values
    up = up_button.value
    down = True
    right = True
    left = True
    photo_button = True

    # z_state controls
    if not up:  # Up button pressed
        print("up button pressed!")
        z_state = "up"
    elif not down:  # down button pressed
        print("down button pressed!")
        z_state = "down"
    
    # x_state controls
    # if not left...
    # elif not right...

    # photo button
    if not photo_button:  # photo button pressed
        print("photo button pressed!")
        take_photo = True
    
    # z_state control (up/down)
    if z_state == "up":
        # replace these with your correct servos + values
        my_rot_servo1.throttle = 0.3
    elif z_state == "down":
        my_rot_servo1 = -0.3
    else:
        my_rot_servo1 = 0.0  # we're not moving up or down, so stop

    # x_state control (left/right)
    # if x_state == "left": ...
    # elif x_state == "right": ...
    # else: ...  # we're stopped

    if take_photo:  # we requested to take a photo
        # stop all up/down servos
        my_rot_servo1.throttle = 0.0

        # move positional servo to take photo. CALIBRATE angles + sleep time
        my_pos_servo.angle = stylus_actuate
        time.sleep(.4)  # brief pause to allow servo to reach correct angle
        my_pos_servo.angle = stylus_rest
        take_photo = False  # turn off photo
    else:
        my_pos_servo.angle = stylus_rest  # return stylus to rest
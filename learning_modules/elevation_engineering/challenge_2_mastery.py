''' 

MASTERY LEVEL PROGRAM

'''

# import Libraries
import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
from adafruit_motor import servo
import time

# ------------ BUTTONS INIT ---------------
# repeat init statements for all x5 buttons

# --------------- SERVOS INIT -------------
# Create a positional servo object for stylus


# Create several rotational servo objects for your lifts

# ----------- INIT VARIABLES ------------

# button states
up = True
# repeat for all states...

# directional states (z, x, take_photo)


# servo throttles set to stop positions

# stylus positional servo angles, CALIBRATE these to your specific needs
stylus_rest = 30
stylus_actuate = 120

# set to rest position

# Main Loop Start
print("starting loop")
while True:
    # read x5 buttons, replace your read values

    # z_state controls
    if not up:  # Up button pressed
        pass
    elif not down:  # down button pressed
        pass
    
    # x_state controls
    # if not left...
    # elif not right...

    # photo button
    
    # z_state control (up/down)
    if z_state == "up":
        pass
    # elif ==?
    # else: stop

    # x_state control (left/right)

    if take_photo:  # we requested to take a photo
        # stop all up/down servos

        # move positional servo to take photo. CALIBRATE angles + sleep time
    else:
        pass
        # return stylus to rest
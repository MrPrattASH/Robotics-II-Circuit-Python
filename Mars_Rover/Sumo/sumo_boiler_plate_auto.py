import time
import board
from digitalio import DigitalInOut, Pull, Direction
from timer import Timer
from adafruit_motor import servo
from sonarbit import Sonarbit
from arcade_drive_servo import Drive
from analogio import AnalogIn
from adafruit_simplemath import map_range
import neopixel 

# Initialize an instance of the Timer object
timer = Timer()

# Initialize an instance of the arcade_drive Object with tuned stop values
# this ALSO INITIALIZES YOUR SERVOS, do not init individual servos
drive = Drive(left_pin=board.D2, right_pin=board.D3, left_stop=0.0, right_stop=0.0)

# Init Neopixel LED
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.5, auto_write=True)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# TODO: init x1 button
button = DigitalInOut(board.D9)  #TODO: adjust to correct pin input
button.direction = Direction.INPUT
button.pull = Pull.UP

# TODO: init x1 servo object for Attack Mechanism 

# TODO: Init distance sensor

# TODO: import analog line_sensor 

def read_analog(pin):
    #maps our current 0>65536 along sensor to sometime more useful, like 0>100
    return map_range(pin.value, 0, 65536, 0, 100)

# ------------------------ STATE FUNCTIONS ------------------------
# don't change these global variables, use it in your distance sensor function with global prev_distance
prev_distance = 570

def auto_state():
    global prev_distance
    ''' write all auto state code here

    ALGORITHM:
    1. read line_sensor
    2. if on black: (reading greater than 80-ish, depends on your sensor)
        3. reverse (drive.drive(50,<50)), sleep, turn 180* (drive.drive(!=50, 50)), sleep
    3. if not on black:
        4. Move forward (drive.drive(50,>50))
        5. read distance sensor 
        6. if found robot:
            7. activate attack mechanism
        6. if not found robot:
            7. deactivate attack mechanism

    '''

def stop_state():
    # turn off all motors & sensors in this state. Activate the blue light
    drive.drive(50,50)
    pixels.fill(BLUE)

# -----------------------------------------------------------------
# -------------------- WHILE TRUE -----------------------------
# DO NOT CHANGE ANY OF THE CODE BELOW.
# only change code in the auto_state() function
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# Variables to control various states
auto = False
teleop = False
init_battle = False

while True:
    if not button.value:
        init_battle = True

    if init_battle:  # start battle
        print("Starting battle. Init auto timer of 45s")
        timer.set_timer(time.monotonic(), time.monotonic() + 45)  # make 45s timer for auto
        auto = True
        init_battle = False
        pixels.fill(GREEN)

    elif auto:  # auto mode checks
        if timer.check_timer():  # check if auto mode is over
            print("auto timer up! init teleop timer") 
            auto = False
            stop_state()
            break  # end loop & main program. 

        else:  # if our timer is not up, enter auto state.
            auto_state()  # enter auto state
    
    else:  # if not init_battle OR not auto, enter stop state. 
        stop_state()

    time.sleep(0.01) # small sleep to prevent CPU overload & button debounces

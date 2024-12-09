import time
import board
from digitalio import DigitalInOut, Pull, Direction
from rc import RCReceiver
from timer import Timer
from adafruit_motor import Servo
from arcade_drive_servo import Drive


# Initialize an instance of the receiver with designated pins for channels
rc = RCReceiver(ch1=board.D10, ch2=board.D11, ch3=None, ch4=None, ch5=board.D12, ch6=board.D13)

# Initialize an instance of the Timer object
timer = Timer()

# Initialize an instance of the arcade_drive Object with tuned stop values
# this ALSO INITIALIZES YOUR SERVOS, do not init individual servos
drive = Drive(left_pin=board.D2, right_pin=board.D3, left_stop=0.0, right_stop=0.0)


# TODO: Init x3 LEDs & directions

# TODO: Init distance sensor

# TODO: import analog line_sensor mapped reading function
'''
def read_analog(pin):
    # read & maps analog line sensor
'''


# ------------------------ STATE FUNCTIONS ------------------------
# don't change these global variables
prev_distance = 570
channels = [1,2,6]
spin = 50
throttle = 50
switch_c = 0


def auto_state():
    ''' write all auto state code here

    ALGORITHM:
    1. read line_sensor
    2. if on black:
        3. reverse (drive.drive(50,<50)), sleep, turn 180* (drive.drive(!=50, 50)), sleep
    3. if not on black:
        4. Move forward (drive.drive(50,>50))
        5. read distance sensor
        6. if found robot:
            7. activate attack mechanism
        6. if not found robot:
            7. deactivate attack mechanism

    '''
    global prev_distance

def teleop_state():
    '''
    write all teleop state code here

    ALGORITHM:
    1. read x3 RC channels (1: spin, 2: throttle, 6: switch_c)
    2. call drive.drive(spin,throttle) with spin + throttle values
    3. if switch_c == 1:
        4. activate attack mechanism
    3. if switch_c != 1:
        4. deactivate attack mechanism
    '''
    global channels, spin, throttle, switch_c

    # read channels
    for i in range(len(channels)):
        channel_value = rc.read_channel(channels[i])

    # assign variables values based on channel reading
    if channel_value is not None:
        if channels[i] == 1:
            spin = channel_value
        elif channels[i] == 2:
            throttle = channel_value
        elif channels[i] == 6:
            switch_c = channel_value

    # ^^ write code here. Don't change above ^^


def stop_state():
    # turn off all motors & sensors in this state. Activate the blue light
    drive.drive(50,50)

# -----------------------------------------------------------------
# -------------------- WHILE TRUE -----------------------------
# DO NOT CHANGE ANY OF THE CODE BELOW.
# only change code in the auto_state(), teleop_state(), and stop_state() functions
# -----------------------------------------------------------------
# -----------------------------------------------------------------


# Variables to store the values read from each channel
sw_b = 0

# Variables to control various states
auto = False
teleop = False
init_battle = False

while True:
    # Read switch B
    switch_b = rc.read_channel(5)

    # setup logic for active robot
    if switch_b is not None:  # switch returned a valid reading
        if switch_b == 1:  # switch is on

            if init_battle:  # start battle
                # set 30s timer
                auto = True
                init_battle = False
                # LEDs on/off

            elif auto:  # auto mode checks
                time_end = False  # check timer
                if time_end:  # check if auto mode is over
                    # set 90s timer
                    auto = False
                    teleop = True
                    # LEDs on/off
                else:
                    auto_state()  # enter auto state

            elif teleop: # teleop mode checks
                time_end = False
                if time_end:  #90s timer is up, end battle.
                    teleop = False
                    stop_state()
                else:
                    teleop_state() # enter teleop state

        else:  # switch is off
            init_battle = True
            auto = False
            teleop = False
            stop_state()

    rc.ensure_cycle()  # Pause for 20ms, the length of a single duty cycle of the RC receiver.


import time
import board
from digitalio import DigitalInOut, Pull, Direction
import rc
from timer import Timer
from adafruit_motor import Servo
from arcade_drive_servo import Drive


# Initialize an instance of the receiver with designated pins for channels
rc = rc.RCReceiver(ch1=board.D10, ch2=board.D11, ch3=None, ch4=None, ch5=board.D12, ch6=board.D13)

# Initialize an instance of the Timer object
timer = Timer()

# Initialize an instance of the arcade_drive Object with tuned stop values
# this ALSO INITIALIZES YOUR SERVOS, do not init individual servos
drive = Drive(left_pin=board.D2, right_pin=board.D3, left_stop=0.0, right_stop=0.0)


# TODO: Init x3 LEDs & directions

# TODO: Init distance sensor & get_distance() function

''' def read_distance()
    global prev_distance  # get old distance!
'''

# TODO: import analog line_sensor mapped reading function
'''
def read_analog(pin):
    # read & maps analog line sensor    
'''

''' def read_distance()
    global prev_distance  # get old distance!
'''

# TODO: init x1 servo object for Attack Mechanism 

# ------------------------ STATE FUNCTIONS ------------------------
# don't change these global variables, use it in your distance sensor function with global prev_distance
prev_distance = 570

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
    pass  # delete the word "pass" once you've written code 

def teleop_state():
    '''
    write all teleop state code here
    
    ALGORITHM:
    1. read x3 RC channels (1: spin, 2: throttle, 6: ch_6)
    2. call drive.drive(spin,throttle) with spin + throttle values
    3. if ch_6 is 1:
        4. activate attack mechanism
    3. if ch_6 is not 1:
        4. deactivate attack mechanism
    '''

    # read channels
    spin = rc.read_channel(1)
    throttle = rc.read_channel(2)
    ch_6 = rc.read_channel(6)
    
    # ^^ write code below this comment. Don't change above ^^
    

def stop_state():
    # turn off all motors & sensors in this state. Activate the blue light
    drive.drive(50,50)
    # TODO: activate blue light

# -----------------------------------------------------------------
# -------------------- WHILE TRUE -----------------------------
# DO NOT CHANGE ANY OF THE CODE BELOW.
# only change code in the auto_state(), teleop_state(), and stop_state() functions
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# Variables to control various states
auto = False
teleop = False
init_battle = False

while True:
    # Read channel 5 (top left switch) 
    ch_5 = rc.read_channel(5)
    print(ch_5)
    
    # setup logic for active robot
    if ch_5 == 1:  # switch is on
        if init_battle:  # start battle
            print("Starting battle. Init auto timer of 30s")
            timer.set_timer(time.monotonic(), time.monotonic() + 30)  # make 30s timer for auto
            auto = True
            init_battle = False
            # TODO: Turn LEDs on/off

        elif auto:  # auto mode checks
            time_end = timer.check_timer()  # check timer, returns True if time's up
            if time_end:  # check if auto mode is over
                print("auto timer up! init teleop timer") 
                timer.set_timer(time.monotonic(), time.monotonic() + 90)  # make 90s timer for teleop
                auto = False
                teleop = True
                # TODO: Turn LEDs on/off

            else:
                auto_state()  # enter auto state

        elif teleop: # teleop mode checks
            time_end = timer.check_timer()
            if time_end:  #90s timer is up, end battle.
                print("battle over!")
                stop_state()
                break  # end while True loop and stop program.  
            else:
                teleop_state() # enter teleop state

    else:  # switch is off
        print("channel 5 off")
        init_battle = True
        auto = False
        teleop = False
        stop_state()
        # TODO: Turn LEDs on/off


    rc.ensure_cycle()  # Pause for 20ms, the length of a single duty cycle of the RC receiver.


import time
import board
from digitalio import DigitalInOut, Pull, Direction
from rc import RCReceiver
from timer import Timer
from adafruit_motor import Servo
from arcade_drive_servo import Drive


# Initialize an instance of the receiver with designated pins for channels
rc = RCReceiver(ch1=board.D0, ch2=board.D1, ch3=None, ch4=None, ch5=board.D2, ch6=board.D3)

# Initialize an instance of the Timer object
timer = Timer()

# Initialize an instance of the arcade_drive Object with tuned stop values
drive = Drive(left_pin=board.D4, right_pin=board.D5, left_stop=0.0, right_stop=0.0)

# ------------------------ STATE FUNCTIONS ------------------------

def auto_state():
    # write all auto state code here
    line_sensor = 0
    pass

def teleop_state():
    # write all teleop state code here
    spin = 50
    throttle = 50
    sw_c = 0
    channels = [1, 2, 5, 6]

    # read channels
    for i in range(len(channels)):
        channel_value = rc.read_channel(channels[i])
    
    if channel_value is not None:
        if channels[i] == 1:
            spin = channel_value
        elif channels[i] == 2:
            throttle = channel_value
        elif channels[i] == 5:
            sw_b = channel_value
        elif channels[i] == 6:
            sw_c = channel_value
    pass

def stop_state():
    # turn off all motors & sensors in this state. Activate the blue light
    pass

# -------------------- INIT VARIABLES -----------------------------

# Variables to store the values read from each channel
sw_b = 0

# Variables to control various states
auto = False
teleop = False
init_battle = False


while True:
    # Read switch B
    sw_b = rc.read_channel(5)
    
    # setup logic for active robot
    if sw_b is not None:  # switch returned a valid reading
        if sw_b == 1:  # switch is on

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
    
    time.sleep(0.02)  # Pause for 20ms, the length of a single duty cycle of the RC receiver.


'''Basic RC Analog input Control
Outputs an analog channel duty cycle rating.

Using the analog joysticks on the FlySky FS-i6X, this program currently reads the channel initialized
as a digital pin, then outputs an arbitrary -100 > 0 > 100 value depending on joystick location.

The program also allows for a larger deadpoint within the joystick, allowing for some "slop" in the centre.
'''

from digitalio import DigitalInOut, Direction, Pull
import board
import time
from adafruit_simplemath import map_range
from math import floor

#init channel pin as a digital input. Defaults to a FALSE reading, so we must pull down.
#PWM will input as low/high values
ch1 = DigitalInOut(board.D0)
ch1.direction = Direction.INPUT
ch1.pull = Pull.DOWN

def read_analog_ch(pin, lower_range_bound = -100, upper_range_bound = 100, deadpoint = 0):
    '''
    Reads a value from an analog channel on an RC reciever.

    :pin: the current channel pin we wish to read. must be initialized as digitalinout, input, and pull.down
    :lower_range_bound: integer: the lower range output. Servo's typically take 1120 at this value for -100% speed or 0*
    :upper_range_bound: integer: the upper range output. Servo's typically take 1920 at this value for 100% speed or 180*
    :deadpoint: integer: accepts whatever "stop" or "90*" would be on a servo. typically 1520
    :returns: the current value read from the pin, mapped to the user-input range boundaries

    '''
    #start low value
    while not pin.value:
        pass
    #get high value
    start = time.monotonic_ns()
    while pin.value:
        pass
    end = time.monotonic_ns()

    #convert time.monotonic into a nice 4 digit duty_cycle value
    in_width = floor((end - start)/1000)
    #deadpoint centre for joystick
    if in_width > 1400 and in_width < 1520:
        out_value = deadpoint
    else:
        out_value = floor(map_range(in_width,800,2100,lower_range_bound,upper_range_bound))
    return out_value
    #note, do NOT introduce a sleep into this code, or it will output odd numbers.

while True:
    print(read_analog_ch(ch1))
    #time.sleep(.2)


""" RC Analog input Filtering
Outputs a filtered analog channel duty cycle rating.

Reading PWM is inherently noisy in CircuitPython. This is a simple moving(rolling) average program
that takes the most recent 2 readings from the analog joystick, checks if they are both equal,
and then updates the output joystick value if the readings were the same.

Often times, the PWM will output 4-5 of the same value, then 1 high value, then return to baseline.
A filter of the 2 most recent passes *should* be sufficient enough to reduce output noise to a motor controller.

This program builds upon the previous read_analog_ch program
"""

from digitalio import DigitalInOut, Direction, Pull
import board
import time
from adafruit_simplemath import map_range
from math import floor

# init channel pin as a digital input. Defaults to a FALSE reading, so we must pull down.
# PWM will input as low/high values
# init RC Controller
# R joystick LR
ch1 = DigitalInOut(board.D5)
ch1.direction = Direction.INPUT
ch1.pull = Pull.DOWN

# R joystick UD
ch2 = DigitalInOut(board.D6)
ch2.direction = Direction.INPUT
ch2.pull = Pull.DOWN

def read_analog_ch(
    pin, lower_range_bound=1.12, upper_range_bound=1.92, deadpoint=1.52
):
    """
    Reads a value from an analog channel on an RC reciever.

    :pin: the current channel pin we wish to read. must be initialized as digitalinout, input, and pull.down
    :lower_range_bound: integer: the lower range output. Servo's typically take 1120 at this value for -100% speed or 0*
    :upper_range_bound: integer: the upper range output. Servo's typically take 1920 at this value for 100% speed or 180*
    :deadpoint: integer: accepts whatever "stop" or "90*" would be on a servo. typically 1520
    :returns: the current value read from the pin, mapped to the user-input range boundaries

    """
    # start low value
    while not pin.value:
        pass
    # get high value
    start = time.monotonic_ns()
    while pin.value:
        pass
    end = time.monotonic_ns()

    # convert time.monotonic into a nice 4 digit duty_cycle value
    in_width = floor((end - start) / 1000)
    # deadpoint centre for joystick
    if in_width > 1400 and in_width < 1520:
        out_value = deadpoint
    else:
        out_value = map_range(in_width, 800, 2100, lower_range_bound, upper_range_bound)

    # Allow for next PWM cycle frequency to read correctly
    # If we don't sleep, we'll start 'out of sync' with the PWM cycle
    # and only return LOW values.
    time.sleep(0.00151)
    return out_value

def moving_average(avg_list: list, new_measure, num_of_polls = 2):
    '''
    Creates a list of the last num_of_polls sensor readings

    :avg_list: list: the global list we will del[0] and append[new_measure]
    :new_measure: int: the current sensor reading
    :num_of_polls: int:  how many polls you want the list to consist of. As our sensors are only slightly noisy,
    an average of 2 polls is sufficient to clear out the noise. If not, increase this to 3, but know this will
    dramatically slow down response time
    '''
    avg_list.append(new_measure)
    if len(avg_list) > num_of_polls:
        del avg_list[0]

def all_equal(lst: list):
    """
    Checks if list is all equal.
    :lst: a list of any length
    :returns: True if all list entries are equal, else, False
    """
    if lst.count(lst[0]) == len(lst):
        return True
    else:
        return False

#create a moving average list
y_moving_avg = [0,0]
x_moving_avg = [0,0]
#create an actual output value to send to motors
x_out = 0
y_out = 0

while True:
    # Get RC joystick Readings (re-map range to arbitrary numbers)
    y_joy_cur = read_analog_ch(ch2, -1, 1, 0)
    x_joy_cur = read_analog_ch(ch1, -1, 1, 0)

    #update moving average list (so we have the most current 2 readings)
    moving_average(x_moving_avg, x_joy_cur)
    moving_average(y_moving_avg, y_joy_cur)

    #check for sensor noise. If not present, update output from axis
    if all_equal(x_moving_avg):
        x_out = x_moving_avg[0]
    if all_equal(y_moving_avg):
        y_out = y_moving_avg[0]

    print("x out: " + str(x_out) + " y out: " + str(y_out))



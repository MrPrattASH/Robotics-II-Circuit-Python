# Write your code here :-)
"""Basic RC Analog input Control
Outputs an analog channel duty cycle rating.

Using the analog joysticks on the FlySky FS-i6X, this program currently reads the channel initialized
as a digital pin, then outputs an arbitrary -100 > 0 > 100 value depending on joystick location.

The program also allows for a larger deadpoint within the joystick, allowing for some "slop" in the centre.
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

# SwB 2 way toggle
ch5 = DigitalInOut(board.D7)
ch5.direction = Direction.INPUT
ch5.pull = Pull.DOWN

# SwC 3 way toggle
ch6 = DigitalInOut(board.D8)
ch6.direction = Direction.INPUT
ch6.pull = Pull.DOWN

def read_switch_ch(pin, three_way_switch=False):
    """
    Reads a value from an analog channel on an RC reciever.

    :pin: the current channel pin we wish to read. must be initialized as digitalinout, input, and pull.down
    :three_way_switch: Bool: Default is a 2-way toggle switch. If true, will return a 3way toggle switch
    :returns: if 2 way switch, 0, 1, if 3 way switch, 0,1,2

    """
    # start low value
    start = time.monotonic_ns()
    # time_monotonic call stops a program break if no signal is recieved
    while not pin.value:
        pass
    # get high value
    start = time.monotonic_ns()
    while pin.value:
        pass
    end = time.monotonic_ns()

    # convert time.monotonic into a nice 4 digit duty_cycle value
    in_width = floor((end - start) / 1000)

    # 2-way switch
    if not three_way_switch:
        # switch in up position (OFF)
        if in_width <= 1500:
            out_value = 0
        else:
            out_value = 1

    # 3-way switch
    else:
        # bottom position
        if in_width <= 1200:
            out_value = 0
        # top position
        elif in_width >= 1800:
            out_value = 2
        # mid position
        else:
            out_value = 1
    #10ms allow for next PWM cycle frequency to read correctly
    #If we don't sleep, we'll start 'out of sync' with the PWM cycle
    #and only return LOW values. Best trial and error reliable value returned 1.51ms wait time.
    time.sleep(0.00151)
    return out_value

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

    # 10ms allow for next PWM cycle frequency to read correctly
    # If we don't sleep, we'll start 'out of sync' with the PWM cycle
    # and only return LOW values.
    time.sleep(0.00151)
    return round(out_value,3)

def exponential_filter(prev_measure, cur_measure, weight):
    return round(weight * cur_measure + (1-weight) * prev_measure,3)

def moving_average(avg_list, new_measure, num_of_polls):
    avg_list.append(new_measure)
    if len(avg_list) > num_of_polls:
        del avg_list[0]

#for exponential_filter func. values always start at 0 code startup.
weight = 0.4
prev_y = 0
prev_x = 0
moving_x_avg_lst = [0,0]
moving_y_avg_lst = [0,0]
moving_x = 0
moving_y = 0
num_polls = 2
while True:
    # Get RC Readings
    sw_c = read_switch_ch(ch6, three_way_switch=True)
    sw_b = read_switch_ch(ch5, three_way_switch=False)
    y_joy_cur = read_analog_ch(ch2, -1, 1, 0)
    x_joy_cur = read_analog_ch(ch1, -1, 1, 0)
    #print("C " + str(sw_c) + " B " + str(sw_b) + " x " + str(x_joy) + " y " + str(y_joy))

    #filter x/y in exponential_filter
    #y_exp_filter = exponential_filter(prev_y, y_joy_cur, weight)
    #x_exp_filter = exponential_filter(prev_x, x_joy_cur, weight)
    #print("x_f " + str(x_exp_filter) + " y_f " + str(y_exp_filter))

    #assign moving exponental average, delete oldest reading
    #moving_average(moving_x_avg_lst, x_exp_filter, num_polls)
    #moving_average(moving_y_avg_lst, y_exp_filter, num_polls)
    #print(moving_x_avg_lst)

    #make lists without exponential_filter
    moving_average(moving_x_avg_lst, x_joy_cur, num_polls)
    moving_average(moving_y_avg_lst, y_joy_cur, num_polls)

    #count the first item in the list. if it is == len of list, means that all items are equal inside, and we have
    #filtered out the noise
    if moving_x_avg_lst.count(moving_x_avg_lst[0]) == len(moving_x_avg_lst):
        print(moving_x_avg_lst)

    #TODO, is 2 values enough to take out 1 signal pulse of noise?)

    '''
    #moving average x
    for i in range(len(moving_x_avg_lst)):
        moving_x += moving_x_avg_lst[i]
    moving_x = round(moving_x/num_polls,3)

    #moving average y
    for i in range(len(moving_y_avg_lst)):
        moving_y += moving_y_avg_lst[i]
    moving_y = round(moving_y/num_polls,3)
    '''

    #print("x_m " + str(moving_x) + " y_m " + str(moving_y))

    #assign previous measures
    prev_y = y_joy_cur
    prev_x = x_joy_cur


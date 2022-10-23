"""Basic RC Library import
Provides functions for:
- Reading analog joysticks
- Reading toggle switches
- calculating a moving average
- equal list noise filtering
"""


import time
from math import floor
from adafruit_simplemath import map_range

def read_3way_switch(pin):
    """
    Reads a value from an analog channel on an RC reciever.

    :pin: the current channel pin we wish to read. must be initialized as digitalinout,
    input, and pull.down
    :returns: 0,1,2 for up, mid, down

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

    # bottom position
    if in_width <= 1200:
        out_value = 0
    # top position
    elif in_width >= 1800:
        out_value = 2
    # mid position
    else:
        out_value = 1
    # 10ms allow for next PWM cycle frequency to read correctly
    # If we don't sleep, we'll start 'out of sync' with the PWM cycle
    # and only return LOW values. Best trial and error reliable value
    # returned 1.51ms wait time.
    time.sleep(0.00151)
    return out_value


def read_2way_switch(pin):
    """
    Reads a value from an analog channel on an RC reciever.

    :pin: the current channel pin we wish to read. must be initialized as digitalinout,
    input, and pull.down
    :returns: 0, 1 for on / off

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

    # switch in up position (OFF)
    if in_width <= 1500:
        out_value = 0
    else:
        out_value = 1

    # 10ms allow for next PWM cycle frequency to read correctly
    # If we don't sleep, we'll start 'out of sync' with the PWM cycle
    # and only return LOW values. Best trial and error reliable value
    # returned 1.51ms wait time.
    time.sleep(0.00151)
    return out_value


def read_analog(pin, lower_range_bound=-1, upper_range_bound=1, deadpoint=0):
    """
    Reads a value from an analog channel on an RC reciever.

    :pin: the current channel pin we wish to read. must be initialized as digitalinout,
    input, and pull.down
    :lower_range_bound: integer: the lower range output. Servo's typically take 1120 at
    this value for -100% speed or 0*
    :upper_range_bound: integer: the upper range output. Servo's typically take 1920 at
    this value for 100% speed or 180*
    :deadpoint: integer: accepts whatever "stop" or "90*" would be on a servo. typically
    1520
    :returns: the current value read from the pin, mapped to the user-input range
    boundaries

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
    return out_value


def upd_mov_avg(avg_list: list, new_measure, num_of_polls=2):
    """
    Creates a list of the last num_of_polls sensor readings

    :avg_list: list: the global list we will del[0] and append[new_measure]
    :new_measure: int: the current sensor reading
    :num_of_polls: int:  how many polls you want the list to consist of. As our sensors
    are only slightly noisy,
    an average of 2 polls is sufficient to clear out the noise. If not, increase this to
    3, but know this will
    dramatically slow down response time
    """
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

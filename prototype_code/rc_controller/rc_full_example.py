"""Basic RC Analog input Control Full example
Full RC example for all 6 channels populated.

Note, likely you will not use Channels 3/4 as analog inputs, though they exist for example purposes.
"""

from digitalio import DigitalInOut, Direction, Pull
import board
import time
from math import floor
from adafruit_simplemath import map_range

# init RC Channels

# R joystick LR
ch1 = DigitalInOut(board.D2)
ch1.direction = Direction.INPUT
ch1.pull = Pull.DOWN

# R joystick UD
ch2 = DigitalInOut(board.D3)
ch2.direction = Direction.INPUT
ch2.pull = Pull.DOWN

# L joystick LR
ch3 = DigitalInOut(board.D4)
ch3.direction = Direction.INPUT
ch3.pull = Pull.DOWN

# L joystick UD
ch4 = DigitalInOut(board.D5)
ch4.direction = Direction.INPUT
ch4.pull = Pull.DOWN

# SwB 2 way toggle
ch5 = DigitalInOut(board.D6)
ch5.direction = Direction.INPUT
ch5.pull = Pull.DOWN

# SwC 3 way toggle
ch6 = DigitalInOut(board.D7)
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
    # 10ms allow for next PWM cycle frequency to read correctly
    # If we don't sleep, we'll start 'out of sync' with the PWM cycle
    # and only return LOW values.
    time.sleep(0.01)
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
        out_value = floor(
            map_range(in_width, 800, 2100, lower_range_bound, upper_range_bound)
        )
    # 10ms allow for next PWM cycle frequency to read correctly
    # If we don't sleep, we'll start 'out of sync' with the PWM cycle
    # and only return LOW values.
    time.sleep(0.01)
    #divide outvalue by 1000 to convert to a ms command we can use for sending a low_level control servo duty cycle
    out_value = out_value/1000
    return out_value


while True:
    # Read all channels
    right_l_r_joy = read_analog_ch(ch1)
    right_fwd_rev_joy = read_analog_ch(ch2)
    left_l_r_joy = read_analog_ch(ch3)
    left_fwd_rev_joy = read_analog_ch(ch4)
    sw_b = read_switch_ch(ch5)
    sw_c = read_switch_ch(ch6)

    # read channels 1 at a time
    print("SwC value:" + str(sw_c))
    # print("SwB value:" + str(sw_b))
    # print("Left Joystick Up/Down value:" + str(left_fwd_rev_joy))
    # print("Left Joystick Left/Right value:" + str(left_l_r_joy))
    # print("Right Joystick Up/Down value:" + str(right_fwd_rev_joy))
    # print("Right Joystick Left/Right value:" + str(right_l_r_joy))
    # note, do not add a sleep inside your main loop, it slows down RC transmission GREATLY and introduces much noise

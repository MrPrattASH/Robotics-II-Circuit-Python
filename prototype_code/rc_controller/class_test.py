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

# SwB 2 way toggle
ch5 = DigitalInOut(board.D7)
ch5.direction = Direction.INPUT
ch5.pull = Pull.DOWN

# SwC 3 way toggle
ch6 = DigitalInOut(board.D8)
ch6.direction = Direction.INPUT
ch6.pull = Pull.DOWN


class FlySky:
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
        # and only return LOW values. Best trial and error reliable value returned 1.51ms wait time.
        time.sleep(0.00151)
        return out_value

fly_sky = FlySky()

while True:
    # Get RC Readings
    """
    sw_c = read_switch_ch(ch6, three_way_switch=True)
    sw_b = read_switch_ch(ch5, three_way_switch=False)
    """

    sw_c = fly_sky.read_switch_ch(ch6, three_way_switch=True)
    sw_b = fly_sky.read_switch_ch(ch5)

    print("B out: " + str(sw_b) + " C out: " + str(sw_c))

#i2C 128 x 64 MONO OLED Example

"""
This test will show quick print statements to the OLED screen via a function
"""

import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import time

#reset displays, needed as if the m4 reboots, we must release the screen before init again.
displayio.release_displays()

oled_reset = board.D9

# init i2C object
i2c = board.I2C()
#perhaps capitalD for address?)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=oled_reset)

#display parameters
WIDTH = 128
HEIGHT = 64
BORDER = 5

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

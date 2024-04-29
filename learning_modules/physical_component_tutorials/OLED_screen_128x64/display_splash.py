#i2C 128 x 64 MONO OLED Example
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# Modified by BroganPratt for School use
# SPDX-License-Identifier: MIT

"""
This test will initialize the display and display a quick splash. Once complete, open the
REPL and try to type something, then watch your OLED screen!
"""

import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

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

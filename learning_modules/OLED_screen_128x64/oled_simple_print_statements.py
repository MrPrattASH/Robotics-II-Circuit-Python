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

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

def display_word(word):
    # Set text, font, and color
    text = str(word)
    font = terminalio.FONT
    color = 0xFFFFFF

    # Create the text label
    text_area = label.Label(font, text=text, color=color, x = 28, y=HEIGHT // 2-1)
    # Show it
    display.show(text_area)

# Loop forever so you can enjoy your image
while True:
    display_word("hello")
    time.sleep(1)
    display_word("new word")
    time.sleep(1)

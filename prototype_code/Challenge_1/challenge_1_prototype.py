#First Challenge Example Board

# button swaps between modes - Color chase or straight fill colour
# 1. colour chase, colour based on distance from sensor
# 2. fill, num_pixels based on distance from sensor
# OLED Screen describes score & distance in each case

import board
from digitalio import DigitalInOut, Direction, Pull
import time
from math import floor
import neopixel
from adafruit_simplemath import map_range
import terminalio
import displayio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

#init button D12 as pull down
#it's pull down due to GND on constant loop, and stops signal noise present
button = DigitalInOut(board.D12)
button.direction = Direction.INPUT
button.pull = Pull.DOWN

#init ping sensor D7
ping_sensor = DigitalInOut(board.D7)

#init neopixel ring D8
num_pixels = 16
pixels = neopixel.NeoPixel(board.D8, num_pixels, brightness=0.1)

#reset displays, needed as if the m4 reboots, we must release the screen before init again.
displayio.release_displays()

oled_reset = board.D9
# init i2C object for OLED screen
i2c = board.I2C()
#perhaps capitalD for address?)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=oled_reset)

def sonar(pin):
    ''' Get a ping reading from 5cm>568cm from the Elecfreaks Pin Sensor. Trigger & Echo are on the 'same pin'.
    pin = the pin with the ping sensor
    returns: Distance in cm between 0 & 568

    Note: If object is <5cm away, it will register either 0 or 568cm away.
    Note: Introduce a 0.1sec delay when taking sensor readings in CircuitPython, else the code will stop parsing.

    '''

    usleep = lambda x: x/1000000

    pin.direction = Direction.OUTPUT

    #send trigger signal
    pin.value = 0
    usleep(2)
    pin.value = 1
    usleep(10)
    pin.value = 0

    #recieve echo signal
    pin.direction = Direction.INPUT
    while pin.value == 0:
        start_time = time.monotonic_ns()

    while pin.value == 1:
        end_time = time.monotonic_ns()

    #If an object is too close, start_time will never be assigned because pin.value will never equal 0, causing a variable assignment error & crash.
    try:
        # Distance is defined as time/2 (there and back) * speed of sound 34000 cm/s
        distance = floor((end_time - start_time) * 34000/2/1000000000)
    except:
        print("object too close")
        distance = 0

    return distance

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
        pixels.show()

#OLED Screen setup
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

#create a full white rectangle object
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
#write the object to the display
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)

def display_word(word):
    # Set text, font, and color on OLED screen
    text = str(word)
    font = terminalio.FONT
    color = 0xFFFFFF

    # Create the text label
    text_area = label.Label(font, text=text, color=color, x = 28, y=HEIGHT // 2-1)
    # Show it
    display.show(text_area)

#init declare variables
button_state = False
distance = 0
wait = 0.02

#main colours for use with neopixel
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0,0,0)

def colour_chase_state():
    #show what state we're in
    display_word("Colour Chase\nDistance: " + str(distance))

    if distance < 30:
        color_choice = RED
    elif distance <= 70 and distance >= 30:
        color_choice = YELLOW
    else:
        color_choice = GREEN
    color_chase(color_choice, wait)
    pixels.fill(OFF)
    pixels.show()
    pixels.show()

def fill_state():
    #show what state we're in
    display_word("Colour Fill\nDistance: " + str(distance))

    #plot to only several pixels
    pixels_to_show = int(map_range(distance,0,100,0,15))

    #turn off pixels above range to show
    for i in range(num_pixels-1, pixels_to_show, -1):
        pixels[i] = OFF
        pixels.show()

    #show pixels in range
    for i in range(pixels_to_show):
        pixels[i] = CYAN
        pixels.show()


while True:
    #is button pushed or not
    button_state = button.value

    #get ping value
    distance = sonar(ping_sensor)

    if button_state:
        colour_chase_state()
    else:
        fill_state()








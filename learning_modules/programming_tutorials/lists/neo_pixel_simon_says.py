import time
import board
from rainbowio import colorwheel
import neopixel
import random

#Initialize neopixel strip w/ 16 pixels
pixels = neopixel.NeoPixel(board.D2, 16, brightness=0.2)

# setup neopixel list 
pixels_array = []
for i in range(16):
    pixels_array.append(i)
print(pixels_array)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0, 0, 0)


while True:
    #simulate a 4 sided dice roll
    dice_roll = (random.randint(0,3) * 4)

    #choose a random colour to display
    colour = random.choice([RED,YELLOW,BLUE,GREEN])
    for i in range(4):
        pixels[i+dice_roll] = colour
    pixels.show()
    time.sleep(1)
    pixels.fill(OFF)


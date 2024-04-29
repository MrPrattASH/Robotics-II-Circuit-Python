#Onboard NeoPixel Example
#SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
#SPDX-License-Identifier: MIT

import time
import board
import neopixel

#onboard Neopixel is an RGB LED, not RGBW (RGB + W LED)
pixel_pin = board.NEOPIXEL

# The number of NeoPixels (on our m4 board, this is 1)
num_pixels = 1

# initialize our pixels pin, with the number of pixels attached to the device. 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)

def rainbow_cycle(wait):
    # rainbow colour cycle with 1ms delay per step
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

while True:
    #RED
    pixels.fill((255, 0, 0))
    pixels.show()
    time.sleep(1)

    #GREEN
    pixels.fill((0, 255, 0))
    pixels.show()
    time.sleep(1)

    #BLUE
    pixels.fill((0, 0, 255))
    pixels.show()
    time.sleep(1)

    rainbow_cycle(0.001)

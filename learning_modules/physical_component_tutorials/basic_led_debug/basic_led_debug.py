# Quick LED Debug Example. 
# Useful for giving you a visual que about what function is running. For example:
# Func 1 - LED constantly on
# Func 2 - LED off
# Func 3 - Blinking LED. etc. 

# First we need to import libraries (pre-built functions)

# the physical hardware pins on our board (every board is different, we need to import OUR specific board)
import board
# The code for accessing the pins on our board
import digitalio
# time based functions
import time

# intialize the red LED pin inside a variable. Now we don't need to call that pin each time...
led = digitalio.DigitalInOut(board.D13)
# We need to output to this LED. Inputs would be for a sensor. 
led.direction = digitalio.Direction.OUTPUT


# Blink LED every .5 second
# While True is your main "forever loop". Essentially, do this while True = True, hence, While True:
while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
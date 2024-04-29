import time
import board
import pwmio
from analogio import AnalogIn

# create an led object
led = pwmio.PWMOut(board.D7, frequency=5000, duty_cycle = 0)

#create pot sensor object
pot = AnalogIn(board.A1)

while True:
    led.duty_cycle = pot.value
    
    time.sleep(.1)

'''Basic RC Analog input Control
Outputs two toggle switches: SWC channel 6.
SWC is a 3 way toggle switch.

'''

import time
import board
from rc import RCReceiver

rc = RCReceiver(ch1=board.D10, ch2=board.D11, ch3=None, ch4=None, ch5=board.D12, ch6=board.D13)

# Main code
while True:
    # Read channels
    channel_6 = rc.read_channel(6)
    if channel_6 is not None: # must not be None to do something with the output
        print("Channel 6:", channel_6)
    
    rc.ensure_cycle()  # Maintains sync with our 20ms cycle every loop iteration





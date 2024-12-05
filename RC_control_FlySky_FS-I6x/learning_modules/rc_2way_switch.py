'''Basic RC Analog input Control
Outputs one toggle switches. SWB (Channel 5) 
SWB is a 2 way toggle switch. On/Off

'''

import time
import board
from rc import RCReceiver

rc = RCReceiver(ch1=board.D10, ch2=board.D11, ch3=None, ch4=None, ch5=board.D12, ch6=board.D13)

# Main code
while True:
    # Read channels
    channel_5 = rc.read_channel(5)
    if channel_5 is not None: # must not be None to do something with the output
        print("Channel 5:", channel_5)
    
    rc.ensure_cycle()  # Maintains sync with our 20ms cycle every loop iteration


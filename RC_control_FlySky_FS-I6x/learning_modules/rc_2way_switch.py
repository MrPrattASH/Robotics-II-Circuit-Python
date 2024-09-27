'''Basic RC Analog input Control
Outputs one toggle switches. SWB (Channel 5) 
SWB is a 2 way toggle switch. On/Off

'''

import time
import board
from rc import RCReceiver

rc = RCReceiver(ch1 = board.D0, ch2 = board.D1, ch3 = None, ch4 = None, ch5 =board.D2, ch6 =board.D3)

# Main code
while True:
    # Read channels
    channel_5 = rc.read_channel(5)
    if channel_5 is not None: # must not be None to do something with the output
        print("Channel 5:", channel_5)
    
    # sleep for 20ms at the end of our loop, the length of a single duty cycle of the RC reciever.
    time.sleep(0.02)


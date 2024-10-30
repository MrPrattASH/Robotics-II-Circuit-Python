import time
import board
from rc import RCReceiver

rc = RCReceiver(ch1=board.D10, ch2=board.D11, ch3=None, ch4=None, ch5=board.D12, ch6=board.D13)
channels = [1,2,5,6]
x = 0
y = 0
sw_b = 0
sw_c = 0

# Main code
while True:
    # Read channels in a loop, iterating through our list 
    for i in range(len(channels)):
        channel_value = rc.read_channel(channels[i])
        if channel_value is not None:
            if channels[i] == 1:
                x = channel_value
            elif channels[i] == 2:
                y = channel_value
            elif channels[i] == 5:
                sw_b = channel_value
            elif channels[i] == 6:
                sw_c = channel_value

    print("Ch 1:", x, "Ch 2:", y, "Ch 5:", sw_b, "Ch 6:", sw_c)

    # sleep for 20ms, the length of a single duty cycle of the RC reciever.
    time.sleep(0.02)
    

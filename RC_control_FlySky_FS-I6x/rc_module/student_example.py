import time
from rc import RCReceiver

rc = RCReceiver()

# Main code
while True:
    # Read channels
    channel_1 = rc.read_channel(1)
    #channel_2 = rc.read_channel(2)
    if channel_1 is not None: # must not be None to do something with the output
        print("1:", channel_1)

    # sleep for 20ms, the length of a single duty cycle of the RC reciever.
    time.sleep(0.02)
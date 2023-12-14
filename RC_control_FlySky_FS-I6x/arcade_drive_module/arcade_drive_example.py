import time
from rc import RCReceiver
from arcade_drive import Drive

rc = RCReceiver()
drive = Drive()

# Main code
while True:
    # Read joystick channels
    channel_1 = rc.read_channel(1) # spin
    channel_2 = rc.read_channel(2) # throttle

    if channel_1 is not None and channel_2 is not None: # must not be None to do something with the output
        drive.drive(channel_1,channel_2) # move our motors arcade drive style


    # sleep for 20ms, the length of a single duty cycle of the RC reciever.
    time.sleep(0.02)

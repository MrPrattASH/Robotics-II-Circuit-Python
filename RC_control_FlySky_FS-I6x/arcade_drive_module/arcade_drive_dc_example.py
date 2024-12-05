import time
import board
from rc import RCReceiver
from arcade_drive import Drive

rc = RCReceiver(ch1=board.D10, ch2=board.D11, ch3=None, ch4=None, ch5=board.D12, ch6=board.D13)
drive = Drive()

# Main code
while True:
    # Read joystick channels
    channel_1 = rc.read_channel(1) # spin
    channel_2 = rc.read_channel(2) # throttle

    if channel_1 is not None and channel_2 is not None: # must not be None to do something with the output
        drive.drive(channel_1,channel_2) # move our motors arcade drive style


    rc.ensure_cycle()  # Maintains sync with our 20ms cycle every loop iteration

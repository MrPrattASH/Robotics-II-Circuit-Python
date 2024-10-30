import board
import time
from rc import RCReceiver
from arcade_drive_servo import Drive

rc = RCReceiver(ch1=board.D10, ch2=board.D11, ch3=None, ch4=None, ch5=board.D12, ch6=board.D13)
drive = Drive(left_pin=board.D2, right_pin=board.D3, left_stop=0.0, right_stop=0.0)

channels = [1,2,5,6]

# Main code
while True:
    # Read joystick channels
    spin = rc.read_channel(1) # spin
    throttle = rc.read_channel(2) # throttle

    if spin is not None and throttle is not None: # must not be None to do something with the output
        drive.drive(spin,throttle)
        print("spin", spin, "throttle", throttle) # move our motors arcade drive style


    # sleep for 20ms, the length of a single duty cycle of the RC reciever.
    time.sleep(0.02)

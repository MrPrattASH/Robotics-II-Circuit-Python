import time
import board
import rc

rc = rc.RCReceiver(ch1=board.D10, ch2=board.D11, ch3=None, ch4=None, ch5=board.D12, ch6=board.D13)

# Main code
while True:
    # Read channels in a loop, iterating through our list 
    x = rc.read_channel(1)
    y = rc.read_channel(2)
    sw_b = rc.read_channel(5)
    sw_c = rc.read_channel(6)

    print("Ch 1:", x, "Ch 2:", y, "Ch 5:", sw_b, "Ch 6:", sw_c)
    # if you want to use the values, ensure you have this structure:
    '''
    if x is not None:
        print("do something")
    '''

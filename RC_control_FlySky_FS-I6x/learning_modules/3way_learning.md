# Reading a FlySky FS-i6x joystick

The RC signal is read from specific pins on a microcontroller, and the code then outputs the duty cycle value of the signal. We'll learn how to read our C Switch, or the Top Right switch of the controller. This is a simple 3 way switch that returns either `0`, `1`, or `2`. 

You'll see that much of the code is the same as the [2 way switch](2way_learning.md), the only difference is that we are reading a 3 way switch instead of a `0-1` switch. 

***

[Download the py file](3c_3way_switch.py)
```python

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
    channel_5 = rc.read_channel(6)
    if channel_5 is not None: # must not be None to do something with the output
        print("Channel 6:", channel_6)
    
    # sleep for 20ms at the end of our loop, the length of a single duty cycle of the RC reciever.
    time.sleep(0.02)

```

***

## Code Breakdown

Most of the code is the same as in the [2 way switch tutorial](2way_learning.md). If you've forgotten how to initilize the rc instance, the import statements, or what variables we are initiallizing, go back there now. 

### Main Code Loop
This is the main part of our script where we continuously read and print the values from the RC receiver.

```python

# Main code
while True:
    # Read channels
    channel_5 = rc.read_channel(6)
    if channel_5 is not None: # must not be None to do something with the output
        print("Channel 6:", channel_6)
    
    # sleep for 20ms at the end of our loop, the length of a single duty cycle of the RC reciever.
    time.sleep(0.02)

```

- **Reading Channels**: 
  - `channel_6 = rc.read_channel(6)`: Reads the value from channel 6, our Switch C (top right on the controller)
    - This will return either a `0` if the switch is off (down), a `1` if the switch is in the middle, or a `2` if the switch us all the way at the top

***

[Return to FlySky Tutorials to put it all together](../learning_modules/Fly_sky_learning.md)
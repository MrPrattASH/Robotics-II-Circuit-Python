# Reading a FlySky FS-i6x joystick

The RC signal is read from specific pins on a microcontroller, and the code then outputs the duty cycle value of the signal. We'll learn how to read our B Switch, or the Top Left switch of the controller. This is a simple 2 way switch that returns either off or on. 

You'll see that much of the code is the same as the [joystick learning](joystick_learning.md), the only difference is that we are reading a 2 way switch instead of a `0-100` analog joystick. 

***

[Download the py file](rc_2way_switch.py)
```python

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

```

***

## Code Breakdown

Most of the code is the same as in the [joystick tutorial](joystick_learning.md). If you've forgotten how to initilize the rc instance, the import statements, or what variables we are initiallizing, go back there now. 

### Main Code Loop
This is the main part of our script where we continuously read and print the values from the RC receiver.

```python

# Main code
while True:
    # Read channels
    channel_5 = rc.read_channel(5)
    if channel_5 is not None: # must not be None to do something with the output
        print("Channel 5:", channel_5)
    
    rc.ensure_cycle()  # Maintains sync with our 20ms cycle every loop iteration

```

- **Reading Channels**: 
  - `channel_5 = rc.read_channel(5)`: Reads the value from channel 5, our Switch B
    - This will return either a `0` if the switch is off (down) or a `1` if the switch is on (up)

***

[Return to FlySky Tutorials](../learning_modules/Fly_sky_learning.md)
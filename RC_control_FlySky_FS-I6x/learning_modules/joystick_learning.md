# Reading a FlySky FS-i6x joystick

The RC signal is read from specific pins on a microcontroller, and the code then outputs the duty cycle value of the signal. We'll first learn how to read our x2 joystick values. 
* Our joystick consists of x2 linear potentiometers
    * one for the X axis, channel 1
    * one for the y axis, channel 2
* We also have access to 2 more channels on 3/4 that are joysticks, but we won't use them for this course. 

***

[Download the py file](rc_joysticks.py)
```python

"""Basic RC Analog input Control
Outputs an analog channel duty cycle rating in 0>100.
50 is the deadpoint. 0 is miniumum, 100 is maximum.

"""

import time
import board
from rc import RCReceiver

rc = RCReceiver(ch1 = board.D0, ch2 = board.D1, ch3 = None, ch4 = None, ch5 =board.D2, ch6 =board.D3)

# Main code
while True:
    # Read channels
    channel_1 = rc.read_channel(1)
    channel_2 = rc.read_channel(2)
    if channel_1 is not None and channel_2 is not None: # must not be None to do something with the output
        print("1: ", channel_1, "2: ", channel_2)
    
    # sleep for 20ms, the length of a single duty cycle of the RC reciever.
    time.sleep(0.02)

```

***

## Code Breakdown

### Libraries

```python
"""
Basic RC Analog input Control
Outputs an analog channel duty cycle rating in 0 > 100.
50 is the deadpoint. 0 is miniumum, 100 is maximum.
"""
import time
import board
from rc import RCReceiver
```

- **`import time`**: Imports the `time` module, which allows us to work with time-related functions, such as delays.
- **`import board`**: Imports the `board` module, which maps the microcontroller's pins.
- **`from rc import RCReceiver`**: Imports the `RCReceiver` class from the `rc` module, allowing us to create an RC receiver object.

### Initializing the RCReceiver instance

The next section of the code initializes the RC receiver channels.

```python

rc = RCReceiver(ch1 = board.D0, ch2 = board.D1, ch3 = None, ch4 = None, ch5 =board.D2, ch6 =board.D3)
```

- **`rc`**: This is an instance of the `RCReceiver` class, which we will use to read the values from the RC receiver.
- **Channels**: `ch1` to `ch6` represent the input channels from the RC receiver. They are connected to specific pins (e.g., `board.D0`, `board.D1`, etc.).
    - Note, we ignore Channels 3/4, so we assign them a value of `None` so that the library will ignore these channels. 

### Main Code Loop
This is the main part of our script where we continuously read and print the values from the RC receiver.

```python

# Main code
while True:
    # Read channels
    channel_1 = rc.read_channel(1)
    channel_2 = rc.read_channel(2)
    if channel_1 is not None and channel_2 is not None: # must not be None to do something with the output
        print("1: ", channel_1, "2: ", channel_2)
    # sleep for 20ms, the length of a single duty cycle of the RC receiver.
    time.sleep(0.02)

```

- **Reading Channels**: 
  - `channel_1 = rc.read_channel(1)`: Reads the value from channel 1 (and 2 respectively)
  - This will return a value between `0-100`:
  - If joystick is in the middle: `50`
  - If the Joystick Channel 1 Left, or Channel 2 down: `0`
  - If the Joystick Channel 1 Right or Channel 2 Up: `100`
- **Check for None**: 
  - `if channel_1 is not None and channel_2 is not None`: Ensures that both channels have valid readings before proceeding. If there is ever an error in reading a channel, the method will return `None`. 
- **Delay**:
  - `time.sleep(0.02)`: Pauses the loop for 20 milliseconds. This matches the length of a single duty cycle of the RC receiver, ensuring the code reads the next cycle's data. 
  - We *always* have to put a single 0.20ms sleep at the end of our `while True:` loop in order to keep our readings in sync with our duty cycle. 


***

[Return to FlySky Tutorials](../learning_modules/Fly_sky_learning.md)
# CircuitPython - FlySky FS-I6X Controller - FS-iA6B Reciever
This page will show you how to use the rc.py library for controlling a FlySky FS-i6(X) controller with an FS-iA6B reciever in circuitpython. 

## Tutorials
* [Transmitter & Receiver Wiring/Controls](fly_sky_wiring.md)
* [Reading Joystick Tutorial](joystick_learning.md)
* [Reading 2way Switch Tutorial](2way_learning.md)
* [Reading 3way Switch Tutorial](3way_learning.md)

***

## Library Documentation (Putting it all together)
* **Before putting this all together below, ensure you have done all 4 tutorials above.**
* Ensure you have added the [rc.py](../rc_module/rc.py) file to your `CIRCUITPY` lib folder. 

***

### Program Breakdown

py file [here](../rc_module/rc_example.py)

```python
import time
import board
from rc import RCReceiver

# Initialize the receiver with designated pins for channels
rc = RCReceiver(ch1=board.D10, ch2=board.D11, ch3=None, ch4=None, ch5=board.D12, ch6=board.D13)

# List of channel numbers we are interested in
channels = [1, 2, 5, 6]

# Variables to store the values read from each channel
x = 0
y = 0
sw_b = 0
sw_c = 0

# Main code loop
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
                
    # Print the channel values to the console
    print("Ch 1:", x, "Ch 2:", y, "Ch 5:", sw_b, "Ch 6:", sw_c)
    
    rc.ensure_cycle()  # Maintains sync with our 20ms cycle every loop iteration

```


### Importing Libraries



```python

import time
import board
from rc import RCReceiver
```



- `import time`: This library allows us to use time-related functions, like pauses.
- `import board`: This library provides pin definitions for the hardware.
- `from rc import RCReceiver`: We import the `RCReceiver` class from a custom `rc` module. This class will help us interface with the RC receiver.



### Initializing the Receiver



```python

rc = RCReceiver(ch1=board.D10, ch2=board.D11, ch3=None, ch4=None, ch5=board.D12, ch6=board.D13)
```

We create an instance of `RCReceiver` and assign specific microcontroller pins (D10, D11, D12, D13) to the receiver channels 1, 2, 5, and 6 respectively. Channels 3 and 4 are not being used (the left side of our controller with the 6 section transmission), hence they are set to `None`. 



### Init Variables



```python

channels = [1, 2, 5, 6]
```

A list is a collection of items that can be of any data type. Lists in Python are ordered, changeable, and allow duplicate values. while a variable is typically only 1 value, you can think of a list as a group or collection of variables that we can access.

This list contains the number of the channels we will be reading data from. 

```python

x = 0
y = 0
sw_b = 0
sw_c = 0
```



We initialize variables `x`, `y`, `sw_b`, and `sw_c` to store the values read from channels 1, 2, 5, and 6 respectively. Their values relate to the axis they are reading on our joystick, or the switch at the top of the controller. 

***

### While Loop

```python

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
```

- `for i in range(len(channels)):`: This loop iterates over the indices of the `channels` list. `range(len(channels))` generates a sequence of numbers from 0 to the length of the `channels` list minus one.
- `channels[i]`: Accesses the current channel number in the loop.
- `rc.read_channel(channels[i])`: Reads the value of the current channel.



We then check if `channel_value` is not `None` and update the corresponding variables (`x`, `y`, `sw_b`, `sw_c`) based on which channel was read.



### Print Statement



```python

print("Ch 1:", x, "Ch 2:", y, "Ch 5:", sw_b, "Ch 6:", sw_c)
```



The `print` statement outputs the values of channels 1, 2, 5, and 6 to the serial console. 


### Sleep Function



```python

rc.ensure_cycle()  # Maintains sync with our 20ms cycle every loop iteration

```



Finally, `rc.ensure_cycle()  # Maintains sync with our 20ms cycle every loop iteration` ensures that our loop follows a 20ms delay cycle. This delay matches the length of a single duty cycle of the RC receiver, ensuring smooth and accurate readings. 

You **must** ensure your cycle at the end of each while True loop, or your RC reading cycles will be out of phase with the sent signals from the RC transmitter. 



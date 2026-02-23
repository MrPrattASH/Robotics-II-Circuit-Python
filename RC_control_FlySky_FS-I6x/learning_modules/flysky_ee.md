# CircuitPython - FlySky FS-I6X Controller - FS-iA6B Reciever
This page will show you how to use the rc.py library for controlling a FlySky FS-i6(X) controller with an FS-iA6B receiver in circuitpython. 

In this course, we'll use an RC controller to be able to control our robot to drive around. You must complete the activities as you watch! *While You are not required to understand this program, it is beneficial to understand the init statements to be able to change the correct Digital ports*

By the end of this lesson, you will have successfully wired an RC receiver to your microcontroller, and be able to move joysticks around to discover how different readings work from the flysky controller via the serial console. 

You have x2 choices here. 
1: Watch the video tutorial OR
2: Complete the text based tutorial below 

***

# Video Tutorial

{% include youtube.html id="Ix4YrCbWJ3o?t=17" %}

If watching the video tutorial, you can use the following code below. 
***

# Text Tutorial

## Library Instillation
* Ensure you have added the [rc.py](../../circuit_python_libraries/lib/rc.py) file to your `CIRCUITPY` lib folder. 
* 
1. click the above rc.py file to download. 
2. With your finder window open, Drag and drop this rc.py file into the CIRCUITPY/lib folder
3. If it asks you to replace any file, yes, replace the file. 

***

### Program Breakdown (Simplified)

```python
import time
import board
from rc import RCReceiver

# Initialize the receiver with designated pins for channels
rc = RCReceiver(ch1=board.D10, ch2=board.D11, ch3=None, ch4=None, ch5=board.D12, ch6=board.D13)


# Main code loop
while True:
    x = rc.read_channel(1)
    y = rc.read_channel(2)
    ch5 = rc.read_channel(5)
    ch6 = rc.read_channel(6)
                
    # Print the channel values to the console
    print("Ch 1:", x, "Ch 2:", y, "Ch 5:", ch5, "Ch 6:", ch6)

    time.sleep(0.02) # add a minor sleep to keep in time with PWM cycle

```

*** 

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

x = 0
y = 0
ch5 = 0
ch6 = 0
```



We initialize variables `x`, `y`, `sw_b`, and `sw_c` to store the values read from channels 1, 2, 5, and 6 respectively. Their values relate to the axis they are reading on our joystick, or the switch at the top of the controller. 

***

### While Loop

```python

x = rc.read_channel(1)
y = rc.read_channel(2)
ch5 = rc.read_channel(5)
ch6 = rc.read_channel(6)
```


- `rc.read_channel(channels[i])`: Reads the value of the current channel.



We then check if `channel_value` is not `None` and update the corresponding variables (`x`, `y`, `sw_b`, `sw_c`) based on which channel was read.



### Print Statement



```python

print("Ch 1:", x, "Ch 2:", y, "Ch 5:", ch5, "Ch 6:", ch6)
```



The `print` statement outputs the values of channels 1, 2, 5, and 6 to the serial console. 

*** 

## Individual Component Tutorials
If you're interested in how all these individual components work, check out these tutorials. 
* [Transmitter & Receiver Wiring/Controls](fly_sky_wiring.md)
* [Reading Joystick Tutorial](joystick_learning.md)
* [Reading 2way Switch Tutorial](2way_learning.md)
* [Reading 3way Switch Tutorial](3way_learning.md)



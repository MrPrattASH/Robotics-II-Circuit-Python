# Arcade Drive (DC Motors) 

The goal of this lesson is to teach you how to wire up your rover to be able to run in RC mode. You will have to:
1. Wire the FlySky RC controller
2. Wire the Motor controller for powering the drive motors
3. Run the attached program to make your rover RC controlled! 

## Controlling Rovers

There are two classic ways of controlling a 2 or 4 wheeled rover that has a tank drive drivetrain. 

From [xiaoxiae on Github](https://xiaoxiae.github.io/Robotics-Simplified-Website/drivetrain-control/tank-drive/):

Tank drive is a method of controlling the motors of a tank drive drivetrain using two axes of a controller, where each of the axes operate motors on one side of the robot. 

![tank](tank-drive.png)

In contrast, Arcade drive is a method of controlling the motors of a tank drive drivetrain using two axes of a controller, where one of the axes controls the speed (throttle) of the robot, and the other the steering (spin) of the robot.

![arcade](arcade-drive.png)

---

### Rover Setup
Your rover needs the following hardware:
- Flysky receiever
- x2 DC motors OR x4 DC motors connected via y Splitter
- RoboClaw Motor Controller (2x30A recommended)

# Video Tutorial

Watch the following video and follow along with the wiring to get your rover prepared for RC control. 

{% include youtube.html id="AsT0ODlqZmo" %}

---

Wiring Diagram (sans 9V batter pack for microcontroller power) 

![23](drive_motors.png)

# Text Tutorial

### Required Libraries

Before moving forward, ensure you have the following [arcade_drive_dc.py](arcade_drive_dc.py) and [rc.py](../../circuit_python_libraries/lib/rc.py) py files on your `CIRCUITPY` lib folder.

---

## Example Code

```python
import time
import board
from rc import RCReceiver
from arcade_drive_dc import Drive

rc = RCReceiver(ch1=board.D0, ch2=board.D1, ch3=None, ch4=None, ch5=board.D2, ch6=board.D3)
drive = Drive(left=board.D10, right=board.D11)

# Main code
while True:
    # Read joystick channels
    spin = rc.read_channel(1) # spin
    throttle = rc.read_channel(2) # throttle

    if spin is not None and throttle is not None: # must not be None to do something with the output
        drive.drive(spin,throttle) # move our motors arcade drive style


    time.sleep(0.02) # keep timer in sync with flysky receiver

```

## Code Breakdown

Again, while it is not necessary for you to understand this code, a rudimentary understanding of what is happening is useful for the course. 

### Importing Necessary Libraries

```python

import board
import time
from rc import RCReceiver
from arcade_drive_dc import Drive
```

- **board**: This library provides board-specific constants to specify pins used for input and output. It's essential to identify which pins on the board connect to devices.
- **time**: This library allows us to use time-related functions, especially `sleep`.
- **RCReceiver** and **Drive**: These are imported from custom modules. `RCReceiver` is used to handle the input from the RC receiver, while `Drive` is used to control the driving mechanism of the robot.

### Setting Up the RC Receiver and Drive

```python
rc = RCReceiver(ch1=board.D10, ch2=board.D11, ch3=None, ch4=None, ch5=board.D12, ch6=board.D13)
drive = Drive(left=board.D0, right=board.D1)
```

- The **RCReceiver** is initialized with different channels corresponding to different board pins. 
- The **Drive** is set up with pins controlling the left and right DC motors. 
    - The pwm motor objects are initialized in the library itself, not in your `code.py` file. 

### Main Code Loop

The code enters an infinite loop, constantly checking for input from the RC receiver and updating the drive system accordingly.

```python
while True:
    # Read joystick channels
    spin = rc.read_channel(1)  # spin
    throttle = rc.read_channel(2)  # throttle

    if spin is not None and throttle is not None:  # Ensures valid input
        drive.drive(spin, throttle)  # Moves the motors based on input
    print("spin", spin, "throttle", throttle)  # Displays the current input values

    time.sleep(0.02) # Maintains sync with our 20ms cycle every loop iteration
```

- **Reading Channels**: The code reads channel 1 for `spin` and channel 2 for `throttle` to get joystick input.
- **Checking Inputs**: It checks if the inputs are not `None` (meaning valid and connected inputs).
- **Driving Motors**: If valid data is read, the `drive` function is called to control the motors according to the joystick's direction and throttle.
- **Print Statement**: This outputs the current values of `spin` and `throttle` to the console for debugging purposes.
- **Delay**: A short delay of 20-40 ish milliseconds is added to match the RC receiver's duty cycle and avoid overwhelming the processor with too many instructions in a short period.

## Conclusion

This code effectively allows for controlling a robot using an RC receiver and DC motors. It's crucial to ensure that the pins and channels are correctly configured to match your hardware setup.

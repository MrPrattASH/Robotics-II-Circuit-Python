# Arcade Drive (Servo Motors)

By the end of this tutorial, you will have a fully RC controlled rover! 

--- 

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
- x2 motors, orientated in tank drive where x1 of the motor sides in inverted/mirrored
    - These motors can be either Servo motors OR DC Motors, depending on your needs


### Required Library

Before moving forward, ensure you have the following [arcade_drive.py](../../circuit_python_libraries/lib/arcade_drive.py) and [rc.py](../../circuit_python_libraries/lib/rc.py) py files on your `CIRCUITPY` lib folder.

---

## Example Code

```python
import time
import board
from rc import RCReceiver
from arcade_drive import Drive

# Initialize the receiver with designated pins for channels
rc = RCReceiver(ch1=board.D0, ch2=board.D1)
robot = Drive(motor_type="servo", left_pin=board.D4, right_pin=board.D5, scale = 1.0)
# if you find your driving too fast, try dropping DOWN the scale. 

# Main code loop
while True:
    spin = rc.read_channel(1)
    throttle = rc.read_channel(2)
    ch5 = rc.read_channel(5)
    ch6 = rc.read_channel(6)

    # Print the channel values to the console
    print("Ch 1:", spin, "Ch 2:", throttle, "Ch 5:", ch5, "Ch 6:", ch6)
    robot.drive(spin, throttle)

    time.sleep(0.02) # add a minor sleep to keep in time with PWM cycle

```
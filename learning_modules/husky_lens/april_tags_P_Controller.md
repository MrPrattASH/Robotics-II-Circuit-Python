# Simple Proportional (P) Controller for Auto Centering on April Tags

Now that we can identify April tags, let's create a simple proportional controller (P controller). **Our goal is to make our future robot center itself on a detected tag.** For now, we'll start by calculating a theoretical "motor value" and printing it to the screen. Then, we'll connect a single servo to see our code create a physical output.

The logic is simple: the further the tag is from the center of the screen, the faster the motor should turn to correct the error. The motor value will be between -1.0 (full speed one way) and 1.0 (full speed the other way), with 0.0 being stationary.

The screen resolution is 320x240 pixels, with the origin (0,0) at the top-left corner. 

![husky](images/coordinates.png)

This means the center of the X-axis is `160`. We'll also include a small "deadzone," or margin of error, so the robot considers itself "centered" when the tag's X value is within 5~ pixels of this center point. (We may need to tune this dead zone later if it's too large or small). 

## Step 1: Visualizing the P Controller Output

First, let's just print the calculated motor value. This will help you understand how the P controller works without needing any extra hardware. You will simply hold the HuskyLens and move it left and right in front of an April Tag.

### The Logic

A proportional controller's output is *proportional* to the error. The further we are from our goal or target, the greater our error, and proportionally, the greater we should try to correct our error. 

*Far away? Move fast. Close? Move slow.* 

1.  **Calculate the Error**: We measure how far the detected tag's center `x` coordinate is from the screen's center (`160`). This difference is our "error".
    *   `error = 160 - block.x`
2.  **Apply Proportional Gain (Kp)**: We multiply this error by a constant, known as the proportional gain (`Kp`). This is a tuning value. A higher `Kp` results in a more aggressive response, while a lower `Kp` is gentler. You are responsible for manually tuning your P value! 
3.  **Clamp the Output**: We'll make sure our final motor value is always between -1.0 and 1.0, as this is a standard range for servo motors. We don't want to send 2.0, for example, as this would be ignored. 

### Code for Visualization

Add the following constants and function to your code. The main loop is updated to call this function and print the results.

```python
import board
from circuitPyHuskyLib import HuskyLensLibrary
import time

# create our husky lens object
hl = HuskyLensLibrary("I2C", SCL=board.SCL, SDA=board.SDA)
time.sleep(1)
hl.algorithm("ALGORITHM_TAG_RECOGNITION")

# P Controller constants
SCREEN_CENTER_X = 160
P_GAIN = 0.01  # This is our Kp value, you'll need to tune this later
DEADZONE_PIXELS = 5 # The margin of error in pixels

def calculate_motor_output(block_x):
    """
    Calculates a motor output value between -1 and 1.
    Returns 0 if the tag is within the deadzone.
    """
    error = SCREEN_CENTER_X - block_x

    # If the tag is close enough to the center, do nothing.
    if abs(error) <= DEADZONE_PIXELS:
        motor_value = 0
    else:
        motor_value = error * P_GAIN

        # Clamp the motor value to be between -1 and 1
        if motor_value > 1:
            motor_value = 1
        elif motor_value < -1:
            motor_value = -1

    return motor_value

# --- Main Loop ---
while True:
    results = hl.learnedBlocks()

    if results:
        first_tag = results[0] # grab the first tag for now
        
        motor_speed = calculate_motor_output(first_tag.x)

        print("--------------------")
        print(f"Tag X: {first_tag.x}")
        print(f"Error: {SCREEN_CENTER_X - first_tag.x}")
        print(f"Motor Output: {motor_speed:.2f}")
    else:
        print("Motor Output: 0") # no tags found

    time.sleep(0.05) # A shorter delay for more responsive control
```

Run this code. Now, point your HuskyLens at a learned April Tag.
-   When the tag is on the **right** side of the screen, you should see a **negative** motor output.
-   When the tag is on the **left** side of the screen, you should see a **positive** motor output.
-   Notice how the value gets larger the further you move the tag from the center!

## Step 2: Adding a Physical Output with a Servo

Now let's translate that abstract printed number into motion. We will connect a continuous rotation servo to act as our "motor". This same logic will later be applied to the drive motors on our autonomous rover.

You'll need to install the appropriate library for your microcontroller to control a servo. For CircuitPython, this is often the `adafruit_motor` library.

### Code for Servo Control

Attach a continuous servo to pin D0. Feel free to power this either by the board 5V, or via a servo PDB board. 

We'll add to our previous code: 

```python
import board
from circuitPyHuskyLib import HuskyLensLibrary
import time
import pwmio
from adafruit_motor import servo

# --- Servo Setup ---
pwm = pwmio.PWMOut(board.D1, frequency=50)
my_servo = servo.ContinuousServo(pwm)


# --- P Controller constants and function from before ---
SCREEN_CENTER_X = 160
P_GAIN = 0.01
DEADZONE_PIXELS = 5

def calculate_motor_output(block_x):
    # (this function is identical to the one in the previous step)

    """
    Calculates a motor output value between -1 and 1.
    Returns 0 if the tag is within the deadzone.
    """
    error = SCREEN_CENTER_X - block_x

    # If the tag is close enough to the center, do nothing.
    if abs(error) <= DEADZONE_PIXELS:
        motor_value = 0
    else:
        motor_value = error * P_GAIN

        # Clamp the motor value to be between -1 and 1
        if motor_value > 1:
            motor_value = 1
        elif motor_value < -1:
            motor_value = -1

    return motor_value

# create our husky lens object
hl = HuskyLensLibrary("I2C", SCL=board.SCL, SDA=board.SDA)
time.sleep(1)
hl.algorithm("ALGORITHM_TAG_RECOGNITION")


# --- Main Loop ---
while True:
    results = hl.learnedBlocks()

    if results:
        first_tag = results[0]
        motor_speed = calculate_motor_output(first_tag.x)
        print(f"Tag X: {first_tag.x}, Servo Throttle: {motor_speed:.2f}")

    else:
        motor_speed = 0 # Stop the servo if no tag is seen
        print("No tag detected. Servo stopped.")

    my_servo.throttle = motor_speed # control motors at the END of the loop
    time.sleep(0.05)
```

## Step 3: Tuning Your Controller

With the servo connected, run the code again. You should now see the servo turn in response to the tag's position. Now comes the MOST IMPORTANT PART: **tuning**.

The `P_GAIN` value directly impacts performance. It is a roboticist's job to tune the P value on a P controller (and to be honest, this is where a LOT of time is spent). Try changing it to see what happens.

-   **If `P_GAIN` is too low (e.g., `0.0005`)**: The servo will react very slowly and weakly. It might not even move much until the tag is far from the center.
-   **If `P_GAIN` is too high (e.g., `0.5`)**: The servo will be very fast and twitchy. It will react aggressively to even small movements. When we apply this to a real robot, a `P_GAIN` that is too high will cause it to overshoot the target and oscillate back and forth, never settling down.

Experiment with different `P_GAIN` values to find a "sweet spot" where the servo's response feels smooth and controlled. This tuning process is a fundamental part of robotics, and getting a feel for it now will be invaluable for your future rover project.
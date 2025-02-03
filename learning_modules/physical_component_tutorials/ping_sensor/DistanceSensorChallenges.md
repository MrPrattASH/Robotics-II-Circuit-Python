# Distance Sensor Challenges
Lets get more practice using a distance sensor on our rover: 

## Challenge 1: Basic Obstacle Detection

### Objective
Stop the rover when an obstacle is detected using the distance sensor.

### Instructions
1. Connect the distance sensor to your microcontroller 
2. Write a program that reads the sensor data continuously in a while True Loop.
3. If an object is detected closer than a set threshold (e.g., 20 cm), stop the rover.

### CircuitPython Code Snippet
```python
import time
import board

# Initialize the distance sensor

# Function to control your rover motors
def stop_rover():
    # Code to stop the rover's motors
    pass

def move_forward():
    # Code to move the rover forward
    pass

try:
    while True:
        #read distance sensor

        if distance < 20:  # Threshold in cm
            stop_rover()
        else:
            move_forward()

        time.sleep(0.1)
```

---

## Challenge 2: Distance Feedback LED

### Objective
Use an LED to visually indicate when an object is detected within a threshold.

### Instructions
1. Use the onboard LED on your microcontroller. 
2. Turn on the LED when an object is detected within the set threshold distance.

---

## Challenge 3: Simple Back-and-Forth Navigation

### Objective
Make the rover move forward until it detects an obstacle, then reverse for a short period.

### Instructions
1. Use the distance sensor to detect obstacles.
2. Move forward until an obstacle is within a threshold distance.
3. Reverse the rover for 2 seconds when an obstacle is detected.
4. Rotate the rover 90* Left
5. Repeat. 

### CircuitPython Code Snippet
```python
def reverse_rover():
    # Code to reverse the rover
    pass

def turn_rover():
    # code to turn rover 90*
    pass

try:
    while True:
        distance = sonar.distance
        print("Distance:", distance)

        if distance < 20:
            stop_rover()
            time.sleep(0.5)
            reverse_rover()
            time.sleep(2)  # Reverse for 2 seconds
            stop_rover()
            turn_rover()
        else:
            move_forward()

        time.sleep(0.1)

```
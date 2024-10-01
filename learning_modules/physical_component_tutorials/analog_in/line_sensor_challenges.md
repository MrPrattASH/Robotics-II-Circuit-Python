# Line Sensor Challenges (Mars Rover)

Let's get some more practice with line sensors with a variety of challenges

---

## 1. Handling False Readings

Line sensors are sensitive to light conditions. Changes in ambient light (shadows or brighter sun) can effect the line sensor's reading. Glossy vs matte surfaces also affect things. This is why our sumo ring is painted matte white in the middle with a matte black ring on the outside. However, lifting a sensor off the ground can also cause false readings. Let's try to stop these false readings. 

1. Write a simple program that:
    - Reads the line sensor & map this to a range of 0>100
    - prints the output
    - sleeps 0.1s. 
2. Attach the line sensor to your rover so that it is placed as close as possible to the battle field. 
    - Wire:
    - x2 rotational servos
    - x1 line sensor
    - Optional: DEBUG LED x3
3. Without your motors on, move your rover around the battlefield and observe the serial outputs. Ensure you test, at minimum, x3 different spots of each condition. Note your observations of values returned in your engineering journal: 
    - White surface
    - Black surface
    - Line sensor lifted off the battlefield (placed in the air) by 1cm
    - Line sensor lifted off the battlefield (placed in the air) by at least 3cm
4. Using the values discovered, modify the following pseudocode to create 3 possible outputs in your print.
    - Your sensor is on black
    - Your sensor is on white
    - Your sensor is in the air
*Note: We can use an `and` statement to combine 2 separate conditions into one statement. In our case, we're checking that a variable is in between 2 values*

```python
# ... initialize sensor & library imports

def mapped_voltage(pin):
    # Maps our current 0-65535 range to 0-100
    mapped_value = map_range(pin.value, 0, 65535, new_min, new_max)
    return floor(mapped_value)

# ----------- INIT VARIABLES --------------
black_min = 70  # change to minimum observed reading for black
white_max = 50  # change to maximum observed reading for white
air_min = 51  # change to minimum observed reading for in the air
air_max = 69  # change to minimum observed reading for in the air

while True:
    line_sensor = mapped_voltage(line_pin)  # replace with your init sensor

    if line_sensor > black_min:
        print("on black line!")
        # consider turning on debug LED 1 here
    elif line_sensor < air_min and line_sensor > air_max:
        print("lifted up in the air!")
        # consider turning on debug LED 2 here
    else:
        print("we're on white!")
        # consider turning off all LEDs here
    time.sleep(0.02)
```

---

## 2. Anti-Fall Rover
Now that you have the basics of handling false positive readings in the air, let's make a rover that stays on the platform. 

1. Modify the following code so the rover:
    - Moves forward on white or in the air
    - Stops, backs up, and turns 180* on black
    - Do NOT use sleeps in your move forward code. 

```python 
# ...

while True:
    line_sensor = mapped_voltage(line_pin)  # replace with your init sensor

    if line_sensor > black_min:
        print("on black line!")
        # stop
        # back up
        # turn 180* 
    elif line_sensor < air_min and line_sensor > air_max:
        print("lifted up in the air!")
        # consider turning on debug LED 2 here
        # move forward
    else:
        print("we're on white!")
        # consider turning off all LEDs here
        # move forward
    time.sleep(0.02)
```
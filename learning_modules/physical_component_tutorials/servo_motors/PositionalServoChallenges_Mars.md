# Positional Servo Challenges (Mars Rovers)
Lets get more practice using positional servos

---

## 1. Modifying the sweep code sleep time

Lets take our sweep code and modify it a bit to further discover the differences between a straight set angle, and a sweep. Run both the sweep and basic angle sets in your while True loop. Attach a single servo (positional) to your breadboard and try the following:

```python
#... init statements & servo setup

while True:
    # basic angles
    print("basic angles")
    my_servo.angle = 0 # set the servo to 0 Degrees, the min point
    time.sleep(1)
    my_servo.angle = 90 # set the servo to 90 Degrees, the midpoint
    time.sleep(1)
    my_servo.angle = 180 #set the servo to 180 Degrees, the max point
    time.sleep(1)

    print("sweeps")
    for angle in range(0, 180, 5):  # "sweep" 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # "sweep" 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
```

* Try to increase or decrease the sleep time inside the `for angle in range` loops. At what point to you notice a difference between a servo sweep, versus a straight angle? How low can you make the sleep occur to notice a difference? 

--- 

## 2. Modifying the sweep code angle change

This time, rather than changing our sleep value, we'll change our angle value each iteration of the loop. 

```python
for angle in range(0, 180, 5):  # "sweep" 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # "sweep" 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
```

* In the `for angle in range(0,180,5)` section of the loop, you've likely been noticing that our angle is increasing by 5 each iteration. 
* Rather than changing our sleep value, now change our angle each loop. At what point is the movement the *smoothest*? At what point is the movement so slow you barely notice a change? 
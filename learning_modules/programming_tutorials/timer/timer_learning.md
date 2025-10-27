# Creating a Simple Timer Using CircuitPython

This tutorial will guide you through creating a simple timer in CircuitPython using the `Timer` module. We will create a basic timer functionality that runs for a specific period (like 10 seconds) before notifying the user that the time has elapsed.


## Libraries
Ensure you have the [`timer.py`](timer.py) file on your `CIRCUIT.PY` lib folder. 

---

# Code

```python
import time
from timer import Timer

# Create an instance of the Timer
timer = Timer()

# Setting a timer for 10 seconds
timer.set_timer(time.monotonic(), time.monotonic() + 10)

# Continuously checks if the timer has ended
while True:
    # Check the timer status
    timer_end = timer.check_timer()
    
    # Provide feedback based on the timer status
    if timer_end:
        print("Timer reached!")
        break
    else:
        print("Timer still running")
    
    # Wait half a second before checking again
    time.sleep(0.5)
```

## Code Breakdown

- **Imports**: This script uses `time` from CircuitPython and a `Timer` object from a custom or external module named `timer`. 
- **Initialize Timer**: `timer = Timer()` initializes the Timer instance.
- **Set Timer**: `timer.set_timer(start_time, end_time)` sets the timer for 10 seconds using CircuitPython's `time.monotonic()`.
    - time.monotonic() is a function in Python that returns the current value of a monotonic clock, which is a clock that cannot go backwards. It tracks the number of seconds from the time the board has turned on until the current moment in time. This is particularly useful in situations where you need to measure elapsed time accurately and want to avoid issues with changes in time.sleep() values, which will pause our code. 
    - time.monotonic() allows us to have non breaking timers functioning in our program. 
- **Check Timer**: In the continuous loop, `timer.check_timer()` is called to see if the timer has reached the set time. If true, it prints "Timer reached!" otherwise it informs you that the timer is still running.
- **Loop Control**: Using `time.sleep(0.5)` ensures the loop checks the timer every half-second, preventing excessive CPU usage.


### Experiment

Try changing the `timer.set_timer()`'s second argument to see how the duration affects the output timing. For example, change `time.monotonic() + 10` to `time.monotonic() + 5` for a shorter duration.
"""

---

## Initializing Multiple Non-Breaking Timers

We can also have multiple timers created with multiple instances. Let's assume we have a robot with x2 continuous servo actuators. 
- The first servo controls an intake that rotates for 2 seconds. 
- The second controls a catapult launching mechanism that rotates for 4 seconds. 
For example (note, I'd excluded all most motor import statements for ease of understanding):

```python
...
intake_timer = Timer()
catapult_timer = Timer()

intake_timer.set_timer(time.monotonic(), time.monotonic()+2)
catapult_timer.set_timer(time.monotonic(), time.monotonic()+4)

while True:
    intake_end = intake_timer.check_timer()
    catapult_end = catapult_timer.check_timer()

    if intake_end:
        print("Intake done!")
    else:
        print("intake still running!")
    
    if catapult_end:
        print("catapult done!")
    else:
        print("catapult still running!")


```

### Experiment
Now you try. Create multiple timers, 1 for a door that runs for 5 seconds, and another for an elevator that runs for 8 seconds. 

---

## Restarting timers
You can also restart timers throughout the while true loop. Let's assume you have a 2 second timer, and every time you flick the switch on your RC reciever on channel 5, you restart the timer. 

```python
feeder_timer = Timer()
feeder_timer_end = false

while True:
    now = time.monotonic() #get current time
    ch5 = rc.read_channel(5)
    feeder_timer_end = feeder_timer.check_timer()

    if ch5 == 1:
        feeder_timer.set_timer(now, now + 2) # start a 2 second timer
        print("reset timer!")
    else:
        if feeder_timer_end:
            print("Timer done!")

```

### Experiment
Create x2 timers. 
- 1 timer that lasts 2 seconds. 
- 2nd timer that lasts 4.8 seconds. 
- Each time the 2nd timer elapses, have this reset the 1st timer. 

---

## Servo Sweep Timers
Sometimes you'll find it useful to set up a timer for a servo sweep, so as to not interupt the rest of your code. The following code below assumes we have a robot that:
- Is controlled via RC in a tank drive orientation
- has a forklift arm attached to a positional servo
- has a distance sensor.
 
Robot Goal: If an object gets within 10cm of the robot, the forklift should lift up, else, the forklift should return to rest (angle 0). 
- We want to smoothly lift up the object, so that our load stays secured. 
- We want to be able to drive around while we are lifting up our object. 

See if you can see the problem with this code:

```python

while True:
    distance = distance_sensor.get_distance(prev_distance)
    throttle = rc.read_channel(1)
    spin = rc.read_channel(2)
    
    if distance < 10: #lift up arm if we get too close
        for i in range(0,90,5):
            forklift.angle = i
            time.sleep(0.5) 
    else: #return the arm to rest
        forklift.angle = 0

    drive.drive(spin, throttle) # call drive motors

    prev_distance = distance
    time.sleep(0.2) # small sleep to stay in time with RC flysky controller
    
```

This program want's to read distance every loop. As you can see, when our distance is <10cm, the code inside our `for loop` activates, and this causes our code to pause for **9 full seconds!** (18 steps in the loop at 0.5 seconds each). This means that our robot's drive motors will remember their last command, and we won't be able to drive for a full 9 seconds! Obviously not ideal. Let's correct this using our non-breaking timer. 

### Experiemnt
See if you can find a solution first, then take a look at my example. 

My solution is below. 

<details>
 <summary>hint #1</summary>
<pre><code>
# I've used the following timers and variables to keep track of my loop

forklift_timer = Timer() # track the full sweep loop time
sweep_timer = Timer() # track individual sweep steps

forklift_sweep_end_angle = 90 # last number in our for loop
forklift_sweep_step = 5 # step value from for loop
forklift_sweep_sleep = 0.5 # sleep value in each loop iteration
forklift_sweep_full_timer = (forklift_sweep_end_angle / forklift_sweep_step) * forklift_sweep_sleep # total time needed for a sweep to complete

forklift_angle = 0 # initial angle

forklift_start = False # boolean to track if our loop has started
</code></pre>
</details>

<details>
 <summary>hint #2</summary>
<pre><code>
# Here;s the start of my while true loop 
while True: 
    now = time.monotonic()
    distance = distance_sensor.get_distance(prev_distance)
    throttle = rc.read_channel(1)
    spin = rc.read_channel(2)

    if distance < 10 and not forklift_start: #lift up arm if we get too close
        forklift_start = True
        forklift_timer.set_timer(now, now + forklift_sweep_full_timer)
        sweep_timer.set_timer(now, now + forklift_sweep_step)
    else: #return the arm to rest
        forklift_angle = 0
        forklift_start = False
    
    if forklift_start:
        # what would you do here? 
</code></pre>
</details>

<details>
 <summary>Click to reveal my solution</summary>
<pre><code>
while True:
    now = time.monotonic()
    distance = distance_sensor.get_distance(prev_distance)
    throttle = rc.read_channel(1)
    spin = rc.read_channel(2)
    
    if distance < 10 and not forklift_start: #lift up arm if we get too close
        forklift_start = True
        forklift_timer.set_timer(now, now + forklift_sweep_full_timer)
        sweep_timer.set_timer(now, now + forklift_sweep_step)
    else: #return the arm to rest
        forklift_angle = 0
        forklift_start = False
    
    if forklift_start:
        sweep_end = forklift_timer.check_timer()
        sweep_step_end = sweep_timer.check_timer()

        if sweep_end:
            forklift_angle = forklift_sweep_end_angle
        else:
            if sweep_step_end:
                forklift_angle += 5 # add 5 to sweep angle
                sweep_timer.set_timer(now, now + forklift_sweep_step)



    drive.drive(spin, throttle) # call drive motors

    forklift.angle = forklift_angle # tell our servo what angle to go to once per loop. 
    prev_distance = distance
    time.sleep(0.2) # small sleep to stay in time with RC flysky controller
</code></pre>
</details>





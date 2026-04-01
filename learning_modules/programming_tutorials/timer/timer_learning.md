# Creating a Simple Timer Using CircuitPython

This tutorial will guide you through creating a simple timer in CircuitPython using the `ElapsedTime` class. Instead of pausing your entire program, we will use this class to track how much time has passed since a specific event, allowing your robot to stay responsive to sensor commands, etc. 

We'll also learn how to combine multiple state machines into a single robot, so we can "do 2 things at once" 

### Why Use "Elapsed Time" over Time.sleep()? 

* Using `time.sleep()` is like playing a game of "Red Light, Green Light" where you have to close your eyes and cover your ears every time you wait for something to happen. 
* If your robot is driving toward a wall and you tell it to `sleep` for two seconds while it moves a motor, the robot becomes "blind" and "deaf" during that time—it can't check its sensors to see the wall, and it can't hear your remote control telling it to stop! 
* A non-breaking timer like `ElapsedTime` is like having a stopwatch strapped to the robot's wrist. It lets the robot keep its "eyes" open and its "hands" on the steering wheel while it simply glances at the watch to see if enough time has passed. This way, your robot never stops thinking, meaning it can move its arm and steer around an obstacle at the exact same time.

---

## Libraries
Ensure you have the [`elapsed_time.py`](../../../circuit_python_libraries/lib/elapsed_time.py) file in your `CIRCUIT.PY` lib folder. 

---

# 1. Example Code

```python
import time
from elapsed_time import ElapsedTime

# Create an instance of the ElapsedTime class
timer = ElapsedTime()

# ALWAYS reset your timer before your loop begins so that we have a fresh "start point" from 0. 
timer.reset()
while True:
    # Check if the elapsed seconds are greater than 10
    if timer.seconds() > 10:
        print("Timer reached!")
        break
    else:
        # Show the time that's elapsed since reset. 
        print("Timer still running: ", timer.seconds())
    
    # Wait half a second before checking again
    time.sleep(0.5)

print("The timer is now done, so we've broken out of the loop")
```

## Code Breakdown

- **Imports**: This script uses `time` from CircuitPython and the `ElapsedTime` class from our library. 
- **Initialize Timer**: `timer = ElapsedTime()` initializes the instance and records the current time as the starting point.
- **Checking Time**: `timer.seconds()` returns a float representing how many seconds have passed since the timer started or was last reset.
    - `time.monotonic()` is used inside the class. It returns the current value of a monotonic clock—a clock that cannot go backwards. It tracks seconds since the board turned on.
    - By comparing the current `monotonic()` value to our `_start_time`, we can measure elapsed time without using `time.sleep()`, which would pause our entire program. `time.sleep()` is considered a "Breaking timer". 
- **Loop Control**: Using `time.sleep(0.5)` here just slows down the text output; in a real robot, you would usually have a much smaller sleep or none at all to keep the robot responsive.

### Experiment
Try changing the `if timer.seconds() > 10:` condition to see how the duration affects the output timing. For example, change `10` to `5` for a shorter duration.

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# Look for the line that uses the "greater than" (>) symbol. 
# The number following that symbol represents the threshold in seconds.
</code></pre>
</details>

<details>
<summary>Click to reveal a solution</summary>
<pre><code>
# Inside the while True loop:
if timer.seconds() > 5:
    print("Timer reached!")
    break
</code></pre>
</details>

---

# 2. Restarting Timers
The `reset()` function is powerful because it lets you restart your count at any time. Let's assume you have a 2-second timer that restarts every time you flick a switch on your RC receiver (Channel 5).

```python
import time
from elapsed_time import ElapsedTime
from rc import RCReceiver

# Initialize the receiver with designated pins for channels
rc = RCReceiver(ch5=board.D3)

feeder_timer = ElapsedTime()

while True:
    ch5 = rc.read_channel(5)

    # If the switch is flipped, reset the timer to 0
    if ch5 == 1:
        feeder_timer.reset()
        print("Timer reset!")
    
    # Perform an action only if the timer is under 2 seconds
    if feeder_timer.seconds() < 2:
        print("Feeder active...")
    else:
        print("Feeder idle.")

    time.sleep(0.02) 
```

### Experiment
Create two timers:
- `timer_a` lasts 2 seconds. 
- `timer_b` lasts 5 seconds. 
- Each time Timer B reaches its limit (5), have it print "Resetting A" and **reset** both Timer A and Timer B.

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# You need to define two separate variables (timer_a and timer_b) as ElapsedTime objects.
# Inside your loop, check if timer_b.seconds() > 5. If it is, call the .reset() method on both.
</code></pre>
</details>

<details>
<summary>Click to reveal a solution</summary>
<pre><code>
timer_a = ElapsedTime()
timer_b = ElapsedTime()

timer_a.reset()
timer_b.reset()

while True:
    if timer_b.seconds() > 5:
        print("Resetting A")
        timer_a.reset()
        timer_b.reset()
    
    if timer_a.seconds() < 2:
        print("Timer A is running")
    
    time.sleep(0.1)
</code></pre>
</details>

---

# 3. Simple State Machines: The Heartbeat

s your robot gets more complex, your code can become a "spaghetti" of `if` statements that are hard to read. To fix this, roboticists use **Finite State Machines (FSMs)**. You've already done this before using simple functions for our maze robot. This time around, we're going to move our states into a single "update" function instead. As we move further in the course, we're going to start creating machines with multiple state machines, and this makes understanding much simpler. 

A State Machine is just a fancy way of saying the robot follows a specific "mode" (like "ON" or "OFF") and only switches modes when a specific event happens (transition events). We use **strings** to keep track of the state/mode and, in this example, an **elapsed_timer** to decide when to switch.

Let’s create a "Heartbeat" LED that blinks to show the robot's brain is running, without using `time.sleep()`. This is helpful for us to know that "if the board's LED is blinking, then we still have our program running". 

Use your rover from challenge #1 as a platform to program on.

```python
import time
import board
import digitalio
from elapsed_time import ElapsedTime

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

heartbeat_timer = ElapsedTime()
led_state = "ON" 

def update_led_state():
    global led_state
    
    if led_state == "ON":
        led.value = True
        if heartbeat_timer.seconds() > 0.5: # The "Transition" event
            led_state = "OFF"
            heartbeat_timer.reset()
            
    elif led_state == "OFF":
        led.value = False
        if heartbeat_timer.seconds() > 0.5: # The "Transition" event
            led_state = "ON"
            heartbeat_timer.reset()

heartbeat_timer.reset()
while True:
    update_led_state() 
    time.sleep(0.02)
```

### Experiment
Modify the code so the LED has an "unbalanced" heartbeat: make it stay **ON for 0.5 seconds** but stay **OFF for 1.0 second**. 

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# Look inside the update_led_state function. 
# There are two different "if heartbeat_timer.seconds() > ..." checks.
# Change the one inside the "OFF" state to 1.0.
</code></pre>
</details>

<details>
<summary>Click to reveal a solution</summary>
<pre><code>
def update_led_state():
    global led_state
    if led_state == "ON":
        led.value = True
        if heartbeat_timer.seconds() > 0.5: # ON duration
            led_state = "OFF"
            heartbeat_timer.reset()
    elif led_state == "OFF":
        led.value = False
        if heartbeat_timer.seconds() > 1.0: # OFF duration increased to 1.0
            led_state = "ON"
            heartbeat_timer.reset()
</code></pre>
</details>

---

# 4. Navigation FSM: Driving vs. Turning

Now we'll try to create a state machine for a simple wall avoiding robot. It will simply drive forward until it sees a wall, then turn. Instead of a "Blink" state, we have a "Driving" state and a "Turning" state. 
 

The transition happens in two ways:
1.  **Sensor Event:** If the distance is too small, switch from `DRIVING` to `TURNING`.
2.  **Timer Event:** If the turn timer reaches 1.2 seconds, switch from `TURNING` back to `DRIVING`.

Again, use your rover as a base. 

```python
mport time
import board
import pwmio
from adafruit_motor import servo
from sonarbit import Sonarbit
from elapsed_time import ElapsedTime

# init distance sensor
distance_sensor = Sonarbit(board.D2)
prev_distance= 570  # Initial value

# init drive servos
pwm = pwmio.PWMOut(board.D0, frequency=50)
pwm1 = pwmio.PWMOut(board.D1, frequency=50)

left_motor = servo.ContinuousServo(pwm)
right_motor = servo.ContinuousServo(pwm1)

nav_state = "DRIVING"
turn_timer = ElapsedTime()

def update_navigation_state():
    global nav_state, prev_distance
    distance = distance_sensor.get_distance(prev_distance)
    
    if nav_state == "DRIVING":
        left_motor.throttle = 0.5
        right_motor.throttle = -0.5
        if distance < 10:
            nav_state = "TURNING"
            turn_timer.reset()
            
    elif nav_state == "TURNING":
        left_motor.throttle = 0.5
        right_motor.throttle = 0.5 
        if turn_timer.seconds() > 1.2:
            nav_state = "DRIVING"
    
turn_timer.reset() #restart our timer before we begin our main loop
while True:
    print("Nav State", nav_state)
    update_navigation_state() #update state machine

    time.sleep(0.02)
    # The loop is free to do other things here!
```

### Experiment
Add a third state called `"BACKING_UP"`. When a wall is detected, the robot should back up for 0.5 seconds *before* it starts the `"TURNING"` state. 

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# 1. Change the DRIVING transition so it goes to "BACKING_UP" instead of "TURNING".
# 2. Add an 'elif' for "BACKING_UP" that sets motor throttles to reverse.
# 3. In the "BACKING_UP" state, check if turn_timer.seconds() > 0.5.
# 4. If it is, switch the state to "TURNING" and reset the timer again.
</code></pre>
</details>

<details>
<summary>Click to reveal a solution</summary>
<pre><code>
def update_navigation_state():
    global nav_state, prev_distance
    distance = distance_sensor.get_distance(prev_distance)
    
    if nav_state == "DRIVING":
        left_motor.throttle = 0.5
        right_motor.throttle = -0.5
        if distance < 10:
            nav_state = "BACKING_UP"
            turn_timer.reset()
            
    elif nav_state == "BACKING_UP":
        left_motor.throttle = -0.3
        right_motor.throttle = 0.3
        if turn_timer.seconds() > 0.5:
            nav_state = "TURNING"
            turn_timer.reset()
            
    elif nav_state == "TURNING":
        left_motor.throttle = 0.5
        right_motor.throttle = 0.5 
        if turn_timer.seconds() > 1.2:
            nav_state = "DRIVING"
</code></pre>
</details>

---

# 5. Combining Multiple FSMs (Multitasking)

The real power of `ElapsedTime` is that you can run both the Heartbeat and the Navigation logic **at the same time**. Because neither function uses `time.sleep()`, they don't block each other. 

Let's combine the state machines now: 

```python
import time
import board
import pwmio
from adafruit_motor import servo
from sonarbit import Sonarbit
from elapsed_time import ElapsedTime

# init distance sensor
distance_sensor = Sonarbit(board.D2)
prev_distance= 570  # Initial value

# init drive servos
pwm = pwmio.PWMOut(board.D0, frequency=50)
pwm1 = pwmio.PWMOut(board.D1, frequency=50)

left_motor = servo.ContinuousServo(pwm)
right_motor = servo.ContinuousServo(pwm1)

# init onboard LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# --- Setup FSM Variables ---
heartbeat_timer = ElapsedTime()
turn_timer = ElapsedTime()

led_state = "ON"
nav_state = "DRIVING"
prev_distance = 570

def update_led_state():
    global led_state
    if led_state == "ON":
        led.value = True
        if heartbeat_timer.seconds() > 0.5:
            led_state = "OFF"
            heartbeat_timer.reset()
    elif led_state == "OFF":
        led.value = False
        if heartbeat_timer.seconds() > 0.5:
            led_state = "ON"
            heartbeat_timer.reset()

def update_navigation_state():
    global nav_state, prev_distance
    distance = distance_sensor.get_distance(prev_distance)
    
    if nav_state == "DRIVING":
        left_motor.throttle = 0.5
        right_motor.throttle = -0.5
        if distance < 10:
            nav_state = "TURNING"
            turn_timer.reset()
    elif nav_state == "TURNING":
        left_motor.throttle = 0.5
        right_motor.throttle = 0.5
        if turn_timer.seconds() > 1.2:
            nav_state = "DRIVING"
    prev_distance = distance


heartbeat_timer.reset()
turn_timer.reset()
# --- Main Loop ---
while True:
    # Both systems run independently!
    print("Nav State:", nav_state, " | Led State:", led_state)

    update_led_state()
    update_navigation_state()
    
    time.sleep(0.01) # Small pause to keep CPU happy
```

### Final Challenge: The Rescue Robot
Create a third timer called `victory_timer`. Your robot should drive normally (avoiding walls), but every 15 seconds, it should stop everything it's doing and perform a "Victory Spin" (spin in a circle) for exactly 1 second. After the second is up, it should go back to normal driving/turning logic for another 15 seconds.

**Bonus**: Can you make the LED blink twice as fast while the robot is doing its Victory Spin?

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# In your while True loop, check if victory_timer.seconds() > 15.
# If it is, force nav_state = "VICTORY" and reset the victory_timer.
# In update_navigation_state, add a "VICTORY" state that spins for 1 second.
# For the bonus, in update_led_state, use an 'if nav_state == "VICTORY":' 
# to check for 0.25 seconds instead of 0.5.
</code></pre>
</details>

<details>
<summary>Click to reveal a solution</summary>
<pre><code>
# Setup
victory_timer = ElapsedTime()
victory_timer.reset()

def update_navigation_state():
    global nav_state
    # ... (other states) ...
    elif nav_state == "VICTORY":
        left_motor.throttle = 1.0
        right_motor.throttle = 1.0
        if victory_timer.seconds() > 1.0: # Spin for 1 second
            nav_state = "DRIVING"
            victory_timer.reset() # Reset to start the 15s count again

# Main Loop
while True:
    # Trigger victory every 15 seconds regardless of current state
    # because we want this to happen REGARDLESS of state, it needs to be outside of the state machine
    if victory_timer.seconds() > 15:
        nav_state = "VICTORY"
        victory_timer.reset() # Reset to time the 1-second spin
    
    update_led_state()
    update_navigation_state()
    time.sleep(0.01)
</code></pre>
</details>
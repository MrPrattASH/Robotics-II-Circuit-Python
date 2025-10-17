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
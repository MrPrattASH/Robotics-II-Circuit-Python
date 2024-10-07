import time
from timer import Timer

# Usage
timer = Timer()

# First call to set the timer
timer.set_timer(time.monotonic(), time.monotonic() + 30)  # 10 seconds timer

while True:
    # calls to check the timer status
    timer_end = timer.check_timer()
    print("Timer reached:", timer_end)

    time.sleep(0.5)
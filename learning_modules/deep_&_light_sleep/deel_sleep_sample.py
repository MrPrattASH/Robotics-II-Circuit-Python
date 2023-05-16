# pulls 7.3mA at deep sleep,
# 29-33mA at program run
# 16mA at idle

import time
import board
import digitalio
import alarm

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

print("Going to sleep")
led.value = False
time.sleep(1)

# Set up an alarm to wake us up after 30 seconds
alarms = [
    alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 10),
]

# Go to DEEP sleep until the alarm wakes us up
alarm.exit_and_deep_sleep_until_alarms(*alarms)

print("Woke up")
led.value = True


# Write your code here :-)

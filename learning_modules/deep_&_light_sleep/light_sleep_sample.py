# 29-33mA at program run
# 16mA at light sleep

import time
import board
import digitalio
import alarm

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

print("Going to sleep")
time.sleep(1)
led.value = False

# Set up an alarm to wake us up after 30 seconds
alarms = [
    alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 10),
]

# Go to LIGHT sleep until the alarm wakes us up
alarm.light_sleep_until_alarms(*alarms)
#light_sleep is effectively the same as time.sleep for power draw

print("Woke up")
led.value = True
time.sleep(2)


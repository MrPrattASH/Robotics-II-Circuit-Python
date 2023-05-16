# pulls 7.3mA at deep sleep,
# 29-33mA at program run
# 16mA at idle

import time
import board
import digitalio
import alarm

#init board LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

print("Going to sleep")
#turn off onboard LED
led.value = False
time.sleep(1)

# Set up an alarm to wake us up after 10 seconds
alarms = [
    alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 10),
]

# Go to DEEP sleep until the alarm wakes us up
alarm.exit_and_deep_sleep_until_alarms(*alarms)

#the program now "chills" here in this space until the alarm is triggered. 

print("Woke up")
led.value = True
#sleep for 2s to show the led 
time.sleep(2)

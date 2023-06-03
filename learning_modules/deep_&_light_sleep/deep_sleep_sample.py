'''multiple pin or timer alarms example
- The first section initializes the button as an input with a pulldown resistor. 
- The second section initializes the onboard LED as an output. 
- The third section sets up a list of alarms that will trigger when the button is pressed or after 10 seconds of deep sleep. 
- The while loop turns off the onboard LED when sleep starts and puts the board into deep sleep mode until either alarm is triggered. 
- When either alarm is triggered, it turns on the onboard LED and repeats the deep sleep program with the same alarms set.
'''

import board
import digitalio
import time
import alarm

# Initialize the onboard LED as an output
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Set up a list of alarms that will trigger when the button is pressed OR after 10 seconds of deep sleep
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 10)


# Turn on the onboard LED when the alarm is woken
led.value = True
time.sleep(1)
# Turn off the onboard LED before sleep starts
led.value = False

# Put the board into deep sleep mode until either alarm is triggered
alarm.exit_and_deep_sleep_until_alarms(time_alarm)
# we never reach here because we restart when exiting deep sleep
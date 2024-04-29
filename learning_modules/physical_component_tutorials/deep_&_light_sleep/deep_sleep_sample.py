'''DEEP SLEEP example
- This program enters deep sleep for 10s, then wakes up due to a 10s alarm. 
- Deep sleep causes the program to terminate on line 26, no more code is run after this statement. 
- Upon awake by alarm, the program starts again from line 7. 
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

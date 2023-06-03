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
pin_alarm1 = alarm.pin.PinAlarm(pin=board.A0, value = False, pull=True)
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 10)

#cue the user that we're about to enter deep sleep
led.value = True
print("going to sleep")
time.sleep(1)
led.value = False

# --------------- INIT DATA COLLECTION PINS -----------------
#init your data collection pins here, temp-D1, humid-D2, and soil moisture-A1



def data_collection_mode():
    #reinit the data_collection_mode "master" pin. must be done here, or we can't read it in loop
    pin = digitalio.DigitalInOut(board.A0)
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP

    #repeat until the user pushes the data_collection_mode button again
    while pin.value:
        #check your pin values and display the correct data...
        print("in function until either TIME Alarm or data_collection_button pressed events")
        time.sleep(1)

# ------------- ALARM WAKEUPS --------------------------

#check if a time based alarm woke us up
if isinstance(alarm.wake_alarm, alarm.time.TimeAlarm):
    print("\nA TIME alarm woke us up!")
    #start normal solenoid function

#check if a pin alarm woke us up (no way to know WHAT pin, just that A pin woke us)
elif isinstance(alarm.wake_alarm, alarm.pin.PinAlarm):
    print("\nA PIN alarm woke us up!")
    data_collection_mode()

alarm.exit_and_deep_sleep_until_alarms(pin_alarm1, time_alarm)
#we never get here as we now exit and deep sleep

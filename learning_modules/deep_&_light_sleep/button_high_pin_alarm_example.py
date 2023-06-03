import board
import digitalio
import time
import alarm

# Initialize the onboard LED as an output
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Set up an alarm that will trigger when the button is pressed
pin_alarm = alarm.pin.PinAlarm(pin=board.A0, value = False, pull=True)

# Turn off the onboard LED when sleep starts
print("going to sleep")
time.sleep(1)
led.value = False

# Put the board into deep sleep mode until the alarm is triggered
alarm.exit_and_deep_sleep_until_alarms(pin_alarm)

#the program now "chills" here in this space until the alarm is triggered. 

# Turn on the onboard LED when the alarm is woken
print("woke up")
led.value = True
time.sleep(2)

'''DEEP SLEEP example
- This program enters deep sleep for 10s, then wakes up due to a 10s alarm.
- Deep sleep causes the program to terminate on line 26, no more code is run after this statement.
- Upon awake by alarm, the program starts again from line 7.
'''

import board
import digitalio
import analogio
import time
import alarm
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
from adafruit_simplemath import map_range
import adafruit_sht4x 


# ----------------------- INIT MAIN DEVICES -----------------------

# Initialize the solenoid
Solenoid = digitalio.DigitalInOut(board.D0)
Solenoid.direction = digitalio.Direction.OUTPUT

#buggy workaround for pin alarm, init as pullup, get a value, then 
#cont. 

wake_button = digitalio.DigitalInOut(board.A0)
wake_button.direction = digitalio.Direction.INPUT
wake_button.pull = digitalio.Pull.UP
time.sleep(1)
wake_button.deinit()
time.sleep(3)

#moisture meter
soil_moisture = analogio.AnalogIn(board.A1)

# ----------------------- SLEEP ALARMS -----------------------
# Set up a list of alarms that will trigger when the button is pressed OR after 12h of deep sleep
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + (43020))
#MAYBE set this pull to false? 
pin_alarm1 = alarm.pin.PinAlarm(pin=board.A0, value = False, pull=True)

# ----------------------- INIT VARIABLES -----------------------

Timer = 0
on_time = 180
saturated = False



def data_collection_mode():

    # --------------- INIT DATA COLLECTION PINS -----------------
    #init your data collection pins here, temp-D1, humid-D2, and soil moisture-A1

    #Using a pin to control this mode is a bit unreliable unfortunately
    #instead, we'll use a 30s timer.


    #time monotonic grabs a second timer since the program started.
    #it's useful to non-breaking time events
    now = time.monotonic()
    end_time = now + 30

    #INIT NEW CONTROL BUTTONS
    moisture_button = digitalio.DigitalInOut(board.D3)
    moisture_button.direction = digitalio.Direction.INPUT
    moisture_button.pull = digitalio.Pull.UP
    moisture_buttonState = False

    #TODO: Add in RED Temp (D1)
    temp_button = digitalio.DigitalInOut(board.D1)
    temp_button.direction = digitalio.Direction.INPUT
    temp_button.pull = digitalio.Pull.UP
    hum_buttonState = False

    #TODO: Add in Yellow Humid (D2)
    hum_button = digitalio.DigitalInOut(board.D2)
    hum_button.direction = digitalio.Direction.INPUT
    hum_button.pull = digitalio.Pull.UP
    hum_buttonState = False

    #TODO: Init sh2 Temp sensor
    sht = adafruit_sht4x.SHT4x(board.I2C())

    #Init OLED display
    displayio.release_displays()
    oled_reset = board.D9

    # init i2C object
    i2c = board.I2C()
    #perhaps capitalD for address?)
    display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=oled_reset)

    #display parameters
    WIDTH = 128
    HEIGHT = 64
    BORDER = 5
    display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)
    
    
    #start main loop
    print('now in data_collection_mode')
    while now < end_time:
        #check your pin values and display the correct data...
        moisture_buttonState = moisture_button.value
        hum_buttonState = hum_button.value
        temp_buttonState = temp_button.value

        if not moisture_buttonState:
            moisture = soil_moisture.value
            moisture_mapped_value = map_range(moisture, 0, 65520, 0, 100)
            print("moisture % " + str(int(moisture_mapped_value)))

        if not temp_buttonState:
            print("Temperature: " + str(sht.temperature))
        
        if not hum_buttonState:
            print("Humidity: " + str(sht.relative_humidity))
        #if you're going to read buttons in this alarm, be sure to have a small sleep
        time.sleep(0.1)

    #\n prints a new line
    print("\n5sec Data record time done. \nGoing back to sleep")
    time.sleep(2)
    alarm.exit_and_deep_sleep_until_alarms(pin_alarm1, time_alarm)

if isinstance(alarm.wake_alarm, alarm.time.TimeAlarm):
    Solenoid.value = True
    while Timer < on_time:
        time.sleep(1)
        Timer+=1
    Solenoid.value = False
    time.sleep(1)

elif isinstance(alarm.wake_alarm, alarm.pin.PinAlarm):
    data_collection_mode()


# Turn off the onboard LED before sleep starts

# Put the board into deep sleep mode until either alarm is triggered
alarm.exit_and_deep_sleep_until_alarms(time_alarm,pin_alarm1)
# we never reach here because we restart when exiting deep sleep

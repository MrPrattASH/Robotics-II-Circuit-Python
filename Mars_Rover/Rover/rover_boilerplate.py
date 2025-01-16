import board
import time
import rc
import pwmio
from arcade_drive_servo import Drive
from adafruit_motor import servo
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306


rc = rc.RCReceiver(ch1=board.D10, ch2=board.D11, ch3=None, ch4=None, ch5=board.D12, ch6=board.D13)
drive = Drive(left_pin=board.D2, right_pin=board.D1, left_stop=0.0, right_stop=0.0)

# Drill servo
# Create a positional servo object, my_pos_servo.
pwm0 = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=50)
drill = servo.Servo(pwm0)


# Display
#reset displays, needed as if the m4 reboots, we must release the screen before init again.
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

printed = False
# Main code
print("Rover Operational")
while True:
    # Read joystick channels
    spin = rc.read_channel(1) # spin
    throttle = rc.read_channel(2) # throttle
    ch5 = rc.read_channel(5)
    
    if spin is not None and throttle is not None:
        drive.drive(spin,throttle)
        #print("spin", spin, "throttle", throttle) # move our motors arcade drive style
    
    if ch5 is not None:
        if ch5 == 0:
            #drill up
            drill.angle = 2
            if not printed:
                print("Excecuting Command:\n   Exo Mars Rover\n  ^^^ DRILL UP ^^^")
                printed = True
        else:
            drill.angle = 178
            if printed:
                print("Excecuting Command:\n   Exo Mars Rover\n  vvv DRILLING vvv")
                printed = False
            
    time.sleep(0.01)

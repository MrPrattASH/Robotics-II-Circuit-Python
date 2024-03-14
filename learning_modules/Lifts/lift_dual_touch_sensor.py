import time
import board
from rc import RCReceiver
from arcade_drive import Drive
import digitalio
import pwmio
from adafruit_motor import servo

# ----------- Init Classes -------------
rc = RCReceiver()
drive = Drive()

# ------------ INIT TOUCH SENSORS --------------
bottom = digitalio.DigitalInOut(board.D2)
top = digitalio.DigitalInOut(board.D3)

bottom.direction = digitalio.Direction.INPUT
top.direction = digitalio.Direction.INPUT

bottom.pull = digitalio.Pull.UP
top.pull = digitalio.Pull.UP

# ----------  INIT SERVO ------------
# create a PWMOut object on Pin A0.
pwm = pwmio.PWMOut(board.A2, frequency=50)

# Create a servo object, my_servo.
servo_1 = servo.ContinuousServo(pwm)


print("start")
# Main code
while True:
    #  Read joystick channels
    ch_1 = rc.read_channel(1)  # spin
    ch_2 = rc.read_channel(2)  # throttle
    ch_5 = rc.read_channel(5)  # 2way switch 
    
    # Read limit switches
    bottom_sw = bottom.value
    top_sw = top.value 
    
    print(ch_5)
    #  Drive
    if ch_1 is not None and ch_2 is not None:
        drive.drive(ch_1, ch_2)  # move our motors arcade drive style
    
    # Lift Switch
    if ch_5 is not None:  # 2 way switch, left side
        if ch_5:  # Lift UP
            if top_sw: #  button NOT pressed, servo up (Counter Clockwise) 
                servo_1.throttle = 0.2
            else: # stop servo
                servo_1.throttle = 0
        else:
            if bottom_sw: #  button NOT pressed, servo down (clockwise)
                servo_1.throttle = -0.2
            else: # stop servo
                servo_1.throttle = 0

    # sleep for 20ms, the length of a single duty cycle of the RC reciever.
    time.sleep(0.02)

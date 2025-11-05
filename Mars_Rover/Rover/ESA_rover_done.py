import time
import board
import pwmio
from adafruit_motor import servo
from rc import RCReceiver
from adafruit_simplemath import map_range

''' PINOUT
0 Left side Servos (pivot)
1 Right side Servos (pivot)
2 Left side continuous servos (drive)
3 right side continuous servos (drive)
4
5 drill continuous servo
6
7 ch3
8 ch4
9 OLED Reset
10 ch1
11 ch2
12 ch5
13 ch6
'''

# ----------------- INIT DEVICES -------------------------
#  Servos
pwm0 = pwmio.PWMOut(board.D0, duty_cycle=2 ** 15, frequency=50)
pwm1 = pwmio.PWMOut(board.D1, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50)
pwm3 = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=50)
pwm5 = pwmio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=50)


left_pivot = servo.Servo(pwm0)
right_pivot = servo.Servo(pwm1)
left_drive = servo.ContinuousServo(pwm2)
right_drive = servo.ContinuousServo(pwm3)
drill = servo.ContinuousServo(pwm5)

# ---- RCReceiver -----

rc = RCReceiver(ch1=board.D10, ch2=board.D11, ch3=None, ch4=None, ch5=board.D12, ch6=board.D13)


# left side, 97 ish is straight

while True:
    x = rc.read_channel(1)
    y = rc.read_channel(2)
    ch5 = rc.read_channel(5)
    
    if x == 50:
        left_pivot.angle = 97
        right_pivot.angle = 97
    else:
        left_pivot.angle = round(map_range(x, 0, 100, 0, 180))
        right_pivot.angle = round(map_range(x, 0,100,0,180))
    
    if y == 50:
        left_drive.throttle = 0
        right_drive.throttle = 0
    else:
        left_drive.throttle = map_range(y, 0, 100, 1, -1)
        right_drive.throttle = map_range(y, 0, 100, -1, 1)
    
    time.sleep(0.02)

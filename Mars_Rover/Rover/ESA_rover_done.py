import time
import board
import pwmio
from adafruit_motor import servo

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
pwm1 = pwmio.PWMOut(board.D0, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.D0, duty_cycle=2 ** 15, frequency=50)
pwm3 = pwmio.PWMOut(board.D0, duty_cycle=2 ** 15, frequency=50)
pwm5 = pwmio.PWMOut(board.D0, duty_cycle=2 ** 15, frequency=50)


left_pivot = servo.Servo(pwm0)
right_pivot = servo.Servo(pwm1)
left_drive = servo.ContinuousServo(pwm2)
right_drive = servo.ContinuousServo(pwm3)
drill = servo.ContinuousServo(pwm5)


# left side, 97 ish is straight

while True:
    '''
    for i in range(20,160,1):
        my_servo.angle = i
        time.sleep(0.02)
    for i in range(160,20,-1):
        my_servo.angle = i
        time.sleep(0.02)

    my_servo.angle = 110
    '''
    left_drive.throttle = -0.15

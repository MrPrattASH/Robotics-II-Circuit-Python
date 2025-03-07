import time
import board
import pwmio
from adafruit_motor import servo

""" PINOUTS
# D0 left servo
# D1 right servo
"""

# ---------------- INIT HARDWARE ----------------
# servos
pwm = pwmio.PWMOut(board.D0, frequency=50)
pwm_2 = pwmio.PWMOut(board.D1, frequency=50)

servo_1 = servo.ContinuousServo(pwm)
servo_2 = servo.ContinuousServo(pwm_2)

# ---------------- FUNCTIONS ----------------

def stop_rover():
    print("stop")
    servo_1.throttle = 0
    servo_2.throttle = 0
    time.sleep(2.0)

def turn(sleep_time):
    print("turning", sleep_time)
    servo_1.throttle = -0.5
    servo_2.throttle = -0.6
    time.sleep(sleep_time)

def forward(sleep_time):
    # Code to move the rover forward
    print("forward", sleep_time)
    servo_1.throttle = -0.25
    servo_2.throttle = 0.2
    time.sleep(sleep_time)

# calibrated turn times
degrees_90 = 0.75
degrees_180 = 1.35

#draw a square
for i in range(4):
    forward(1)
    stop_rover()
    time.sleep(1)
    turn(degrees_90)
    stop_rover()
    time.sleep(1)

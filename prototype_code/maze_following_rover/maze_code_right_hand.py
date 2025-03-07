import time
import board
import pwmio
from digitalio import DigitalInOut, Direction, Pull
from sonarbit import Sonarbit
from adafruit_motor import servo

""" PINOUTS
# D0 left servo
# D1 right servo
# D2 Distance sensor front
# D3 Distance sensor right
"""

# ---------------- INIT HARDWARE ----------------
# servos
pwm = pwmio.PWMOut(board.D0, frequency=50)
pwm_2 = pwmio.PWMOut(board.D1, frequency=50)

servo_1 = servo.ContinuousServo(pwm)
servo_2 = servo.ContinuousServo(pwm_2)

# Debug LEDs
led_right = DigitalInOut(board.D9)
led_forward = DigitalInOut(board.D12)

led_right.direction = Direction.OUTPUT
led_forward.direction = Direction.OUTPUT

# distance sensors
distance_sensor_front = Sonarbit(board.D2)
distance_sensor_right = Sonarbit(board.D3)

# ---------------- FUNCTIONS ----------------

def stop_rover():
    print("stop")
    servo_1.throttle = 0
    servo_2.throttle = 0
    time.sleep(2.0)

def right():
    print("right")
    servo_1.throttle = -0.5
    servo_2.throttle = -0.6
    time.sleep(0.75)

def u_turn():
    print("u turn")
    servo_1.throttle = 1
    servo_2.throttle = 1
    time.sleep(1.35)

def forward():
    # Code to move the rover forward
    servo_1.throttle = -0.25
    servo_2.throttle = 0.2
    time.sleep(2.0)
    print("forward")


prev_distance_front = 570  # highest value for distance sensors
prev_distance_right = 570


while True:
    # read distance sensors
    distance_front = distance_sensor_front.get_distance(prev_distance_front)
    distance_right = distance_sensor_right.get_distance(prev_distance_right)
    if distance_right > 20: # no wall on right
        time.sleep(1.0)
        # If no wall on right turn right
        led_right.value = False
        right()
        forward()
        stop_rover()

    else: # wall on right
        time.sleep(1.0)
        led_right.value = True  # light up debug LED to denote wall on right
        if distance_front > 20: # no wall in front
            led_forward.value = False
            forward()
            stop_rover()

        else: # wall in front and right
            led_forward.value = True # light up debug LED to denote wall in front
            u_turn()
            stop_rover()

    # reassign values of previous distance to current distance readings
    prev_distance_front = distance_front
    prev_distance_right = distance_right
    time.sleep(0.1) # minor sleep to prevent spamming of distance sensor readings

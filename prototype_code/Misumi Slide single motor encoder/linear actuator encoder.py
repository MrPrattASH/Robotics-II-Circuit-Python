# Write your code here :-)
# ROTATIONAL SERVO BOILER PLATE

import time
import board
import pwmio
import rotaryio
from digitalio import DigitalInOut, Direction, Pull
from math import tan, atan

encoder = rotaryio.IncrementalEncoder(board.D1, board.D2)

button = DigitalInOut(board.D13)
button.direction = Direction.INPUT
button.pull = Pull.UP  # Pull: defines the pull of a digital input pin


motor = pwmio.PWMOut(board.D0, frequency=50)

#motor speed commands
stop = 1.520
full_forward = 1.920 #+400us (microseconds)
full_reverse = 1.120 #-400us (microseconds)

'''Speed Values:
The speeds are based on pulse width duty cycles, (pwm). We use the below in the function above us.
'''

def servo_duty_cycle(pulse_ms, frequency=50):
    '''converts a pulse in milliseconds to a duty cycle value our motorcontroller can read
    pulse_ms - Int - accepts any value between 1.120 and 1.920
    '''
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

button_state = True         # Current debounced state
prev_button_state = True    # Last debounced state
last_debounce_time = 0
DEBOUNCE_DELAY = 0.05       # 50 ms debounce delay

length = 554 + 5.5 # mm 
height = 0
theta = 0
static_friction = 0
ticks_per_revolution = 384.5 # setup for 435rpm motor at shaft

# Main code
while True:
    motor_cur_pos = encoder.position
    button_state = button.value   # Read *raw* pin value
    #print(motor_cur_pos)

    if button_state != prev_button_state: #button pressed
        #reset timer
        last_debounce_time = time.monotonic()
        
    # If the state has been stable for longer than debounce delay
    if (time.monotonic() - last_debounce_time) > DEBOUNCE_DELAY:
        # If the button state has changed:
        if button_state != prev_button_state:
            if not button_state:
                motor.duty_cycle = servo_duty_cycle(full_forward-.200) #move forward at half speed
            else:
                motor.duty_cycle = servo_duty_cycle(stop) #stop motor
                print("stopping motor")

                height = (motor_cur_pos / ticks_per_revolution) * 8 #mm per full rev
                theta = atan(height/length) #angle of the arm
                static_friction = tan(theta)

                print("motor position: ", motor_cur_pos)
                print("height: ", height)
                print("theta: ", theta)
                print("static friction: ", static_friction)

                time.sleep(10)
                while motor_cur_pos > 0: #while the motor is not back to the starting position
                    motor.duty_cycle = servo_duty_cycle(full_reverse-.200) #move reverse at half speed
                    print("moving reverse")
                    motor_cur_pos = encoder.position
                    time.sleep(0.01) #prevent CPU overload
                motor.duty_cycle = servo_duty_cycle(stop) #stop motor


    prev_button_state = button_state  # Update last state for next loop
    time.sleep(0.01)  # Small delay to avoid CPU overload

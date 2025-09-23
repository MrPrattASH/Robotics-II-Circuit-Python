# Write your code here :-)
# ROTATIONAL SERVO BOILER PLATE

import time
import board
import pwmio
import rotaryio
from digitalio import DigitalInOut, Direction, Pull

encoder = rotaryio.IncrementalEncoder(board.D1, board.D2)

button = DigitalInOut(board.D3)
button.direction = Direction.INPUT
button.pull = Pull.UP  # Pull: defines the pull of a digital input pin

button_state = True

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
last_button_state = True    # Last debounced state
last_debounce_time = 0
DEBOUNCE_DELAY = 0.05       # 50 ms debounce delay
# Main code
while True:
    motor_cur_pos = encoder.position
    reading = button.value   # Read *raw* pin value
    #print(motor_cur_pos)

    if reading != last_button_state:
        # Button changed, reset timer
        last_debounce_time = time.monotonic()

    # If the state has been stable for longer than debounce delay
    if (time.monotonic() - last_debounce_time) > DEBOUNCE_DELAY:
        # If the button state has changed:
        if reading != button_state:
            button_state = reading
            if not button_state:
                start_ext = time.monotonic()
                while motor_cur_pos > -300: #UP
                    motor_cur_pos = encoder.position
                    #print(motor_cur_pos)
                    motor.duty_cycle = servo_duty_cycle(full_reverse)
                end_ext = time.monotonic()
                motor.duty_cycle = servo_duty_cycle(stop)
                total_ext = round(end_ext-start_ext,2)
                print("\n\n")
                print("Ext", total_ext)
            else:
                #print("off")
                # add a brief pause after reaching max height
                motor.duty_cycle = servo_duty_cycle(stop)
                time.sleep(0.1)
                start_ret = time.monotonic()
                while motor_cur_pos < -30: #DOWN
                    motor_cur_pos = encoder.position
                    #print(motor_cur_pos)
                    motor.duty_cycle = servo_duty_cycle(full_forward)
                end_ret = time.monotonic()
                motor.duty_cycle = servo_duty_cycle(stop)
                total_ret = (round(end_ret-start_ret,2)-0.1)
                print("Ret", total_ret)
                print("Cycle", str(total_ext + total_ret))

    last_button_state = reading
    time.sleep(0.01)  # Small delay to avoid CPU overload

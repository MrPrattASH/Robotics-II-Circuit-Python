'''Basic Roboclaw instructions
DEBUG:

No seriously Mr. Pratt, do this first.

Sometimes the roboclaw likes to add mixing back, EVEN IF PROGRAMMED CORRECTLY W/ ONBOARD BUTTONS.
Verify the below settings on basic micro windows App & write settings to the board again.

Button mode 1 (RC - Tank Style Driving)
Option 3:
F MIXING
T TTL FLip
F Exponential
T MCU

'''
import time
import board
import pwmio

#init motors as PWM objects
motor1 = pwmio.PWMOut(board.D3, frequency=50)
motor2 = pwmio.PWMOut(board.D2, frequency=50)

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

while True:
    motor1.duty_cycle = servo_duty_cycle(full_forward)
    motor2.duty_cycle = servo_duty_cycle(full_forward)
    print("forward")
    time.sleep(2)

    motor1.duty_cycle = servo_duty_cycle(stop)
    motor2.duty_cycle = servo_duty_cycle(stop)
    print("stop")
    time.sleep(2)

    motor1.duty_cycle = servo_duty_cycle(full_reverse)
    motor2.duty_cycle = servo_duty_cycle(full_reverse)
    print("backward")
    time.sleep(2)

    motor1.duty_cycle = servo_duty_cycle(stop)
    motor2.duty_cycle = servo_duty_cycle(stop)
    print("stop")
    time.sleep(2)




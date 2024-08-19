import time
import board
import pulseio
import digitalio
import pwmio

# Encoder pin setup
ENCODER_A = board.D2  # Encoder A channel pin
ENCODER_B = board.D3  # Encoder B channel pin
encoder_a = digitalio.DigitalInOut(ENCODER_A)
encoder_a.direction = digitalio.Direction.INPUT
encoder_b = digitalio.DigitalInOut(ENCODER_B)
encoder_b.direction = digitalio.Direction.INPUT

# Initialize variables
last_time = time.monotonic()
last_position = 0
ppr = 537.7  # Encoder resolution in pulses per revolution

#init motors as PWM objects
motor = pwmio.PWMOut(board.D0, frequency=50)

#motor speed commands
stop = 1.520
full_forward = 1.920 #+400us (microseconds)
full_reverse = 1.120 #-400us (microseconds)

def servo_duty_cycle(pulse_ms, frequency=50):
    '''converts a pulse in milliseconds to a duty cycle value our motorcontroller can read
    pulse_ms - Int - accepts any value between 1.120 and 1.920
    '''
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

# Function to read encoder
def read_encoder():
    a = encoder_a.value
    b = encoder_b.value
    return a, b

# Function to calculate speed and direction
def calculate_speed_and_direction(current_position, last_position, elapsed_time):
    delta_position = current_position - last_position
    speed = (delta_position / ppr) / elapsed_time  # speed in revolutions per second
    direction = "CW" if delta_position > 0 else "CCW" if delta_position < 0 else "Stopped"
    return speed, direction

# Function to stop the motor
def stop_motor():
    motor.value = False

# Function to run the motor
def run_motor():
    motor.value = True

# Main loop
motor.duty_cycle = servo_duty_cycle(full_forward-(400*0.75))
while True:
    current_time = time.monotonic()
    elapsed_time = current_time - last_time

    # Read the encoder
    a, b = read_encoder()
    current_position = a - b

    # Calculate speed and direction
    speed, direction = calculate_speed_and_direction(current_position, last_position, elapsed_time)

    # Check for excessive load (example threshold: speed < 0.1 rev/s)
    if speed < 0.1:
        motor.duty_cycle = servo_duty_cycle(stop)
        print("stop")

    # Print the results (for debugging)
    print(f"Speed: {speed:.2f} rev/s, Direction: {direction}")

    # Update variables
    last_time = current_time
    last_position = current_position

    # Adjust the speed check interval as needed
    time.sleep(0.1)
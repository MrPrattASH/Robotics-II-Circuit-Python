import time
import board
import pwmio
import rotaryio
from digitalio import DigitalInOut, Direction, Pull

# === CONFIG ===
ENCODER_TICKS_PER_REV = 112  # <-- set this to match your motor/encoder
SAMPLE_INTERVAL = 0.1       # seconds per measurement window
RECOVERY_THRESHOLD = 0.95   # % of max RPM considered "recovered"

# === HARDWARE SETUP ===
encoder = rotaryio.IncrementalEncoder(board.D1, board.D2)

button = DigitalInOut(board.D3)
button.direction = Direction.INPUT
button.pull = Pull.UP

motor = pwmio.PWMOut(board.D0, frequency=50)

# motor speed commands
stop = 1.520
full_forward = 1.920

def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

# === HELPER: CALCULATE RPM ===
def get_rpm(prev_ticks, prev_time):
    ticks = encoder.position
    now = time.monotonic()
    dt = now - prev_time
    delta_ticks = ticks - prev_ticks
    revs = delta_ticks / ENCODER_TICKS_PER_REV
    rpm = (revs / dt) * 60.0
    return rpm, ticks, now

# === MAIN LOOP ===
while True:
    # Wait for button press
    while button.value:
        pass  # do nothing until button pressed

    print("Button pressed, spinning up motor...")
    motor.duty_cycle = servo_duty_cycle(full_forward)

    # spin-up + measure max RPM
    max_rpm = 0
    prev_ticks = encoder.position
    prev_time = time.monotonic()
    start_time = prev_time

    while time.monotonic() - start_time < 3:  # 3 sec spin-up window
        time.sleep(SAMPLE_INTERVAL)
        rpm, prev_ticks, prev_time = get_rpm(prev_ticks, prev_time)
        if rpm > max_rpm:
            max_rpm = rpm
        print("RPM:", rpm)

    print("Max average RPM:", max_rpm)

    # === WAIT FOR BALL EVENT ===
    print("Waiting for RPM drop...")
    min_rpm = max_rpm * .99
    drop_time = None
    recovering = False
    recovery_start = None

    while True:
        time.sleep(SAMPLE_INTERVAL)
        rpm, prev_ticks, prev_time = get_rpm(prev_ticks, prev_time)

        if rpm < min_rpm:
            min_rpm = rpm
            drop_time = time.monotonic()
            recovering = True
            print("Ball event detected! Min RPM:", min_rpm)

        if recovering and rpm >= max_rpm * RECOVERY_THRESHOLD:
            recovery_time = time.monotonic() - drop_time
            print("Recovered to near max RPM")
            print("Lowest RPM:", min_rpm)
            print("Recovery time (s):", recovery_time)
            break

    # stop motor until next button press
    motor.duty_cycle = servo_duty_cycle(stop)
    print("Motor stopped. Press button to test again.")
    time.sleep(1)

import time
import board
import pwmio
import rotaryio

# === TODO CHANGES ===
# for each, set values higher or lower depending on your tests
GEAR_RATIO = 1.0 # set to 1.0 if no external gearing, otherwise set to your ratio


'''
Don't change anything below this line! 
'''

# === HARDWARE SETUP ===
encoder = rotaryio.IncrementalEncoder(board.D6, board.D7) #TC5 Timer

flywheel = pwmio.PWMOut(board.D4, frequency=50) #left flywheel motor TC2 Timer


# === CONFIG ===
ENCODER_TICKS_PER_REV = 28  # Flywheel motor encoder ticks @ 6K RPM motor
SAMPLE_INTERVAL = 0.02       # seconds per measurement window
RECOVERY_THRESHOLD = 0.95   # % of max RPM considered "recovered"
STOP = 1.520 # motor stop command
FULL_FORWARD = STOP + .400 # motor max fwd 
FULL_REVERSE = STOP - .400 # motor max rev
GATE_OPEN_TIME = 0.25

# === P control setup ===
Kp = 0.0001
BASE_MOTOR_POWER = STOP + .3

def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

# === HELPER: CALCULATE RPM ===
def get_rpm(encoder, prev_ticks, dt):
    delta_ticks = encoder.position - prev_ticks
    if dt == 0: return 0.0
    revs = delta_ticks / ENCODER_TICKS_PER_REV
    rpm = (revs / dt) * 60.0
    return rpm


# === MAIN LOOP ===
'''
1. Run the Flywheel at goal RPM. 
'''

prev_ticks = encoder.position
cur_rpm = 0.0
prev_rpm_time = time.monotonic()

fire_start_time = 0.0

flywheel_power = STOP

print("Motor Starting in 3..")
time.sleep(1)
print("2..")
time.sleep(1)
print("1..")
time.sleep(1)

start_loop = time.monotonic()
end_loop = start_loop + 5 # run for 5 seconds
while True:
    # update encoders at fixed interval
    now = time.monotonic()
    if now > end_loop:
        break
    dt = now - prev_rpm_time
    if dt >= SAMPLE_INTERVAL:
        cur_rpm = get_rpm(encoder, prev_ticks, dt)
        prev_ticks = encoder.position
        prev_rpm_time = now
        
    print(f"input RPM = {cur_rpm:.0f} | Output RPM = {cur_rpm * GEAR_RATIO:.0f}")

    flywheel.duty_cycle = servo_duty_cycle(FULL_FORWARD)

    time.sleep(0.02) 

#stop motor
flywheel.duty_cycle = servo_duty_cycle(STOP)

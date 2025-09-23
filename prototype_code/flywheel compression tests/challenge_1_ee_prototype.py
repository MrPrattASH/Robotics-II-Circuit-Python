import time
import board
import pwmio
import rotaryio
from digitalio import DigitalInOut, Direction, Pull
import rc
from arcade_drive_dc import Drive
from adafruit_motor import servo

# === TODO CHANGES ===
# for each, set values higher or lower depending on your tests
FLYWHEEL_GOAL_RPM = 300 
SERVO_GATE_OPEN_ANGLE = 90 
SERVO_GATE_CLOSE_ANGLE = 120 
GATE_OPEN_TIME = 0.75 # how long the gate remains open in seconds






# === HARDWARE SETUP ===
encoder = rotaryio.IncrementalEncoder(board.D6, board.D7) #TC5 Timer

flywheel_left = pwmio.PWMOut(board.D4, frequency=50) #left flywheel motor TC2 Timer

rc = rc.RCReceiver(ch1=board.D0, ch2=board.D1, ch3=None, ch4=None, ch5=board.D2, ch6=board.D3) #TC 0/1/4 Timers
drive = Drive(left=board.D10, right=board.D11) # init's motors like flywheel_left TC3 Timer

servo_pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
gate_servo = servo.Servo(servo_pwm)

# === CONFIG ===
ENCODER_TICKS_PER_REV = 112  # Flywheel motor encoder ticks @ 6K RPM motor
SAMPLE_INTERVAL = 0.1       # seconds per measurement window
RECOVERY_THRESHOLD = 0.95   # % of max RPM considered "recovered"
STOP = 1.520 # motor stop command
FULL_FORWARD = STOP + .400 # motor max fwd 
FULL_REVERSE = STOP - .400 # motor max rev

# === P control setup ===
Kp = 0.001
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

# === STATE MACHINE SETUP ===
STATE_IDLE = "IDLE"
STATE_SPINNING_UP = "SPINNING_UP"
STATE_READY = "READY"
STATE_FIRING = "FIRING"

flywheel_state = STATE_IDLE
print(f"starting in State: {flywheel_state}")


# === MAIN LOOP ===
'''
1. read RC channels + store values
2. if ch6 >=1, spin up flywheels
3. if ch5 ==1, attempt to launch servo if flywheels at speed. launch one flywheels at speed. 
'''

prev_ticks = encoder.position
cur_rpm = 0.0
prev_rpm_time = time.monotonic()

fire_start_time = 0.0

flywheel_power = STOP

gate_servo.angle = SERVO_GATE_CLOSE_ANGLE

while True:
    now = time.monotonic()

    # read RC channels
    spin = rc.read_channel(1)
    throttle = rc.read_channel(2)
    gate_request = rc.read_channel(5) == 1 # True if flipped
    flywheel_request = rc.read_channel(6) == 1 # True if flipped

    if spin is not None and throttle is not None:
        drive.drive(spin, throttle) # move drive motors arcade style

    # update encoders at fixed interval
    dt = now - prev_rpm_time
    if dt >= SAMPLE_INTERVAL:
        cur_rpm = get_rpm(encoder, prev_ticks, dt)

        prev_ticks = encoder.position
        prev_rpm_time = now


    # ========== STATE MACHINE START ===========
    # Master Off Switch
    if not flywheel_request and flywheel_state != STATE_IDLE:
        print(f"Flywheel OFF. State: {flywheel_state} > IDLE ")
        flywheel_state = STATE_IDLE

    # === IDLE ===
    if flywheel_state == STATE_IDLE:
        flywheel_power = STOP
        gate_servo.angle = SERVO_GATE_CLOSE_ANGLE

        if flywheel_request:
            print("State: IDLE > SPINNING_UP")
            flywheel_state = STATE_SPINNING_UP

    # === SPINNING_UP ===
    elif flywheel_state == STATE_SPINNING_UP:

        # P controller logic
        print(f"State: SPINNING_UP: Cur RPM = {cur_rpm:.0f}")
        error = (FLYWHEEL_GOAL_RPM - cur_rpm)
        p_adj = error * Kp

        #apply P control & clamp
        flywheel_power = max(FULL_REVERSE, min(FULL_FORWARD, BASE_MOTOR_POWER + p_adj))
        
        #Transition if wheel at speed
        if cur_rpm >= FLYWHEEL_GOAL_RPM * RECOVERY_THRESHOLD:
            flywheel_state = STATE_READY
    
    # === READY ===
    elif flywheel_state == STATE_READY:
        print(f"State: READY: Cur RPM = {cur_rpm:.0f}")
        error = (FLYWHEEL_GOAL_RPM - cur_rpm)
        p_adj = error * Kp

        #apply P control & clamp
        flywheel_power = max(FULL_REVERSE, min(FULL_FORWARD, BASE_MOTOR_POWER + p_adj))
        
        # Transition: If user requests to Fire, go to firing state
        if gate_request: 
            print("State: READY > FIRING")
            fire_start_time = now
            flywheel_state = STATE_FIRING
    
    # === FIRING ===
    elif flywheel_state == STATE_FIRING:
        gate_servo.angle = SERVO_GATE_OPEN_ANGLE
        # keep motors running 
        error = (FLYWHEEL_GOAL_RPM - cur_rpm)
        p_adj = error * Kp

        #apply P control & clamp
        flywheel_power = max(FULL_REVERSE, min(FULL_FORWARD, BASE_MOTOR_POWER + p_adj))
        

        # Transition: Give the gate time to react. Once reacted, close gate and move to SPINUP
        if now - fire_start_time > GATE_OPEN_TIME:
            gate_servo.angle = SERVO_GATE_CLOSE_ANGLE # return gate to closed

            print("State: FIRING > SPINNING_UP")
            flywheel_state = STATE_SPINNING_UP

    flywheel_left.duty_cycle = servo_duty_cycle(flywheel_power)

    time.sleep(0.02) # keep is in sync with rc receiver 


import board
import pwmio

class Drive:
    def __init__(self, motor_type="servo", left_pin=board.D0, right_pin=board.D1, freq=50, scale=1.0):
        """
        motor_type: "servo" or "dc"
        left_stop/right_stop: Used for servo calibration (fine-tuning the stop point)
        """
        self.motor_type = motor_type.lower()
        self.m_left = pwmio.PWMOut(left_pin, frequency=freq)
        self.m_right = pwmio.PWMOut(right_pin, frequency=freq)
        self.scale = scale
        self.freq = freq

        # Pre-calculate duty cycle constants
        self.min_duty = int(0.05 * 65535)  # 5% duty cycle (~1.0ms)
        self.max_duty = int(0.1 * 65535)   # 10% duty cycle (~2.0ms)
        self.mid_duty = int(0.075 * 65535) # 7.5% duty cycle (~1.5ms)

        # Servo specific stop duties (calibration)
        if self.motor_type == "servo":
            self.stop = int(0.5 * (self.max_duty - self.min_duty) + self.min_duty)
        elif self.motor_type == "dc":
            self.stop = 1.520
            self.full_forward = 1.920
            self.full_reverse = 1.120

    def _ms_to_duty(self, pulse_ms):
        """Converts millisecond pulse lengths to duty cycle (used for DC mode)."""
        period_ms = 1.0 / self.freq * 1000.0
        return int(pulse_ms / (period_ms / 65535.0))

    def drive(self, spin=0, throttle=0):
        """Standard Arcade Drive logic."""
        if spin is None: spin = 0
        if throttle is None: throttle = 0

        if throttle == 0 and spin == 0:
            left_val = right_val = 0 
        else:
            # Calculate raw motor speeds (-1.0 to 1.0)
            left_val = self.scale * (throttle - spin)
            right_val = self.scale * (throttle + spin)

        # Clamp values to -1.0 and 1.0
        left_val = max(-1, min(1, left_val))
        right_val = max(-1, min(1, right_val))

        if self.motor_type == "servo":
            # Servo logic: Map -1 to 1 onto the duty cycle range
            # Note: Inverted right_val to match original servo logic
            self.m_left.duty_cycle = self._map_to_servo(left_val, self.stop)
            self.m_right.duty_cycle = self._map_to_servo(-right_val, self.stop)

        else:
            # DC logic: Map -1 to 1 onto ms pulses (1.12ms to 1.92ms)
            # Center is 1.52ms
            left_ms = 1.520 + (left_val * 0.4) 
            right_ms = 1.520 + (right_val * 0.4)
            
            self.m_left.duty_cycle = self._ms_to_duty(left_ms)
            self.m_right.duty_cycle = self._ms_to_duty(right_ms)

    def _map_to_servo(self, value, stop_duty):
        """Helper to map normalized -1...1 to servo duty cycle."""
        if value == 0:
            return stop_duty
        # Map (-1, 1) to (min_duty, max_duty)
        return int(((value + 1) / 2) * (self.max_duty - self.min_duty) + self.min_duty)
import board
import pwmio

class Drive:
    def __init__(self, left_pin=board.D0, right_pin=board.D1, freq=50, scale=0.5, left_stop=0.0, right_stop=0.0):
        self.m1 = pwmio.PWMOut(right_pin, frequency=freq)
        self.m2 = pwmio.PWMOut(left_pin, frequency=freq)
        self.scale = scale
        # Convert normalized stop values to duty cycles
        min_duty = int(0.05 * 65535)  # 5% duty cycle for full reverse
        max_duty = int(0.1 * 65535)   # 10% duty cycle for full forward
        self.left_stop_duty = int(((left_stop + 1) / 2) * (max_duty - min_duty) + min_duty)
        self.right_stop_duty = int(((right_stop + 1) / 2) * (max_duty - min_duty) + min_duty)

    def control_servo(self, value, servo, stop_duty):
        """Controls a rotational servo based on an input value."""
        min_duty = int(0.05 * 65535)  # 5% duty cycle for full reverse
        max_duty = int(0.1 * 65535)   # 10% duty cycle for full forward
        # Map value from (-1.0, 1.0) to (min_duty, max_duty)
        duty_cycle = int(((value + 1) / 2) * (max_duty - min_duty) + min_duty)
        servo.duty_cycle = duty_cycle if value != 0 else stop_duty

    def drive(self, spin, throttle):
        """Throttle and spin control using arcade drive logic."""
        if spin == None:
            spin = 50
        if throttle == None:
            throttle = 50
        spin = (spin - 50) / 50  # Normalize spin to -1 to 1
        throttle = (throttle - 50) / 50  # Normalize throttle to -1 to 1
        scale_factor = self.scale

        if throttle == 0 and spin == 0:
            left = right = 0  # Stop
        else:
            left = scale_factor * (throttle - spin)
            right = scale_factor * (throttle + spin)
        
        # Clamping values within -1 to 1
        left = max(-1, min(1, left))
        right = max(-1, min(1, right))

        self.control_servo(left, self.m1, self.right_stop_duty)
        self.control_servo(-right, self.m2, self.left_stop_duty)  # Note the inversion for right
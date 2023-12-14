import board
import pwmio

class Drive:
    def __init__(self, left=board.D0, right=board.D1, freq=50, scale=0.5):
        self.m1 = pwmio.PWMOut(left, frequency=freq)
        self.m2 = pwmio.PWMOut(right, frequency=freq)
        self.scale = scale

    def servo_duty_cycle(self, pulse_ms, freq=50):
        ''' 
        Converts a ms_pulse length into a duty cycle value

        :pulse_ms: float: 
        
        '''
        period_ms = 1.0 / freq * 1000.0
        duty_cycle = int(pulse_ms / (period_ms / 65535.0))
        return duty_cycle
    
    def map_value(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def drive(self, spin, throttle):
        """throttles the robot using arcade throttle."""
        if throttle == 50 and spin == 50:
            left = right = 1.520 # stop
        else:
            #map to -1 to 1 for drive
            throttle = self.map_value(throttle, 5, 95, -1, 1)
            spin = self.map_value(spin, 5, 95, -1, 1)
            
            # Arcadedrive logic
            scale_factor = self.scale  # This can be adjusted
            left = 1.520 + scale_factor * (throttle - spin)
            right = 1.520 + scale_factor * (throttle + spin)

            # Clamping the values to be within motor command range
            left = max(1.120, min(1.920, left))
            right = max(1.120, min(1.920, right))
        
        
        #print('left',left,'right',right)
        self.m1.duty_cycle = self.servo_duty_cycle(left)
        self.m2.duty_cycle = self.servo_duty_cycle(right)
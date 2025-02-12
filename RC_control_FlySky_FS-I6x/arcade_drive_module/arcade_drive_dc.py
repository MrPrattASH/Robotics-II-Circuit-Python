import board
import pwmio

class Drive:
    def __init__(self, left=board.D0, right=board.D1, freq=50, scale=0.5):
        self.m1 = pwmio.PWMOut(left, frequency=freq)
        self.m2 = pwmio.PWMOut(right, frequency=freq)
        self.scale = scale
        self.stop = 1.520
        self.full_forward = 1.920
        self.full_reverse = 1.120

    def duty_cycle(self, pulse_ms, freq=50):
        ''' 
        Converts a ms_pulse length into a duty cycle value

        :pulse_ms: float: 
        
        '''
        period_ms = 1.0 / freq * 1000.0
        duty_cycle = int(pulse_ms / (period_ms / 65535.0))
        return duty_cycle

    def drive(self, spin, throttle):
        """throttles the robot using arcade throttle."""
        if spin == None:
            spin = 50
        if throttle == None:
            throttle = 50

        spin = (spin - 50) / 50  # Normalize spin to -1 to 1
        throttle = (throttle - 50) / 50  # Normalize throttle to -1 to 1
        scale_factor = self.scale 


        if throttle == 0 and spin == 0:
            left = right = 1.520 # stop
        else:            
            # Arcadedrive logic
            left = 1.520 + scale_factor * (throttle - spin)
            right = 1.520 + scale_factor * (throttle + spin)

            # Clamping the values to be within motor command range
            left = max(self.full_reverse, min(self.full_forward, left))
            right = max(self.full_reverse, min(self.full_forward, right))
        
        #print('left',left,'right',right)
        self.m1.duty_cycle = self.duty_cycle(left)
        self.m2.duty_cycle = self.duty_cycle(right)
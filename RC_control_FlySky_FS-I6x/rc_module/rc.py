import board
import pulseio
import time

class RCReceiver:
    def __init__(self, ch1, ch2, ch3, ch4, ch5, ch6):
        self.channel_pins = list(filter(None, [ch1, ch2, ch3, ch4, ch5, ch6]))
        self.pwm_ins = [pulseio.PulseIn(pin, maxlen=64, idle_state=False) for pin in self.channel_pins]
        self.last_read_time = time.monotonic()
        print("RCReceiver initialized with channels:", self.channel_pins)

    @staticmethod
    def correct_pulse(high_pulse, low_pulse, channel):
        if high_pulse > 2050:
            high_pulse, low_pulse = low_pulse, high_pulse

        if channel <= 4 and channel > 0:
            high_pulse_scaled = round((high_pulse - 950) * 100 / (2050 - 950))
            if 46 < high_pulse_scaled < 54:
                high_pulse_scaled = 50
        elif channel == 5:
            high_pulse_scaled = 0 if high_pulse < 1500 else 1
        elif channel == 6:
            if high_pulse < 1200:
                high_pulse_scaled = 0
            elif high_pulse < 1700:
                high_pulse_scaled = 1
            else:
                high_pulse_scaled = 2
        else:
            high_pulse_scaled = high_pulse

        return high_pulse_scaled, low_pulse

    def read_channel(self, channel, timeout=0.1):
        high_pulse = None
        index = channel - 1
        if channel in [5, 6]:
            index = channel - 3
        if index < 0 or index >= len(self.pwm_ins):
            print(f"Channel {channel} is not active")
            return None
        
        pwm_in = self.pwm_ins[index]
        print(f"Reading channel {channel} with index {index}")
        
        start_time = time.monotonic()

        try:
            while len(pwm_in) < 2:
                if time.monotonic() - start_time > timeout:
                    print(f"Timeout waiting for pulses on channel {channel}")
                    return None
                time.sleep(0.005)
            
            high_pulse, low_pulse = pwm_in[0], pwm_in[1]
            high_pulse, low_pulse = self.correct_pulse(high_pulse, low_pulse, channel)
            pwm_in.clear()

        except RuntimeError as e:
            print(f"Failed to read from channel {channel} with error: {str(e)}")

        return high_pulse
    '''
    def ensure_cycle(self):
        current_time = time.monotonic()
        elapsed_time = current_time - self.last_read_time
        if elapsed_time < 0.02:
            time.sleep(0.02 - elapsed_time)
        self.last_read_time = time.monotonic()
    '''
# rc.py
import board
import pulseio
import time

class RCReceiver:
    def __init__(self, ch1, ch2, ch3, ch4, ch5, ch6): #  channel_pins = [board.D7, board.D8, board.D9, board.D10, board.D11, board.D12]):
        self.channel_pins = []
        self.is_ch1 = False
        self.is_ch2 = False
        self.is_ch3 = False
        self.is_ch4 = False
        self.is_ch5 = False
        self.is_ch6 = False
        if ch1 is not None:
            self.channel_pins.append(ch1)
            self.is_ch1 = True
        if ch2 is not None:
            self.channel_pins.append(ch2)
            self.is_ch2 = True
        if ch3 is not None:
            self.channel_pins.append(ch3)
            self.is_ch3 = True
        if ch4 is not None:
            self.channel_pins.append(ch4)
            self.is_ch4 = True
        if ch5 is not None:
            self.channel_pins.append(ch5)
            self.is_ch5 = True
        if ch6 is not None:
            self.channel_pins.append(ch6)
            self.is_ch6 = True
        self.pwm_ins = [pulseio.PulseIn(pin, maxlen=64, idle_state=False) for pin in self.channel_pins]
        # __init__(self, channel_pins = [board.D7, board.D8, board.D9, board.D10, board.D11, board.D12]):
        #self.channel_pins = channel_pins

    @staticmethod
    def correct_pulse(high_pulse, low_pulse, channel):
        pulse_length_min = 950
        pulse_length_max = 2050
        # Reverse correction if necessary
        if high_pulse > pulse_length_max:
            high_pulse, low_pulse = low_pulse, high_pulse

        # Scale the high_pulse value from its original range to -100 to 100 scale.
        #scale_min = 0
        #scale_max = 100
        #high_pulse_scaled = round((high_pulse - pulse_length_min) * (scale_max - scale_min) / (pulse_length_max - pulse_length_min)) + scale_min
        if channel <= 4 and channel > 0:
            # Scale from 0 to 100 for channels 1-4
            scale_min = 0
            scale_max = 100
            high_pulse_scaled = round((high_pulse - pulse_length_min) * (scale_max - scale_min) / (pulse_length_max - pulse_length_min))
            if high_pulse_scaled < 54 and high_pulse_scaled > 46:
                # centre the deadpoint of our joysticks
                high_pulse_scaled = 50
        elif channel == 5:
            # Scale to 0 or 1 for channel 5
            high_pulse_scaled = 0 if high_pulse < 1500 else 1 
        elif channel == 6:
            # Scale to 0, 1, or 2 for channel 6
            if high_pulse < 1200:
                high_pulse_scaled = 0
            elif high_pulse < 1700:
                high_pulse_scaled = 1
            else:
                high_pulse_scaled = 2
        else:
            high_pulse_scaled = high_pulse  # default to no scaling
        
        return high_pulse_scaled, low_pulse


    def read_channel(self, channel):
        high_pulse = None
            
        try: 
            # pause to acquire values - removed and pause in the main code instead. 
            #time.sleep(0.02)
            # select specified channel
            if not self.is_ch3 or not self.is_ch4:
                if channel == 5 or channel == 6:
                    pwm_in = self.pwm_ins[channel -3]
                else:
                    pwm_in = self.pwm_ins[channel - 1]
            else:
                pwm_in = self.pwm_ins[channel - 1]

          

            # Number of pulses that have been read
            num_pulses = len(pwm_in)
        
            high_pulse = low_pulse = 0
            if num_pulses > 1:  # We have at least 1 full cycle
                high_pulse, low_pulse = pwm_in[0], pwm_in[1]

                # correct pulse if necessary
                high_pulse, low_pulse = self.correct_pulse(high_pulse, low_pulse, channel)
            
            # clear out read pulses
            for _ in range(num_pulses):
                pwm_in.popleft()
        
        except RuntimeError as e:
            print("Failed to read from channel", channel, "with error:", str(e))
        
        return high_pulse
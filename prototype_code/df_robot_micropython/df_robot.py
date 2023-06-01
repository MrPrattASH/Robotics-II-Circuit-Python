from microbit import i2c, sleep
from math import floor

#registers
PCA9685_ADDRESS = 0x40
MODE1 = 0x00
MODE2 = 0x01
SUBADR1 = 0x02
SUBADR2 = 0x03
SUBADR3 = 0x04
PRESCALE = 0xFE
LED0_ON_L = 0x06
LED0_ON_H = 0x07
LED0_OFF_L = 0x08
LED0_OFF_H = 0x09
ALL_LED_ON_L = 0xFA
ALL_LED_ON_H = 0xFB
ALL_LED_OFF_L = 0xFC
ALL_LED_OFF_H = 0xFD

#stepper motor calibrations? Assuming from STP
STP_CHA_L = 2047
STP_CHA_H = 4095

STP_CHB_L = 1
STP_CHB_H = 2047

STP_CHC_L = 1023
STP_CHC_H = 3071

STP_CHD_L = 3071
STP_CHD_H = 1023

#unsure calibrations 
BYG_CHA_L = 3071
BYG_CHA_H = 1023

BYG_CHB_L = 1023
BYG_CHB_H = 3071

BYG_CHC_L = 4095
BYG_CHC_H = 2047

BYG_CHD_L = 2047
BYG_CHD_H = 4095

# Bits: (unsure if all are needed?)
RESTART            = 0x80
SLEEP              = 0x10
ALLCALL            = 0x01
INVRT              = 0x10
OUTDRV             = 0x04
RESET              = 0x00

Servos = {
 'S1': 0x08,
 'S2': 0x07,
 'S3': 0x06,
 'S4': 0x05,
 'S5': 0x04,
 'S6': 0x03,
 'S7': 0x02,
 'S8': 0x01
 }

Motors = {
 'M1': 0x1,
 'M2': 0x2,
 'M3': 0x3,
 'M4': 0x4
 }


Dir = {
        'CW': 1,
        'CCW': -1
    }

class df_robot:
    '''attempted convert dfrobot motor controller to micropython''' 
    #taken from https://github.com/gingemonster/PCA9685-Python-Microbit/blob/master/PCA9685.py
    #new Init code
    def __init__(self, i2c, address=PCA9685_ADDRESS):
        """Initialize the PCA9685. should* be modelled off of DF_robot and modifed from beside"""
        self.address = address
        i2c.write(self.address, bytearray([MODE1, RESET])) # reset seems to be what DF_robot does initially? 

    def set_pwm_freq(self, freq_hz):
        """Set the PWM frequency to the provided value in hertz, constrained"""
        prescaleval = 25000000.0    # 25MHz
        prescaleval /= 4096.0       # 12-bit
        prescaleval /= float(freq_hz)
        prescaleval -= 1.0

        prescale = int(floor(prescaleval + 0.5))
        oldmode = i2c.read(self.address, MODE1) #maybe byte array? maybe '1' for MODE1
        oldmode = int.from_bytes(oldmode, 'big')
        newmode = (oldmode & 0x7F) | 0x10    # sleep 
        i2c.write(self.address, bytearray([MODE1, newmode]))
        i2c.write(self.address, bytearray([PRESCALE, prescale]))
        i2c.write(self.address, bytearray([MODE1, oldmode]))
        sleep(5000)
        i2c.write(self.address, bytearray([MODE1, oldmode | 0xa1]))

    #normal setPWM
    def set_pwm(self, channel, on, off):
        if channel < 0 or channel > 15:
            return None
        buf = bytearray(5)
        buf[0] = LED0_ON_L + 4 * channel
        buf[1] = on & 0xff
        buf[2] = (on >> 8) & 0xff
        buf[3] = off & 0xff
        buf[4] = (off >> 8) & 0xff
        i2c.write(self.address, buf)

    def servo(self, index:str, degree:int):
        #controls a servo
        # min 0, max 180
        #S1-S8
        if index in Servos:
            new_index = Servos[index]
        else:
            return None
        v_us = (degree * 1800 // 180 + 600) #0.6ms - 2.4ms
        value = v_us * 4096 // 20000
        self.set_pwm(new_index + 7, 0, value)

    def MotorRun(self, index, direction, speed):
        #Set M1-M4 address
        if index in Motors:
            new_index = Motors[index]
        else:
            return None
        
        #set 1/-1 for CW/CCW motor movement respectively
        if direction in Dir:
            new_dir = Dir[direction]
        else:
            return None

        speed = speed * 16 * new_dir #map 255>4096
        if speed >= 4096:
            speed = 4095
        elif speed <= -4096:
            speed = -4095
        
        pn = (4 - new_index) * 2
        pp = (4 - new_index) * 2 + 1
        if speed >= 0:
            self.set_pwm(pp, 0, speed)
            self.set_pwm(pn, 0, 0)
        else:
            self.set_pwm(pp, 0, 0)
            self.set_pwm(pn, 0, -speed)

    def motor_stop(self, index):
        if index in Motors:
            new_index = Motors[index]
        else:
            return None
        self.set_pwm((4 - new_index) * 2, 0, 0)
        self.set_pwm((4 - new_index) * 2 + 1, 0, 0)

    def motor_stop_all(self):
        for idx in range(1, 5):
            key = 'M' + str(idx)
            self.motor_stop(Motors[key])

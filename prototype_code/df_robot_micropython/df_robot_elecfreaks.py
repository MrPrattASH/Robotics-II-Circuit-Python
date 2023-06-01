from microbit import *

#registers
PCA9685_ADDRESS = 0x40

class df_robot(object):
    '''attempted convert dfrobot motor controller to micropython''' 
    #taken from https://github.com/gingemonster/PCA9685-Python-Microbit/blob/master/PCA9685.py
    #new Init code
    def __init__(self):
        i2c.init()

    def set_motors(self,motor,speed):
        if speed < 0:
            i2c.write(PCA9685_ADDRESS, bytearray([motor, 0x02, speed * -1, 0]))
        else:
            i2c.write(PCA9685_ADDRESS, bytearray([0x06 + 4 * channel, 0x01, speed, 0]))

if __name__ == '__main__':
    df = df_robot()
    df.set_motors(1,100)
import board
import busio
import time
import adafruit_apds9960.apds9960
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True
sensor.enable_color = True
sensor.enable_gesture = True

while True:
    
    line = sensor.proximity # no parenthesis
    r,g,b,c = sensor.color_data
    print("prox", line, "Red: {0}, Green {1}, Blue: {2}, Clear: {3}".format(r,g,b,c))
    
    gesture = sensor.gesture()
    #print("Raw gesture data:", gesture)
    if gesture == 0x01:
        print("up")
    elif gesture == 0x02:
        print("down")
    elif gesture == 0x03:
        print("left")
    elif gesture == 0x04:
        print("right")
    #time.sleep(0.1)
    

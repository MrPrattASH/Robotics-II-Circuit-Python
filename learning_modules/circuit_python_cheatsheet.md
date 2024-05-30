# Circuit Python Cheatsheet
Common code needed in robotics, as a reference for you. Keep this open as you program. Original cheat sheet from Adafruit[here](https://github.com/adafruit/awesome-circuitpython/blob/main/cheatsheet/CircuitPython_Cheatsheet.md)

## Digital I/O
Used for initializing new sensors, objects, motors, etc. 
```
    import board
    from digitalio import DigitalInOut, Direction, Pull

    led = DigitalInOut(board.D13)
    led.direction = Direction.OUTPUT # output for motors/lights

    switch = DigitalInOut(board.D5)
    switch.direction = Direction.INPUT # input for sensors
    switch.pull = Pull.UP   # Pull.Up/Down is used for switches

    while True:
        led.value = not switch.value
        time.sleep(0.01)
```
## Analog Input
This can be handy for converting incoming RC signals as PWM values. 

```
    import time
    import board
    from analogio import AnalogIn

    analog_in = AnalogIn(board.A1)

    def get_voltage(pin):
        return (pin.value * 3.3) / 65536

    while True:
        print((get_voltage(analog_in),))
        time.sleep(0.1)
```
Analog input values are always 16 bit (i.e. in range(0, 65535)), regardless of the converter's resolution. The get_voltage function converts the analog reading into a voltage, assuming the default 3.3v reference voltage. (10K Pot's should use 5v)

## Analog Output
```
    import board
    from analogio import AnalogOut

    analog_out = AnalogOut(board.A0)

    while True:
        # Count up from 0 to 65535
        for i in range(0, 65536):
            analog_out.value = i
```
Analog output values are always 16 bit (i.e. in range(0, 65535)). Depending on the underlying hardware those values will get scaled to match the resolution of the converter.
The example will generate a stairstepped signal, the number of steps depends on the resolution of the converter. E.g. the 10-bit converter in the SAMD21 will create 1024 steps, while the 12-bit converter on the SAMD51 will create 4096 steps.

## Servo - High Level Control
```import time
    import board
    import pwmio
    from adafruit_motor import servo

    # Create a positional servo object, my_pos_servo.
    pwm0 = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50)
    my_pos_servo = servo.Servo(pwm0)

    # Create a rotational servo object, my_servo.
    pwm1 = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50)
    my_rot_servo = servo.ContinuousServo(pwm1) 

    while True:
        #basic servo sweep
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
            my_pos_servo.angle = angle
            time.sleep(0.05)
        for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
            my_pos_servo.angle = angle
            time.sleep(0.05)
        
        #spin rot. servo full forward
        my_rot_servo.throttle = 1.0
        time.sleep(1)

        #stop rot. servo
        my_rot_servo.throttle = 0
        time.sleep(1)

        #spin rot. servo full reverse
        my_rot_servo.throttle = -1.0
        time.sleep(1)
```

## PWM Motors - Low Level Controls
Fixed frequency PWM with variable duty cycle. This is useful for controllign the brightness of a LED, the speed of a motor, or sending an RC signal. 

```import time
    import board
    import pwmio

    led = pwmio.PWMOut(board.D13, frequency=5000, duty_cycle=0)

    while True:
        for i in range(100):
            # PWM LED up and down
            if i < 50:
                led.duty_cycle = int(i * 2 * 65535 / 100)  # Up
            else:
                led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
            time.sleep(0.01)
```

## PWM Speakers
With variable frequency. This is handy for producing tones on speakers. The duty cycle effects the sound (as opposed to the note).

```import time
    import board
    import pwmio

    piezo = pwmio.PWMOut(board.A1, duty_cycle=0, frequency=440, variable_frequency=True)

    while True:
        for f in (262, 294, 330, 349, 392, 440, 494, 523):
            piezo.frequency = f
            piezo.duty_cycle = 65536 // 2  # On 50%
            time.sleep(0.25)  # On for 1/4 second
            piezo.duty_cycle = 0  # Off
            time.sleep(0.05)  # Pause between notes
        time.sleep(0.5)
```

## PWM Duty Cycle Conversion
You can make a handy Python function to more easily set PWM duty cycle. For example given a value from 0.0 to 1.0 (0 to 100%) it can compute the necessary duty cycle value for you: [Original Tutorial from AdaFruit](https://learn.adafruit.com/circuitpython-basics-analog-inputs-and-outputs/pulse-width-modulation-outputs)

```
def duty_cycle_value(percent):
    return int(percent * 65535)
YOURDEVICE.duty_cycle = duty_cycle_value(0.5)  # Set 50% duty cycle!
```

## NeoPixels 
```
    import time
    import board
    import neopixel

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    pixel_pin = board.A1
    num_pixels = 8

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

    pixels.fill(RED)
    pixels.show()

    #The usual slicing operations can be used
    pixels[1:6:2] = GREEN
    pixels[7] = BLUE
    pixels.show()
```         
## OLED Display 
```
    import board, displayio

    bitmap = displayio.Bitmap(320, 240, 3)
    bitmap[0, 0] = 0
    palette = displayio.Palette(1)
    palette[0] = 0xFFFFFF
    tilegrid = displayio.TileGrid(bitmap, pixel_shader = palette)
    group = displayio.Group()
    group.append(tilegrid)
    board.DISPLAY.show(group)

    # Ctrl+D and any key to re-enter the REPL on-screen
```


# MONO OLED 128x64 i2C tutorial

This tutorial was originaly taken from ADAFruit [here](https://learn.adafruit.com/monochrome-oled-breakouts/circuitpython-setup) and has since been modified to include documentation for only the Metro M4 Express board.

## Installing Libraries

Before beginning, you will need 3 relevant libraries that will do a lot of the heavy lifting for us. Install these to your M4 lib folder They are located in the folders/files above. Be sure to download the entire folder contents for the bottom 2, not just the .mpy files. (unsure how to download files from GitHub? See [these instructions](https://www.itprotoday.com/development-techniques-and-management/how-do-i-download-files-github)):
* adafruit_displayio_ssd1306 (single mpy file)
* adafruit_bus_device (folder)
* adafruit_display_text (folder)

## Wiring Diagram
![oled](https://user-images.githubusercontent.com/101632496/187387302-fb97456a-efc9-4922-b8dd-6fb14d7c4ccb.png)
* We will use this board in i2C mode, NOT SDI mode
* Use 3.3V only, connected to VIN pin.

It's easy to use OLEDs with Python and the Adafruit CircuitPython DisplayIO SSD1306 module. This module allows you to easily write Python code to control the display.

To demonstrate the usage, we'll initialize the library and use Python code to control the OLED from the board's Python REPL.

## Example Code
```python
import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

displayio.release_displays()

oled_reset = board.D9

# Use for I2C
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=oled_reset)

WIDTH = 128
HEIGHT = 64  # Change to 32 if needed
BORDER = 5

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

for i in range(5):
    print("index:", i)
    time.sleep(1)

```

***

## Code Explained

Let's take a look at the sections of code one by one. We start by importing the board so that we can initialize SPI, displayio,terminalio for the font, a label, and the adafruit_displayio_ssd1306 driver.
```python
import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
```

Next we release any previously used displays. This is important because if the microprocessor is reset, the display pins are not automatically released and this makes them available for use again.

```python
displayio.release_displays()
```
Next we define the reset line, which will be used for either SPI or I2C.

```python
oled_reset = board.D9
```

We set the I2C object to the board's I2C with the easy shortcut function board.I2C(). By using this function, it finds the SPI module and initializes using the default SPI parameters. We also set the display bus to I2CDisplay which makes use of the I2C bus.

### What is i2c?
I²C (Inter-Integrated Circuit) is a simple communication protocol that allows multiple electronic devices to exchange data using just two wires: SDA (data line) and SCL (clock line). It follows a master-slave structure, where a master device (like a microcontroller) controls communication with multiple slave devices (like sensors or displays), each identified by a unique address. The master sends a start signal, selects a slave, exchanges data, and then stops communication. 

I²C is widely used because it minimizes wiring, supports multiple devices on the same bus, and is efficient for connecting multiple peripherals over the same ports, rather than needing a spare Digital port for every sensor!

```python
# Use for I2C
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=oled_reset)
```

In order to make it easy to change display sizes, we'll define a few variables in one spot here. We have the display width, the display height and the border size, which we will explain a little further below. If your display is something different than these numbers, change them to the correct setting.

```python
WIDTH = 128
HEIGHT = 64    
BORDER = 5
```
Finally, we initialize the driver with a width of the WIDTH variable and a height of the HEIGHT variable. If we stopped at this point and ran the code, we would have a terminal that we could type at and have the screen update.

```python
for i in range(5):
    print("index:", i)
    time.sleep(1)
```

We now put in a simple for loop to be able to see our screen up and running. Now we have a far more useful debugging console build directly into our robot! 


# Extended Learning
want to do more advanced things with this OLED? Check out this page [here](https://learn.adafruit.com/circuitpython-display-support-using-displayio)

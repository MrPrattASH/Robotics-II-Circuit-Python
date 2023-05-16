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
Start with the *display_splash.py* above
```
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
HEIGHT = 32  # Change to 64 if needed
BORDER = 5

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)
```

## I2C Initialization
If your display is connected to the board using I2C you'll first need to initialize the I2C bus. First import the necessary modules:
```
import board
```
Now for either board run this command to create the I2C instance using the default SCL and SDA pins:
```
i2c = board.I2C()
```
After initializing the I2C interface for your firmware as described above, you can create an instance of the I2CDisplay bus:

```
import displayio
import adafruit_displayio_ssd1306
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d)
```

Finally, you can pass the display_bus in and create an instance of the SSD1306 I2C driver by running:

```
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
```

Now you should be seeing an image of the REPL. Note that the last two parameters to the SSD1306 class initializer are the width and height of the display in pixels.  Be sure to use the right values for the display you're using!

Now, pause and play with your REPL in your serial console. what happens when you type? 

## Code Explained

Let's take a look at the sections of code one by one. We start by importing the board so that we can initialize SPI, displayio,terminalio for the font, a label, and the adafruit_displayio_ssd1306 driver.
```
import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
```

Next we release any previously used displays. This is important because if the microprocessor is reset, the display pins are not automatically released and this makes them available for use again.

```
displayio.release_displays()
```
Next we define the reset line, which will be used for either SPI or I2C.

```
oled_reset = board.D9
```

We set the I2C object to the board's I2C with the easy shortcut function board.I2C(). By using this function, it finds the SPI module and initializes using the default SPI parameters. We also set the display bus to I2CDisplay which makes use of the I2C bus.
```
# Use for I2C
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=oled_reset)
```

In order to make it easy to change display sizes, we'll define a few variables in one spot here. We have the display width, the display height and the border size, which we will explain a little further below. If your display is something different than these numbers, change them to the correct setting.

```
WIDTH = 128
HEIGHT = 64    
BORDER = 5
```
Finally, we initialize the driver with a width of the WIDTH variable and a height of the HEIGHT variable. If we stopped at this point and ran the code, we would have a terminal that we could type at and have the screen update.

## Example Code

Now, download the full_text_example.py to your board. 

```
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)
adafruit_products_repl.jpeg
```
Next we create a background splash image. We do this by creating a group that we can add elements to and adding that group to the display. In this example, we are limiting the maximum number of elements to 10, but this can be increased if you would like. The display will automatically handle updating the group.
```
splash = displayio.Group(max_size=10)
display.show(splash)
```
Next we create a Bitmap that is the full width and height of the display. The Bitmap is like a canvas that we can draw on. In this case we are creating the Bitmap to be the same size as the screen, but only have one color. Although the Bitmaps can handle up to 256 different colors, the display is monochrome so we only need one. We create a Palette with one color and set that color to 0xFFFFFF which happens to be white. If were to place a different color here, displayio handles color conversion automatically, so it may end up black or white depending on the calculation.

```
color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF # White
```
With all those pieces in place, we create a TileGrid by passing the bitmap and palette and draw it at (0, 0) which represents the display's upper left.

```
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)      
splash.append(bg_sprite)
```
![image](https://user-images.githubusercontent.com/101632496/187388907-13379230-3608-49ae-8617-671c2977b9c5.png)

Next we will create a smaller black rectangle. The easiest way to do this is to create a new bitmap that is a little smaller than the full screen with a single color of 0x000000, which is black, and place it in a specific location. In this case, we will create a bitmap that is 5 pixels smaller on each side. This is where the BORDER variable comes into use. It makes calculating the size of the second rectangle much easier. The screen we're using here is 128x64 and we have the BORDER set to 5 , so we'll want to subtract 10 from each of those numbers.

We'll also want to place it at the position (5, 5) so that it ends up centered.

```
# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(WIDTH-BORDER*2, HEIGHT-BORDER*2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000 # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER)
splash.append(inner_sprite)
```
Since we are adding this after the first square, it's automatically drawn on top. Here's what it looks like now.
![image](https://user-images.githubusercontent.com/101632496/187389002-fda19626-3632-464e-a20d-3ffa7c1620d1.png)

Next add a label that says "Hello World!" on top of that. We're going to use the built-in Terminal Font. In this example, we won't be doing any scaling because of the small resolution, so we'll add the label directly the main group. If we were scaling, we would have used a subgroup.

Labels are centered vertically, so we'll place it at half the HEIGHT for the Y coordinate and subtract one so it looks good. We use the // operator to divide because we want a whole number returned and it's an easy way to round it. We'll set the width to around 28 pixels make it appear to be centered horizontally, but if you want to change the text, change this to whatever looks good to you. Let's go with some white text, so we'll pass it a value of 0xFFFFFF.

```
# Draw a label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=HEIGHT//2-1)
splash.append(text_area)
```
Finally, we place an infinite loop at the end so that the graphics screen remains in place and isn't replaced by a terminal.
```
while True:
    pass
```

![image](https://user-images.githubusercontent.com/101632496/187389108-7077c5ac-950a-4974-8a2a-84c0e8581599.png)

# Extended Learning
want to do more advanced things with this OLED? Check out this page [here](https://learn.adafruit.com/circuitpython-display-support-using-displayio)

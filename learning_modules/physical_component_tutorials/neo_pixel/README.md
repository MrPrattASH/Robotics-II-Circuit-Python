# Programming the Onboard NeoPixel (P40)

**Note, this tutorial has been heavily modified from the fantastic M4 tutorial [here](https://learn.adafruit.com/adafruit-metro-m4-express-featuring-atsamd51/circuitpython-neopixel), but updated for circuitpy 7.3.2, and specifially changed for the M4 board.**

## The Code
This example includes multiple visual effects.

To use with CircuitPython, you need to first install a few libraries, into the lib folder on your CIRCUITPY drive. Then you need to update code.py with the example script. Install the neopixel library now if you have not dones so. 

Start this code following along from the "onboard_neopixel.py" file (located above) 

## Create the LED
The first thing we'll do is create the LED object. The NeoPixel object has two required arguments and two optional arguments. You are required to set the pin you're using to drive your NeoPixels and provide the number of pixels you intend to use. You can optionally set brightness and auto_write.

NeoPixels can be driven by any pin. We've chosen NEOPIXEL (as this is the onboard neopixel). To set the pin, assign the variable pixel_pin to the pin you'd like to use, in our case board.NEOPIXEL

To provide the number of pixels, assign the variable num_pixels to the number of pixels you'd like to use. In this example, we're using a strip of 8.

We've chosen to set brightness=0.3, or 30%.

By default, auto_write=True, meaning any changes you make to your pixels will be sent automatically. Since True is the default, if you use that setting, you don't need to include it in your LED object at all. We've chosen to set auto_write=False. If you set auto_write=False, you must include pixels.show() each time you'd like to send data to your pixels. This makes your code more complicated, but it can make your LED animations faster!

## NeoPixel Helpers
Next we've included a few helper functions to create the super fun visual effects found in this code. First is wheel() which we just learned with the Internal RGB LED. Then we have color_chase() which requires you to provide a color and the amount of time in seconds you'd like between each step of the chase. Next we have rainbow_cycle(), which requires you to provide the mount of time in seconds you'd like the animation to take. Last, we've included a list of variables for our colors. This makes it much easier if to reuse the colors anywhere in the code, as well as add more colors for use in multiple places. Assigning and using RGB colors is explained in this section of the CircuitPython Internal RGB LED page.

## Main Loop
Thanks to our helpers, our main loop is quite simple. We include the code to set every NeoPixel we're using to red, green and blue for 1 second each. Then we call color_chase(), one time for each color on our list with 0.1 second delay between setting each subsequent LED the same color during the chase. Last we call rainbow_cycle(0), which means the animation is as fast as it can be. Increase both of those numbers to slow down each animation!

Note that the longer your strip of LEDs, the longer it will take for the animations to complete.

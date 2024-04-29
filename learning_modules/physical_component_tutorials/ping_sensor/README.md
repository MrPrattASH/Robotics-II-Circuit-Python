# Using a Ping Sensor in CircuitPython

This tutorial will teach you how to use a ping sensor (in our case, a "SonarBit" branded ping sensor) on a M4 board. 

Start by copying the sonarbit.py code above onto your code.py file on your M4. 

## Code Explanation

Firstly, we import all revelant libraries. Math will be important for later. 

```
""" Sonarbit Distance Program."""

import time
import board
import digitalio
from math import floor
```

Now, we define a new function for getting our distance. Unlike an ultrasonic sensor used on a hummingbird:bit, that had 1 pin for send, and 1 pin for recieve, the ping sensor uses the *same pin* for both send and recieve. This requires some tricky programming to get working in CircuitPython.

Something else to note is the triple quote at the start. this is called a "docstring" and it is documentation for your function. What variables your function takes, what it does, and how to use the function. It's good practice to use this inside your future functions. 

```
def sonar(pin):
    ''' Get a ping reading from 5cm>568cm from the Elecfreaks Ping Sensor. Trigger & Echo are on the 'same pin'. 
    pin = the pin with the ping sensor
    returns: Distance in cm between 0 & 568

    Note: Introduce a 0.05sec delay when taking sensor readings in CircuitPython. The ping sensor board cannot take readings quicker than this, otherwise there is not enough time created between send and recieve commands. 
    
    '''
```

This lambda is sort of a "function inside a function", essentially, it is a "variable function", one that we won't call outside of this function itself, but a calculation we'll need to use a lot inside this code. This converts an integer value into a *microsecond* rather than millisecond, as the ping sensor waits for microseconds. 
```
    usleep = lambda x: x/1000000
```

Here, we assign the pin as an output pin in order to send the signal that we will then listen for later in order to check distance to our object. We need to send these signals at a very specific frequency and timing, so we use the left side speaker to send out these signals. 
```
    pin.direction = digitalio.Direction.OUTPUT

    #send trigger signal
    pin.value = 0
    usleep(2)
    pin.value = 1
    usleep(10)
    pin.value = 0
```

We now **reassign** the same pin as an input, in order to be able to listen for our trigger signal that we send above. We use time.monotonic to be able to continue to listen for our signal and "do other things" while our timer is running. In this case, we are listening for our pin.value to return True, that we have indeed recieved back our signal. (If we never receive a signal, the sensor will time out, return max range, and give a return value of 1.) 

We calculate our start time for when we begin listening, and our end time for when we actually recieve the signal. We'll use these variables below to calcualte distance. 
```
    #recieve echo signal
    pin.direction = digitalio.Direction.INPUT
    while pin.value == 0:
        start_time = time.monotonic_ns()

    while pin.value == 1:
        end_time = time.monotonic_ns()
```

Lastly, we check our distance to the object based on how long it took for the sent the sound signals to return and be heard. First, we try to calculate the distance as time/2 * the speed of sound (34,000 cm/s). We must divide time/2 as we are actually calculating the time that the signal takes to be sent out, then returned, and we only need to calculate the distance of *half* of this measurement, as otherwise we would be double measuring. We use floor here to return an integer value, rather than float, as our sensor realistically is accurate to +/- 1cm, and is not accurate to a floating decimal point, so returning a float is pointless. 

We use a try statement here, as sometimes an object can be under 5cm away from the sensor. When this happens, the signal doesn't have enough time to be sent and recieved, causing our end time to be < than start time. When this is true, start time is never assigned above, and we get an error that "start time has not been defined", and this breaks out program. To solve this, we use an except statement, meaning that if our try doesn't work, or returns an error, our program will print "object too close" and return a distance of 0. 

Finally, we return the distance value as an integer, in cm. 
```
    #If an object is too close, start_time will never be assigned because pin.value will never equal 0, causing a variable assignment error & crash. 
    try:
        # Distance is defined as time/2 (there and back) * speed of sound 34000 cm/s
        distance = floor((end_time - start_time) * 34000/2/1000000000)
    except:
        print("object too close")
        distance = 0
    
    return distance
```

Below is the code working in your main loop. 
```
pin = digitalio.DigitalInOut(board.D2)
while True:
    print("the object is " + str(sonar(pin)) + " cm away")
    time.sleep(0.5)
```

That's it! 

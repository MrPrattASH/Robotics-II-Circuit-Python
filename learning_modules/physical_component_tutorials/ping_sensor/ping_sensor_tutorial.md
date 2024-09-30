# Distance (Ping) Ultrasonic Sensor

An Ultrasonic Distance Sensor is a device that measures the distance to an object by emitting ultrasonic sound waves and listening for the echoes that bounce back. This process is similar to sonar and radar.

## Wiring
An Ultrasonic Ping sensor has three key wires:

* Signal: The wire responsible for sending and receiving ultrasonic signals.
* Power: Provide 5V OR 3.3V power to the sensor.
* Ground: Provide a ground back to your microcontroller.

![ping_wiring](ping_sensor_wiring.png)

     

## Adding Required Libraries

Make sure you have added the [sonarbit.py](sonarbit.py) library to the lib folder on your CircuitPython device. This library contains the necessary functions to interact with the ultrasonic sensor.

## Code

python code [here](sonarbit_example.py)
```python
# Sonarbit_class Example
# SPDX-FileCopyrightText: 2024 Brogan Pratt
#
# SPDX-License-Identifier: MIT

import board
from sonarbit import Sonarbit
import time

distance_sensor = Sonarbit(board.D2)

prev_distance= 570  # Initial value

while True:
    distance = distance_sensor.get_distance(prev_distance)
    print("The object is: " + str(distance) +  " cm away")

    prev_distance = distance
    time.sleep(1)
```


## Code Breakdown

### Imports:
```python
import board
from sonarbit import Sonarbit
import time
```

* board: Provides access to the specific pins on the microcontroller.
* sonarbit: Custom library to interface with the Sonarbit sensor.
* time: Module for adding delays between measurements.

### Initialize the Sensor:

`distance_sensor = Sonarbit(board.D2)`

* Creates an instance of the Sonarbit class on digital pin D2, allowing you to interact with the sensor. 
* In programming, an instance is part of a class. A *class* is a blueprint for creating objects (a particular data structure). A class defines a set of attributes (characteristics) and methods (behaviors) that the created objects will have. It allows for bundling data and functionality together.
* In our case, we have a single *instance* (one version) of an ultrasonic sensor class. This class has 1 method, "distance". A function we can call to get the distance from the sensor. 

### Initial Value:

`prev_distance = 570  # Initial value`
* Sets an initial previous distance value, otherwise when we call the first "distance" without assigning a value, we'll throw an error.

### Main Loop:

```python
while True:
    distance = distance_sensor.get_distance(prev_distance)
    print("The object is: " + str(distance) +  " cm away")

    prev_distance = distance
    time.sleep(1)
```

* while True: Creates an infinite loop that continuously runs.
* distance_sensor.get_distance(prev_distance=prev_d): Calls a method from the Sonarbit class to get the current distance measurement, using the previous distance for accuracy improvement cancelling out false low/high readings.
* print("The object is: " + str(distance) + " cm away"): Prints the measured distance to the serial console.
* prev_distance = distance: Updates the prev_distance variable with the current distance for the next iteration.
* time.sleep(1): Adds a 1-second delay before the next measurement, to avoid overwhelming the sensor with requests.

## Sonarbit Class

* What is a "Class"?:
    * The Sonarbit class (defined in the sonarbit.py library) acts as a blueprint for the ultrasonic sensor.
* Constructor Method (creating a class instance):
    * When Sonarbit(board.D2) is called, the __init__ method in the Sonarbit class is executed. This sets up the sensor on the pin D2.
* Methods:
    * get_distance(prev_distance=prev_d) is a method of the Sonarbit class that interacts with the sensor to get the current distance measurement. Methods are functions for class objects. 
* Instance:
    * distance_sensor is an instance of the Sonarbit class. It represents one specific ultrasonic sensor connected to the microcontroller.

# Attaching Multiple Distance Sensors

### Wiring
Wiring is the same as one sensor, but simply add in a second sensor to a different digital pin. 

### Code
* Rather than initialize a single instance of our sonarbit, we simply initialize 2 instances. 
* Note, we need to now double up on our variables for each respective sensor. 
* Note, the method calls remain the same, as we're calling them from difference instances of the class. 

```python
# Sonarbit_class Example
# SPDX-FileCopyrightText: 2024 Brogan Pratt
#
# SPDX-License-Identifier: MIT

import board
from sonarbit import Sonarbit
import time

distance_sensor1 = Sonarbit(board.D2)
distance_sensor2 = Sonarbit(board.D3)

prev_distance1= 570  # Initial value
prev_distance2= 570  # Initial value

while True:
    distance1 = distance_sensor1.get_distance(prev_distance)
    distance2 = distance_sensor2.get_distance(prev_distance)

    print("The object from #1 is: " + str(distance1) +  " cm away")
    print("The object from #2 is: " + str(distance2) +  " cm away")

    prev_distance1 = distance1
    prev_distance2 = distance2
    time.sleep(1)
```

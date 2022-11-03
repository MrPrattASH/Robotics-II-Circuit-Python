# CircuitPython - FlySky FS-I6X Controller - FS-iA6B Reciever

This tutorial will serve as a reference for setting up the FlySky FS-i6X transmitter and FS-iA6B reciever with a metro M4 device. Theoretically, this should work for just about any RC controller that is capable of outputting a PWM signal.

# RC Intended output

- CH1 - Right joystick, Left/Right Control
- CH2 - Right joystick, Up/Down Control
- Ch3 - Left joystick, Left/Right Control
- CH4 - Left joystick, Up/Down Control
- CH5 - SWB, 2 way toggle switch
- CH6 - SWC, 3 way toggle switch

Eventually, we will drive the robot throttle with CH2, and steer with CH1. CH3/4 will likely not be used, and CH 5/6 will be used for various mechanisms attached to our robot. 

# Powering on switch states
- All toggle switches should be pushed UP, the OFF state
- Right joystick should auto centre, as it is spring loaded
- Left joystick should be pulled all the way down


![Screen Shot 2022-10-18 at 20 25 43](https://user-images.githubusercontent.com/101632496/196513614-dd92db1c-323c-43ee-bb24-fdf60ac65196.png)

## Main Tutorial Credits & Documentation
Much of this tutorial is taken from several different sources. I include them here for future reference, as CircuitPython documentation is sparse online. 
- [Main Instruction manual for the FS-i6X controller](https://files.banggood.com/2016/09/FS-i6X%20User%20manual.pdf)
- [An amazing tutorial on setting up the controller by Run Amok Combat Robotics](http://runamok.tech/RunAmok/flysky_i6.html#modes). I have modified a decent portion of this tutorial to only provide relevant material here. 
- [this random thread from 2021 on a raspberryPi forum](https://forums.raspberrypi.com/viewtopic.php?t=308269) that provided the necessary PseudoCode for translating PWM into a useable signal. (April 01,2021 8:03am post)

# Setting initial settings on the Transmitter
First, Put x4 AA into the transmitter & power it on. 

## Change AUX Switches
We need to change some default settings. Default AUX switches are VRA & VRB, x2 analog dials. We instead want to switch these over to SWC (3 way toggle switch) and SWB, a 2 way toggle switch. Since we'll only use the right joystick for robot control, there is no need to have x4 analog sensors that we won't use, so instead we'll create 2 switches and 2 analog sensors. 

1. power on the transmitter
2. press and hold 'OK' key to enter the menu screen
3. highlight "System", press 'OK' key
4. tap 'Down' key until the "AUX Switches". press 'OK' Key
5. on this screeen, Up/Down turns on/off the current selection. Use 'OK' to cycle through options until you have the following settings:
- SwA: Off
- SwB: On
- SwC: On
- SwD: Off
- VrA: Off
- VrB: Off
- Ch: 6
6. press and hold 'CANCEL' to save settings. (I know, holding cancel = save)
7. press cancel again to return to the main menu
8. press 'DOWN' key and select 'Functions Setup'. press 'OK'
9. press 'DOWN' until 'Aux. Channels' is selected. press 'OK'
10. with Channel 5 selected, press 'DOWN' to select SwB. press 'OK'
11. with Channel 6 selected, press 'DOWN' to select SwC. press and hold 'CANCEL' to save settings
12. press cancel x2 to exit the menu. AUX channels are now set. 

## Correct Failsafe
(credit to runamok source)
We need to create a Failsafe for our transmitter. If for whatever reason our transmitter stops sending signals, our reciever will default to OFF, rather than continuing to fly/run away on us. The default failsafe 'Off' setting will lock the selected channel in the last setting it had before the transmitter signal was lost. That is not an acceptable response for a combat robot! Turning failsafe 'On' will return a receiver port to a pre-selected safe setting that will bring all motion on the robot to a stop -- a correct failsafe response.

1. Back at the 'MENU' Screen
2. Tap the 'Down' key to highlight 'System setup' -- tap 'OK' to select.
3. Use the 'Down' key to scroll down the list to 'RX Setup' -- tap 'OK' to select.
4. Use the 'Down' key to scroll down the list to 'Failsafe' -- tap 'OK' to select.
5. Pull the left stick all the way down, and leave the other stick axis spring centered.
6. Tap 'OK' to select channel 1, tap 'Down' to turn failsafe 'On', then 'OK' to return to channel selection. Tap 'Down' to the next channel and repeat for channels 2, 3 and 4. Your screen should look like:
- Channel 1: 0%
- Channel 2: 0%
- Channel 3: -99%
- Channel 4: 0%
- Channel 5: Off
- Channel 6: Off

8. With all channels correctly set, press and hold 'Cancel' to exit and save the failsafe settings.
9. Tap 'Cancel' three times to step back to the status display screen

# Wiring the Reciever
It is important to know that the receiver outputs a 5V signal. However, our CircuitPython board logic pins are only 3.3V, so we need to use a device called a LevelShifter, or Voltage changer, to shift 5V logic down to 3.3V logic. The level shifter we're using in our class is bi-directional, meaning that it can convert both High > low voltage, and vice-versa. We need to wire an input voltage, 5V to the A or B side, an output voltage (3.3V) to the opposing side, and connect the GND to our M4. Then, we can easily convert A1 > B1 voltage, or B2 > A2 voltage, and so in. In our case, we'll input 5V to the B side, and output 3.3V to the A side. 

![RC_WIRING_diagram_fix](https://user-images.githubusercontent.com/101632496/196914475-a4d45ae9-17f8-4dcd-a750-b5233a771c3b.png)

# Sample Code
In the folders above are 3 sample programs
- rc_analog_channel_read shows you how to read a single analog channel, and output whatever the potentiometer joystick is currently reading
- rc_toggle_switches shows you how to read a single analog channel, and output whatever state the toggle switch is currently in
- rc_full_example shows a fully wired transmitter, with all 6 channels populated & programmed. 

# Calibration of Joysticks "SubTrim"
Joysticks are unfortunately not all made the same. Some centre points are different than others, and this means that you'll output a different PWM value depending on what controler you are using. Additionally, overtime joystick springs will relax and change their calibrated centre points. Likely, you'll need to calibrate the joysticks overtime to gain more accurate readings. Upon initial setup, you'll also need to calibrate the joysticks, and fiddle with the below settings. You may also notice that your wheels "twitch" at stop, this is also a good time to calibrate the joysticks "SubTrim" 

*Note: If your robot will not use the left-joystick, there is no need to follow these steps for channels 3/4. 

### Setting up to Calibrate the Deadpoint
1. Open rc_full_example.py and download this to your code.py file on the M4. 
2. Modify your pin initializations to read the correct channels for your wiring. 
3. Modify line 58's print statement as below and save this to your M4:
```
    print(" X_Joy: " + str(x_cur) + " Y:Joy " + str(y_cur))
```
4. On your controller, Centre the right joystick and look at the serial printout statements. Your goal is to have only 0 displaying (or the odd false-high every 5-8 readings or so), such as:
```
0
0
0
0
0.234892
0
0
0
0
```
If your controller is outputing 0 consistently , great! You don't need to do the below steps. If you're jumping between a postive number, or negative number and 0, you need to:

### Centering the RC Deadpoint (Ch1, Ch2)
1. press and hold 'OK' to enter the menu
2. press 'DOWN' to select the 'Functions Setup'. press 'OK'
3. press 'DOWN' to select 'Subtrim' press 'OK'
4. press 'OK' to select the correct channel (1 for X_joy, 2 for Y_joy). If your serial output is bouncing between a negative value and 0, hold 'DOWN' to move the centre subtrim to the left. Vice versa if your serial value is presenting positive.
5. As you press 'DOWN' or 'UP', watch your serial output on your circuitPy board. You should notice it's consistency improving over time and random high/low values not outputting as consistently. Once they're far more consistently returning "0" than at initial calibration, you're done. 
6. Repeat the steps for the 2nd analog joystick channel. 
7. Press and hold 'CANCEL' to save your settings. 
8. Repeat the above steps for all spring loaded axis (Ch1 Right L/R,Ch2 R Up/Down,Ch4 Left Left/Right) 

### Calibrating the Joystick Endpoints
Again, not all Joysticks are made the same. Some do not have as great of a range of motion as others do. You may have noticed that your motors may move faster in 1 direction than in a different direction. This is because your joysticks "range" is likely not exactly -1 & 1 respectively. This could be due to manufacturing defects in either the joystick instillation, the electronic components themselves, or the plastic housing. Whatever the reasoning,  we can calibrate this as well.  

1. Use the same modified rc_full_example.py code from above to read the current outputs of the x/y axis on channel 1/2 on the right joystick. 
2. Push the joystick all the way left and look at the serial printout statements. Your goal is to have the highest, *most consistent* number displaying as possible. This is so that we have a reliable range output on our joystick axis'. For example, on my controller, 
```
# most reliable, consistent readings
X min: -0.729231
X max: 0.773846 
Y min: -0.729231
Y max: 0.773846 
```
Likely, your controller is jumping between inconistent values at the endpoints of the controller, or even registering a value higher than mine. That's okay, we don't really care what the end number is, what we care about is the conistency/reliability of endpoint value readings. To calibrate: 
1. press and hold 'OK' to enter the menu
2. press 'DOWN' to select the 'Functions Setup'. press 'OK'
3. press 'DOWN' to select 'Endpoints' press 'OK'
4. press 'OK' to select the correct channel. The left collumn (red) corresponds to the minimum joystick value, the right collumn (blue) corresponds to the maximum joystick value. 

![Screen Shot 2022-10-18 at 21 50 44](https://user-images.githubusercontent.com/101632496/196532621-67523a8e-3a7f-4047-b365-8c915c1436e4.png)

5. Starting with Channel 1, hold your joystick all the way to the left. Look at what number you are displaying, and see if you are getting false highs outputting. 
6. As you're holding the joystick, If you're displaying inconsistent highs values, lower your channel endpoint slightly with the "Down" key on the transmitter. 
7. As you change the endpoint values, watch your serial output on the M4. You should notice the output's consistency improving over time. Our goal is consistent readings, similar to when we calibrated the deadpoint "0" as above. The odd high spike is OK. 
8. Once the low endpoint is calibrated, move the joystick to the right all the way to the right. Watch the serial output. 
9. To change the top endpoint, you need to also use the joystick to select the correct collumn (convenient!). You'll need to  select the correct collumn, change the value slightly with Up/Down keys, then hold your joystick all the way right again & watch the serial output, repeat. 
9. Press OK to select ch2. Repeat steps 6-9 for Ch2. 
10. Press and hold 'CANCEL' to save your settings. 

My controllers final endpoint values were:
```
Ch1 99% 99%
Ch2 99% 98%
```
And its most reliable, consistent readings:
```
X min: -0.729231
X max: 0.773846 
Y min: -0.729231
Y max: 0.773846 
```

### Calibrating the Motor Max/Min Values:
Now that we've calibrated your joystick, you'll likely notice that we just reduced the output to our motors, so we can only ever drive them at 75%-ish power now. We can fix that in our code. 

The rc.py function takes 4 arguments:
```
rc.read_analog(pin, lower_bound = -1.0, upper_bound = 1.0, dead_point = 0.0)
    
    :pin: the current channel pin we wish to read.
    :lower_range_bound: integer: the lower range output. Defaults to an arbitrary -1.0
    :upper_range_bound: integer: the upper range output. Defaults to an arbitrary 1.0
    :deadpoint: integer: accepts whatever "stop" or "90*" would be on a servo. Defaults to 0.0
    :return: the current value read from the channel, mapped to the user-inputed range
```

We need to change these lower and upper bounds to compensate for our reduced output range from our joystick. What we're going to do is pull our function's endpoints up to compensate for the fact that we now have reduced range outputs. What used to be a "min/max" range of -1/1, will now be more like -1.3/1.3. This will compensate for the fact that we're actually only outputting -.77/-.72, but we can tell our motors that -.77 is actually -100% power.  Let's modify our read_analog function calls on lines 101-102 to compensate:

```
# my controllers final modified lower/upper ranges
y_joy = rc.read_analog(ch2, -1.361, 1.302)
x_joy = rc.read_analog(ch1, -1.361, 1.302)
```

1. Using my modified ranges as a starting point, modify your rc_full_example file to match the above calibration. 
2. Move the joystick to its max values on the X/Y axis. Watch your x_cur and y_cur print outputs. You want to get them as close to -1 and 1 as possible. For example, mine outputed:
```
# max
x 1.00087 y 1.00087
# min
x -1.00033 y -1.00033
```
3. Modify your lower/upper bounds via trial * error (or maths if you're feeling fancy) until you're reading to a 3 decimal point accuracy (1.000*)

Save these values for later, you're going to need them in future calibrations and programs. 




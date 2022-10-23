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

# Calibration of Joysticks
Joysticks are unfortunately not all made the same. Additionally, overtime joystick springs will relax and change their calibrated centre points. Likely, you'll need to calibrate the joysticks overtime to gain more accurate readings. Upon initial setup, you'll also need to calibrate the joysticks, and fiddle with the below settings. 

*Note: If your robot will not use the left-joystick, there is no need to follow these steps for channels 3/4. 

## Centering the RC Deadpoint (Ch1, Ch2, Ch4)
1. Open the rc_analog_channel_read and read Ch1 joystick, (Right, L/R)
2. Centre the joystick and look at the serial printout statements. Your goal is to have only 0 displaying, such as:
```
0
0
0
0
```
If you're jumping between -32,0, or 17,0, , you need to:
1. press and hold 'OK' to enter the menu
2. press 'DOWN' to select the 'Functions Setup'. press 'OK'
3. press 'DOWN' to select 'Subtrim' press 'OK'
4. press 'OK' to select the correct channel. If your serial output is bouncing between a negative value and 0, hold 'DOWN' to move the centre subtrim to the left. Vice versa if your serial value is presenting positive.
5. As you press 'DOWN' or 'UP', watch your serial output. You should notice it's consistency improving over time. 
6. Press and hold 'CANCEL' to save your settings. 
7. Repeat the above steps for all spring loaded axis (Ch1 Right L/R,Ch2 R Up/Down,Ch4 Left Left/Right) 

## Widening the Top/Bottom Boundaries
Again, not all Joysticks are made the same. Some do not have as great of a range of motion as others do. Thankfully, we can calibrate this as well.  
1. Open the rc_analog_channel_read and read Ch1 joystick, (Right, L/R)
2. Push the joystick all the way left and look at the serial printout statements. Then, all the way to the right Your goal is to have only -100 & 100 (min/max) respectively displaying, such as:
```
-100
-100
-100
-100
```
If you're jumping between numbers that are not absolute 100, you need to:
1. press and hold 'OK' to enter the menu
2. press 'DOWN' to select the 'Functions Setup'. press 'OK'
3. press 'DOWN' to select 'Endpoints' press 'OK'
4. press 'OK' to select the correct channel. The left collumn (red) corresponds to the minimum joystick value, the right collumn (blue) corresponds to the maximum joystick value. 

![Screen Shot 2022-10-18 at 21 50 44](https://user-images.githubusercontent.com/101632496/196532621-67523a8e-3a7f-4047-b365-8c915c1436e4.png)

5. Increase the lower-endpoint, 1% at a time pressing 'UP'. As we're changing, watch your serial output. You should notice it's consistency improving over time. Your goal is a pure number display of the minimum value. Don't be surprised if you need to increase the endpoints to their maximum value of 120%. 
6. To change the top endpoint, press 'OK' until you have Ch1 selected. Then, push the Right Joystick all the way to the right, this will select the 2nd collumn. Repeat Steps 4/5 until your top joystick value is the same pure 100 number.
6. Press and hold 'CANCEL' to save your settings. 
7. Repeat the above steps for Ch2,3,4.

# CircuitPython - FlySky FS-I6X Controller - FS-iA6B Reciever

This tutorial will serve as a reference for setting up the FlySky FS-i6X transmitter and FS-iA6B reciever with a metro M4 device. Theoretically, this should work for just about any RC controller that is capable of outputting a PWM signal.

# RC Intended output
CH1 - Right joystick, Left/Right Control
CH2 - Right joystick, Up/Down Control
Ch3 - Left joystick, Left/Right Control
CH4 - Left joystick, Up/Down Control
CH5 - SWB, 2 way toggle switch
CH6 - SWC, 3 way toggle switch

Eventually, we will drive the robot throttle with CH2, and steer with CH1. CH3/4 will likely not be used, and CH 5/6 will be used for various mechanisms attached to our robot. 


![Screen Shot 2022-10-18 at 20 25 43](https://user-images.githubusercontent.com/101632496/196513614-dd92db1c-323c-43ee-bb24-fdf60ac65196.png)

## Main Tutorial Credits & Documentation
Much of this tutorial is taken from several different sources. I include them here for future reference, as CircuitPython documentation is sparse online. 
- [Main Instruction manual for the FS-i6X controller](https://files.banggood.com/2016/09/FS-i6X%20User%20manual.pdf)
- [An amazing tutorial on setting up the controller by Run Amok Combat Robotics](http://runamok.tech/RunAmok/flysky_i6.html#modes). I have modified a decent portion of this tutorial to only provide relevant material here. 
- [this random thread from 2021 on a raspberryPi forum](https://forums.raspberrypi.com/viewtopic.php?t=308269) that provided the necessary PseudoCode for translating PWM into a useable signal. (April 01,2021 8:03am post)

# Setting initial settings on the Transmitter
First, Put x4 AA into the transmitter

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

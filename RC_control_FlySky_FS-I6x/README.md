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
We need to change some default settings. Default AUX switches are VRA & VRB, x2 analog dials. We instead want to switch these over to SWC (3 way toggle switch) and SWB, a 2 way toggle switch. 
1. power on the transmitter
2. 

# The RoboClaw MotorControler:

# Wiring Instructions
Originally taken from [this tutorial from basicmicro](https://resources.basicmicro.com/roboclaw-motor-controllers-getting-started-guide/), and modified to suit CircuitPython uses. While the photos may use a slightly different motor controler than ours, hookup is the same. 
![image](https://user-images.githubusercontent.com/101632496/193512714-6ac7c174-88ff-486f-b924-520d89c0c88e.png)

1. Wire two DC motors to the RoboClaw. On dual channel RoboClaws like ours, the first motor is wired to M1A and M1B and the second motor to M2A and M2B. For class consistency, A is + and B is GND (though it doesn't really matter)

![image](https://user-images.githubusercontent.com/101632496/193512894-0248a016-98b8-4cf2-97a5-ef0109d769d5.png)

# Connect Power Supply - DC Battery Wiring Instructions
>
> Wiring up, Positive First, then Negative. Disconnecting, Negative First, then Positive
>

Why? If we wire up a battery with a negative connected, we may cause a "short". A short happens when there is low resistane between two wires from a power source. This low resistance can generate excess voltage and cause excessive flow of current in the power source. The electricity flows through the ‘short’ route and causes a short circuit. [This is bad](https://youtu.be/osfgkFyq7lA?t=253). Although, our 12V batteries include a fuse (a thin wire that will burn up/"snap" if overvolted/over current), just incase things get spicy. 

1. Connect both red blue crimp connector wires to the master On/Off switch. One lead terminates on a bare red wire, the other lead terminates on a bare negative wire. 

![IMG_4050 Small](https://user-images.githubusercontent.com/101632496/193517406-9815f32e-1a4b-481d-ac7a-a40f4c704ebd.png)


2. The power terminals are labelled (+) for positive and (-) for negative. Be careful to not connect the power source backwards as this will damage the RoboClaw. DO NOT PLUG IN THE TAMIYA CONNECTOR TO THE DC BATTERY PACK PRIOR TO THIS STEP. Otherwise you will have LIVE bare wires, a dangerous situation for short risk. 

![IMG_4051](https://user-images.githubusercontent.com/101632496/193517620-236c989d-37a6-4b96-93bf-456cade8c445.png)


3. Esure the switch is presently off. Connect the 2 tamiya connectors together. Feel free to flip the switch now, you should notice the green LEDs are now lit on the RoboClaw. 

![IMG_4052 Small](https://user-images.githubusercontent.com/101632496/193517636-65f17911-e516-4696-b349-0f86a7263680.png)

# Wiring the M4 to our Controller
We'll be sending commands to our motors using low_level servo control over digital pins. We can use any Digital pin. We also need to provide power to these pins from the M4, not from the roboclaw itself. Wire up your board as per below (though the D.PINS 2/3 are not hard/fast rules)

While not labelled on the schematic, we are going from M4 D.Pins to S1 and S2 on the RoboClaw. S1 controls MA, and S2 controls MB respectively. 

![m4_RC_wiring_diagram](https://user-images.githubusercontent.com/101632496/193522995-c9ddba14-4c4f-4a5d-bbbb-cdcfa753be12.png)


### Advanced Wiring: Encoders
We'll be using encoders later in the course, but for basic wiring we won't need wire up the encoders. On dual channel RoboClaws the encoder for motor channel 1 is wired to the EN1 header and the encoder for motor channel 2 is wired to the EN2 header. 
Power for the encoder is available at the 5V pins on both the dual channel and single channel RoboClaws. Be sure to also connect the encoder’s ground pin to ground on the RoboClaw. You may not use the 5V rail from the M4 board. 

![image](https://user-images.githubusercontent.com/101632496/193513369-7f2999ed-5bb1-4a8c-93e7-efc5f132f872.png)

Locate the EN1, EN2 and encoder power headers on the RoboClaw. The photo below shows where these are located. Each encoder has two power wires and two wires of output for a total of 4 wires that need to be connected to the RoboClaw. Wire the encoder according to the table below. The encoder of each motor will need to be wired to the correct encoder header. Motor channel M1 uses ENC1 and motor channel M2 uses ENC.

Motor Wire	Function	RoboClaw board
Red	Motor power	M1A/M2A terminal
Black	Motor power	M1B/M2B terminal
Green	Encoder Ground	(-) pin on encoder power header
Blue	Encoder Vcc	(+) pin on encoder power header
Yellow	Encoder A output	ENC1/ENC2 header inside pin
White	Encoder B output	ENC1/ENC2 header outside pin

![image](https://user-images.githubusercontent.com/101632496/193513594-da6bd836-192b-4692-9c31-6042425dd3f9.png)

![image](https://user-images.githubusercontent.com/101632496/193513633-df8e0647-4995-4fdc-ac27-d5cd10877f5c.png)
Reading encoders on an arduino tutorial can be found [here](https://resources.basicmicro.com/simple-arduino-control-of-the-roboclaw/) and [here](https://resources.basicmicro.com/pololu-encoder-wiring/), though I still need to modify this for CircuitPython. 

After wiring, these need to be tuned, [instructions here](https://resources.basicmicro.com/roboclaw-motor-controllers-getting-started-guide/)

# DEBUG METHODS
Note: The roboclaw will randomly erase its onboard memory if it has not been powered on in several weeks. When it does, it defaults to "mixing" mode, which will cause the "rc_control.py" code to IGNORE M2. Follow the steps below to re-program, this MUST be done on the basicmicro windows app, it cannot be re-programmed via onboard buttons for whatever reason. 

1. Be sure RoboClaw has at least 9V battery source. We're going to be using large 12V battery packs for driving our DC motors, so we should be OK. 6V battery sources will not chooch 'er enough, you'll get a constant "logic battery low" error. (so don't use the small 6V barrel jack 4x AA battery holders) 
2. Be sure the RC is in the correct mode, via the onboard buttons. Follow the steps below to verify that your motorcontroller is in the correct mode. 
    - Tank style bots, Mode 1 Opt 4 (*This is what we'll use for our first robot*)
    - Differential style bots, Mode 2, Opt 4
3. Be sure turn on the 12V battery FIRST, then the M4 battery.


#### How to Set *Mode* on the Motor Controller
1. Be sure you have provided power to the motor controller. 
- Press and release the MODE button to enter mode setup. The STAT2 LED will begin to
blink out the current mode. Each blink is a half second with a long pause at the end of the
count. Five blinks with a long pause equals mode 5 and so on.
- Press SET to increment to the next mode. Press MODE to decrement to the previous
mode.
- Press and release the LIPO button to save this mode to memory.
### Set Mode *Option* 
- After the desired mode is set and saved press and release the SET button for options
setup. The STAT2 LED will begin to blink out the current option setting.
- Press SET to increment to the next mode. Press MODE to decrement to the previous
mode.
- Press and release the LIPO button to save this mode to memory. 

If you've done this correctly, when you send a PWM signal similar to how you've programmed low-level servo control, STAT1 starts to blink/flash rapidly, indicating it is recieving RC signals.

## Advanced Fix Steps:
1. Provide at least 9V Power to RC (RoboClaw)
2. Connect RC to motion studio in windows PC, connect device. 
    - Note, you need the RC firmware drivers AND basic micro motion studio installed. 
3. Update firmware if needed. 
4. Basic micro settings:
    - RC mode
    - TTL Flip: YES
    - Mixing: NO
    - Exponetial: YES
    - MCU: YES
5. Verify motors function via PWM sliders. 

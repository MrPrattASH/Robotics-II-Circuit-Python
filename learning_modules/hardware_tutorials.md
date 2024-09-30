# Breadboarding & Hardware Tutorials 
Follow through these self-guided tutorials to learn fundamental skills for breadboarding, and interfacing with physical components via CircuitPython. If you are unable to complete a tutorial, or are not sure what to do, seek help from your teacher or a peer! 

Start with the Basics, then move on from there. You'll notice that Level 1 tutorials correspond to Level 0 tutorials, but increase in complexity. 

***

# Breadboarding Tutorials

### The Basics
* Base 0.0: [What Is A Breadboard?](https://learn.adafruit.com/breadboards-for-beginners/introduction)
    * Read up to & *including* "Jumper Wires" 
* Base 0.1: [Simple Circuits](physical_component_tutorials/breadboard_basics/breadboard_basics.md)

### Level 0:
* 0.0: [Simple External LED Circuit](physical_component_tutorials/basic_led_debug/single_led_0.md)
* 1.0: [4-Pin Buttons](https://sites.google.com/view/circuitpython/tutorials/button-and-led)
* 2.0: [Capacitors & Noisy Signals](physical_component_tutorials/capacitors_breadboard/Capacitors.md)

### Level 1:
* 0.1: [x4 External LED Circuit](physical_component_tutorials/basic_led_debug/single_led_1.md)
* 1.1: [Buttons & LEDs](physical_component_tutorials/4-Pin_Buttons/button_4_1.md)

***

# Motor Tutorials

## Servo Motors
### Power Requirements
* For Projects that use 2 or less servos, we can provide simple Breadboard Power from out Metro M0 board. The current output is only 1.5A, but this is sufficient for the (typically) low power requirements that using 2 servos requires. 
* If you're using more than 3 servos, or your board keeps "browning out" (shutting off or restarting in "safe mode" (Serial output)) due to power requirements, you'll need to wire in an UBEC to provide external power. 
    * Universal Battery Elimination Circuit Wiring (UBEC)

### Servo Tutorials
* [(Continuous) Rotational Servos](physical_component_tutorials/servo_motors/ContinuousRotationalServos.md)
    * [*Mars Rovers* Challenges](physical_component_tutorials/servo_motors/RotationalChallenges.md)
    * [*Elevation Engineering* Challenges](physical_component_tutorials/servo_motors/RotationalChallenges_Engineering.md)
* [Positional Servos](physical_component_tutorials/servo_motors/PositionalServos.md)

*** 

# Sensor Tutorials
* [Distance Sensor (Ping)](physical_component_tutorials/ping_sensor/README.md)
    * [*Mars Rovers* Distance Sensor Challenges](physical_component_tutorials/ping_sensor/DistanceSensorChallenges.md)
* [FlySky FS-i6x Radio Reciever & Transmitter](../RC_control_FlySky_FS-I6x/learning_modules/Fly_sky_learning.md)
# Tutorials
Follow through these self-guided tutorials to learn fundamental skills for using CircuitPython on the MetroM4 Express. If you are unable to complete a tutorial, or are not sure what to do, seek help from your teacher or a peer! 

Each tutorial has a *Level 0* and corresponding *Level 1* tutorial associated with it. If you complete level 0, move on to level 1. For example:
* Level 0 tutorial *0.0: Python Syntax* has a corresponding second Level 1 tutorial, *0.1: Built in Libraries*

# Circuit Python Programming Tutorials

## The Basics
Before moving on to any level 0/1 tutorials, ensure you have completed this initial tutorial. 
* Base 0.0: [How to Write & Save Code on Circuit Python Boards](programming_tutorials/circuit_python_basics/python_basics.md)

## Level 0:
* 0.0: [Python Syntax](https://sites.google.com/view/circuitpython/tutorials/set-up/hello-python)
* 0.1: [What are "Variables"?](programming_tutorials/variables/variables.md)
* 0.2: [Forever Loops](programming_tutorials/while_true/while_true.md)
* 1.0: [Onboard LED](programming_tutorials/digital_io/digital_io.md)
* 2.0: [Traceback Error Codes](https://learn.adafruit.com/welcome-to-circuitpython/interacting-with-the-serial-console)
* 3.0: [Adding Libraries](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries)
* 4.0: [What are "Functions"?](https://sites.google.com/view/circuitpython/tutorials/blinking-led/libraries-and-functions)
* 5.0: [Conditional Statements](https://sites.google.com/view/circuitpython/tutorials/button-and-led/conditionals-i)

## Level 1:
* 0.3: [Built in Libraries](https://sites.google.com/view/circuitpython/tutorials/blinking-led/libraries-and-functions)
* 1.1: [Morse](programming_tutorials/SOS_Blinking20_LED/morse.md)
* 2.1: [The REPL](https://learn.adafruit.com/welcome-to-circuitpython/the-repl)
* 4.0: [Built in Functions](programming_tutorials/Built_In_Functions_Practices/built_in_functions.md)

# Breadboarding & Hardware Tutorials 

## The Basics
Before moving on to any level 0/1 tutorials, learn about the basics of a *Breadboard* (and why they're called breadboards) and electrical flow
* Base 0.0: [What Is A Breadboard?](https://learn.adafruit.com/breadboards-for-beginners/introduction)
    * Read up to & *including* "Jumper Wires" 
* Base 0.1: [Simple Circuits](physical_component_tutorials/breadboard_basics/breadboard_basics.md)


## Level 0:
* 0.0: [Simple External LED Circuit](physical_component_tutorials/basic_led_debug/single_led_0.md)
* 1.0: [4-Pin Buttons](https://sites.google.com/view/circuitpython/tutorials/button-and-led)

## Level 1:
* 0.1: [x4 External LED Circuit](physical_component_tutorials/basic_led_debug/single_led_1.md)
* 1.1: [Buttons & LEDs](physical_component_tutorials/4-Pin_Buttons/button_4_1.md)

# Motors

## 2 or Less Motors Required
For Projects that use 2 or less servos, we can provide simple Breadboard Power from out Metro M0 board. The current output is only 1.5A, but this is sufficient for the (typically) low power requirements that using 2 servos requires. 
* [(Continuous) Rotational Servos](physical_component_tutorials/servo_motors/ContinuousRotationalServos.md)
* [Positional Servos](physical_component_tutorials/servo_motors/PositionalServos.md)

## 3 or more Motors Required
If you're using more than 3 servos, or your board keeps "browning out" (shutting off or restarting in "safe mode" (Serial output)) due to power requirements, you'll need to wire in an UBEC to provide external power. 
* Universal Battery Elimination Circuit Wiring (UBEC)

# Sensors
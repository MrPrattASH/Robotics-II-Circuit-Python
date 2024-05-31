# Wiring LED's leveled up

Using [the tutorial from level 0](learning_modules/physical_component_tutorials/basic_led_debug/single_led_0.md), continue on by wiring up more LEDs. This quickly becomes significantly more complex when you need to factor in two pieces of hardware now instead of just 1. 

## Stage 0:
* Wire up 1 more LED to a different Digital pin and blink this in time with the first LED. 
    * Initilize this pin the same way you did on lines 17 & 19 in this code.  
    * Change the variable name to led2, and the board.D13 to board.D0-12 (pick one, it doesn't matter)
    * turn both LEDs on, then time.sleep(0.5), then both off, then time.sleep(0.5). 

## Stage 1: 
* Wire up two additional external LEDs to new D.pins. You should now have a total of x4 external LEDs connected.
* Can you make an interesting pattern display across your 4 LEDs by causing them to blink out of sync and in sync? 


##### Quick Links
* [Home](README.md)
* [Tutorials](learning_modules/tutorials_list.md)
* [Circuit Python Cheat Sheet](learning_modules/circuit_python_cheatsheet.md)
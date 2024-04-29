# Wiring an LED

Use the following Diagram below to wire an LED to your breadboard. 

You will need: 
* x2 Male > Male Jumper Wires
* x1 220ohm Resistor
* x1 3mm LED
  
<img width="400" alt="Screenshot 2023-12-12 at 14 21 00" src="https://github.com/MrPrattASH/Robotics-II-Circuit-Python/assets/101632496/00036102-5310-45fb-95d9-a564b58325b1">

## Things to know:

* The "D" for Digital pin, does not matter. You can use any D pin you choose, as long as your code aligns. 
* All LED’s, unless otherwise specified, need a resistor or you’ll overpower the LED, causing it to be REALLY bright once, then dead. 
* What is a resistor? 
    * That little orange piece. We'll need to use these for ALL LEDs in this course. Resistors "resist" the flow of current in a circuit. It's simply a little rod of ceramic or carbon that holds back some current (flow of electricity), and exhausts the "wasted" current as heat. 
    * Why do we need a resistor with LEDs? If we didn't, electricity would be flowing so quickly through our LED, that it would get hot quickly, and burn out the LED from too much current. Think drinking through a firehose vs drinking through a watering fountain; which water circuit is resisted?
    * What size resistor do I need? Resistors come in all different sizes and reduce more “Ohms” (the measurement of current). For our purposes, anything between 220-1000 ohm will be sufficient. 
* LEDs have 2 leads. A long lead and a short lead. They also have a flat indent on their plastic head rim. * current only flows through an LED one way and you don't want to wire this up backwards.
    * The long lead is positive
    * The short lead is neutral

<img width="307" alt="Screenshot 2023-12-12 at 14 20 31" src="https://github.com/MrPrattASH/Robotics-II-Circuit-Python/assets/101632496/fa479601-906b-4586-9a72-bdf9ecbf2272">


## Code:
Use the code above this README.md called "basic_led_debug.py". If you click that link, you can copy the code to your M4 board. 

![Screenshot 2023-12-12 at 14 21 25](https://github.com/MrPrattASH/Robotics-II-Circuit-Python/assets/101632496/2f71c790-ae46-434a-9891-fca0e7a25883)



You can click this button to copy all code once a .py file is open. 

![Screenshot 2023-12-12 at 14 19 22](https://github.com/MrPrattASH/Robotics-II-Circuit-Python/assets/101632496/a96d7b88-331a-4780-9de5-3fb510c90558)




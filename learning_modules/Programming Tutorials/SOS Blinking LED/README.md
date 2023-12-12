# S.O.S. Blinking LED

Now that you can make an LED blink simply, try this challenge. (modified from this [tutorial](https://sites.google.com/view/circuitpython/tutorials/blinking-led/sos_))


## Morse Code
Morse code is a system for sending messages as a sequence of ON and OFF signals with predefined spaces in between. 

A key for international Morse code
Attribution: Rhey T. Snodgrass & Victor F. Camp, 1922, Public domain, via Wikimedia Commons

Characters in Morse code are represented by a series of dots and dashes, which we will use to determine the length of time our LED turns on for. 

* 1 dot = turning the LED on for 1 unit of time, then off again
* 1 dash = turning the LED on for 3 units of time, then off again
* Between letters, we wait for 3 units.
* Between words, we wait for 7 units.

## Your Challenge
Fill in the blanks in the code below. We want to blink the message SOS, so we need to make our LED:

1. blink 3 dots (S)
2. wait for 3 units (between letters)
3. blink 3 dashes (O)
4. wait for 3 units (between letters)
5. blink 3 dots (S)
6. wait for 7 units (between words)

## tips:
* Unit time: As long as your units are consistent, the code is the same. For example:

`# unit time of 1s each. This is a LONG processing code
led.value = True # turn on
time.sleep(3) # sleep 3 "units"
led.value = False # turn off`

`# unit time of 0.1s each. This is a MUCH FASTER processing code.
led.value = True # turn on
time.sleep(0.3) # sleep 3 "units"
led.value = False # turn off`

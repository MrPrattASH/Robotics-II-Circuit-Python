# Advanced Button Practice

Let's get more practice initializing pins for different components on our board. Its best to get the practice of initializing hardware under your belt, as it's something we'll be doing A LOT. To do get more practice, lets make a more complex circuit. 

## Challenge 1
* Wire up x2 buttons and x2 LEDs. Make each button toggle each LED individually. For Example: 
    * Button 1 when pressed/held down, lights up LED 1, and vice versa. 
    * Button 2 when pressed/held down, lights up LED 2, and vice versa.
    * Button 1+2 are pressed/held down, both LEDs light up, and vice versa. 
##### Tip:
You can initialize each button the same, however, you need to have different variable names. Perhaps "green_button" and "blue_button"? 

## Challenge 2
* Wire up x1 buttons and x2 LEDs total. 
* This single button toggle 1 LED on, and the other LED off. When pressed/held down, the LEDs swap their current states. 

## Challenge 3
* Wire up x2 buttons and x4 LEDs total.
    * Button 1 actuated outputs pattern #1
    * Button 2 actuated outputs pattern #2
    * NO buttons actuated outputs pattern #3
    * ALL buttons actuated outputs pattern #4

##### Tip:
* you can use the `and` operator to check multiple conditions at once in single if statement. For example:
```
if button_1 and button_2: 
   # both buttons have been pressed 
```
* You also likely need an if, elif, else loop here.
```
    while True:
        if button_1 and not button_2:
            # only button 1 is pressed
        elif button_2 and not button_1:
            # only button 2 is pressed
        ...
```

##### Quick Links
* [Home](README.md)
* [Tutorials](learning_modules/tutorials_list.md)
* [Circuit Python Cheat Sheet](learning_modules/circuit_python_cheatsheet.md)
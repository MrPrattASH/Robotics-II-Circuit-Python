# Built In Fuctions

This tutorial will teach you how to use built in functions in CircuitPython.

1. load up the serial monitor on your M4 and press any key to open the REPL
type in the following:

`import math`

`dir(math)`

Do you see any math operators you have used before?

type in the following:

`import random`

`random.randint(0,100)`

`random.randint(50,100)`

`random.randint(0,50)`

What was the output for each random call?
Was the return an integer or a decimal? (float)

randint(min,max) is Exclusive, meaning it will return -1 from your max number (rounding down)

type in the following:

`random.random()`

`random.random()`

`random.random()`

what was the output for each random call?
random.random() will return a random float (decimal number) between 0, and 1.0. This is handy for sensors later in the course.

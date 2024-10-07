# For Loops with Ranges in Python

In this tutorial, we'll learn about:
* What a `for` loop is, and how it differs from a `while True:` loop
* How `for` loops can be used to repeat actions a specific number of times.
Let's try the difference between a single line program and a `for` loop.

### Single Line Program
1. Connect the M4 to your computer, and load *code.py*
2. On line 1, write:

```python
print("this is a non-looped program")
```

3. Open the serial console.
4. Save this program and observe the serial output. You'll notice you should see a `code done running` line in your Serial console. 

---

### For Loop
1. Delete all existing code.
2. Write in this code:

```python
for i in range(5):
    print("this is in a loop!")
```

3. Open the serial console.
4. Save this program and observe the serial output.

## Examining a For Loop:
You've likely noticed by now that the statement is printed five times. That's what the `for i in range(5):` statement does. Let's examine this:
* The word "for" initiates a loop. This loop will run a specific number of times as defined.
* The variable `i` is a counter. It will take values from 0 up to 4 in our case (5 values in total because `range(5)` gives us numbers 0, 1, 2, 3, 4).
* The `range(5)` function provides a sequence of numbers from 0 to 4.
* The colon `:` signifies to the computer that the statement is over and the loop body begins. Similar to how we write `if x is True` statements.
* Much like the indentation in the bullet points here, anything that is indented within the `for` loop will run for each value in the range.

Try running the following code to see the counter `i` value throughout loop interations:

```python
for i in range(3):
    print("Loop iteration number:", i)
```

---

## Using Delays in For Loops:
We can also use time delays in `for` loops just like in `while` loops to see the iteration more clearly. *This is generally advised for debugging purposes, but not super helpful for when we're actually running code, unless the `time.sleep()` value in minimal*. 

1. Import the `time` module and use `time.sleep()` for delays.
2. Write and run the following code:

```python
import time
for i in range(5):
    print("This is in a loop! We're on interation number:", i)
    time.sleep(1)
print("The loop has finished")
```

## For Loops and While True Loops
A `for` loop lets us run a block of code a specific number of times. Unlike a `while True:` loop, which runs forever, a `for` loop ends after a predetermined number of iterations. This can be useful when you need to repeat actions a set number of times rather than indefinitely. We can even nest in `for` loops inside of our `while True:` loop. 

1. Delete all existing code. 
2. Write and run the following code:

```python
import time

print("starting main loop")
while True:
    for i in range(5):
        print("This is in a loop! We're on interation number:", i)
        time.sleep(1)
    print("The loop has finished. Notice how 'i' will now reset back to '0'")
    time.sleep(1)
```

3. Observe the serial output. 

--- 

## For Loops: 2 Arguments (Start & Stop)
a `for` loop can also take more than a single arguement. Up to this point, we've been playing with a single arguement:

```python
for i in range(10):
    print(i)
    time.sleep(0.5)
```

* in this example, we increase our `i` iterater variable by 1 every time.
* we also always start at `0` for our loop. 

Let's try something different: 
```python
for i in range(0, 10):
    print(i)
    time.sleep(0.5)
```

* did you notice a difference in the output? What has changed in our arguments? 

---

We have 2 arguments now, rather than always starting from `0`, we can say what number to start from, and what number to end at. Observe:

```python
for i in range(5, 10):
    print(i)
    time.sleep(0.5)
```

* what number did we start at this time? 

---

## For Loops: 3 Arguments (Start, Stop, Iterater)
Lets try 3 arguments:

```python
for i in range(0, 10, 2):
    print(i)
    time.sleep(0.5)
```

* What was the print output this time?
* the third argument, `2`, is our step iterator. Rather than stepping by 1 each iteration or loop, now we are stepping by 2! 

Lets look at a few more examples:

Example 1: Count by 5's
```python
for i in range(0, 50, 5):
    print(i)
    time.sleep(0.5)
```

Example 2: Reverse counting down
```python
for i in range(10, 0, -1):
    print(i)
    time.sleep(0.5)
```
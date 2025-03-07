# For Loops with Ranges in Python

In Python programming, the `for i in range` loop is a fundamental construct that allows you to iterate over a sequence of numbers, executing a block of code multiple times efficiently. This is similar to the `while True` loops we have previously explored, but with more control over the number of repetitions and better readability.

## Understanding `for i in range` Loops

In Python, `for i in range` is commonly used with the `range()` function, which generates a sequence of numbers. Here's a basic structure, copy and paste this into your code.py file and observe the output in your serial console:

```python
# Using a 'for' loop with 'range' to repeat an action
for i in range(5):
    print("This is iteration number:", i)
```

- **Loop Definition:** `for i in range(5):` This line defines a loop that will iterate five times. The loop variable `i` starts at 0 and goes up to 4 (one less than the number provided).
- **Repeating Actions:** `print("This is iteration number:", i)` The loop repeats this action, updating the loop variable `i` each time.

### Parameters of `range()`

The `range()` function can take different parameters to tailor the sequence of numbers:

1. **Single Parameter:** `range(stop)` generates numbers from 0 up to (but not including) `stop`.
2. **Two Parameters:** `range(start, stop)` generates numbers from `start` to `stop` (excluding `stop`).
3. **Three Parameters:** `range(start, stop, step)` generates numbers from `start` to `stop`, incrementing by `step`. If `step` is negative, the numbers will decrement.

Here's how these parameters can be used:

```python
# Numbers from 0 to 4
for i in range(5):
    print(i)

# Numbers from 2 to 5
for i in range(2, 6):
    print(i)

# Numbers from 10 to 1, decreasing by 2
for i in range(10, 0, -2):
    print(i)
```

## Practice 1

1. Experiment with `range()` by running this code:

```python
for i in range(1, 10, 2): 
    print("Odd number:", i)
```

How does changing the parameters modify the output sequence?

## Applying `for` Loops in Robotics

In robotics, loops are essential for repeated actions like moving a robot forward or reading sensor data multiple times. 

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

### Example: Moving a Robot Forward

Assume you have a function `move_forward(steps)` that moves the robot forward by a given number of steps. You can use `for` loops to move the robot a specific way:

```python
# Move the robot forward 5 steps, 3 times
for i in range(3):
    move_forward(5)
```

## Challenge 1: Looping for Tasks

Use a `for` loop to simulate a robot lifting objects repeatedly. Each lift takes one unit of energy, and you want the robot to lift 4 objects.

```python
# Define a function 'lift_object()' that prints "Object lifted". This will be a placeholder statement
def
# Use a 'for' loop to call 'lift_object()' 4 times
```

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# Create the function with 'def lift_object():' and inside, use 'print("Object lifted")'.
# Use 'for i in range(4):' to call the function multiple times.
</code></pre>
</details>

## Challenge 2: Countdown for Launch

Create a countdown from 10 to 1 before a robot launch using a loop.

```python
# Use a 'for' loop to count down from 10 to 1
for
    # Print each number in the countdown
# Print "Launch!" after the loop
```

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# Use 'for i in range(10, 0, -1)' for counting down from 10 to 1.
# Ensure you print "Launch!" outside of the loop.
</code></pre>
</details>

## Challenge 3: Adjusting Parameter Values

Your task is to create a loop that modifies the speed of the robot incrementally from 1 to 5 units.

```python
# Assume a function 'set_speed(speed)' sets the robot's speed
def set_speed(speed):
    print("speed", speed, "set!")

# Use a 'for' loop to increase speed from 1 to 5
for
    # Call 'set_speed(speed)' inside the loop
```

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# Iterate with 'for speed in range(1, 6):' to change the speed from 1 to 5 inclusive.
# Call 'set_speed(speed)' within each iteration of the loop.
</code></pre>
</details>

As you practice more, you'll appreciate the power and flexibility these loops provide!
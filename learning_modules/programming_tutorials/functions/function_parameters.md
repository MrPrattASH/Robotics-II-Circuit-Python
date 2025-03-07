# Function Tutorial

In Python programming, we've learned that a function is a reusable block of code designed to perform a specific task. Functions allow us to organize our code, make it more readable, and use the same logic multiple times without having to repeat ourselves. 

Something new is that functions can take inputs called **parameters** to perform operations on them.

Earlier, we've seen functions like `time.sleep(1)`, where `1` is an **argument** passed to the function `time.sleep()`, helping it understand how long to pause. Now let's learn more about parameters and arguments in our own functions!

## Understanding Functions with Parameters

A parameter is a named variable passed into a function which serves as a placeholder for the argument during function execution. Parameters and Arguments sound like a lot, so let's break it down further. 

Here’s how you define and use a simple function with a parameter:

```python
# We're defining a function named 'greet'
# 'name' is a parameter that the function uses
def greet(name):
    print("Hello, " + name + "!")
```

- **Define the Parameter:** `def greet(name):` This line defines a function called `greet`, which takes one parameter: `name`.
- **Using the Parameter:** `print("Hello, " + name + "!")` The function uses the parameter `name` to display a personalized greeting.

When you call this function and pass a value to it, that value is known as an **argument**. The argument fills in or replaces the parameter when the function executes.

```python
greet("Rover")  # "Rover" is an argument
greet("World")  # "World" is another argument
```

***

## Practice 1

1. Copy the `greet` function into your code editor.
2. Call the function with different names to see various outputs.

```python
greet("Alice")
greet("Bob")
```

3. Notice how the function uses the `name` parameter to create a unique greeting each time you provide a different argument.

***

## Functions with Multiple Parameters

Functions can also take more than one parameter, which allows them to perform more complex tasks. Here’s how it works:

```python
# This function calculates the area of a rectangle
# 'length' and 'width' are parameters
def calculate_area(length, width):
    area = length * width
    print("The area is:", area)
```

- **Multiple Parameters:** The function `calculate_area` takes two parameters: `length` and `width`.
- **Calculating Area:** Inside the function, it calculates the area by multiplying `length` and `width`.

You can call this function and pass different arguments to calculate areas of various rectangles:

```python
calculate_area(5, 3)
calculate_area(10, 4)
```

## Function Practice 2

1. Copy the `calculate_area` function into your code.
2. Call the function with different values for `length` and `width`.

```python
calculate_area(7, 2)
calculate_area(6, 9)
```

3. Observe how changing the arguments affects the calculated area.

***

## Challenge #1: Function with Parameters

Now it’s your turn to create a function that calculates the perimeter of a rectangle!

```python
# Define a function 'calculate_perimeter' with parameters 'length' and 'width'
def 
    # Assign a variable 'perimeter' to the sum of all sides (2 * length + 2 * width)
    
    # Print the perimeter

# Try calling the function with different lengths and widths

```

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# Use the formula for perimeter: 2 * length + 2 * width in the function body.
</code></pre>
</details>

<details>
<summary>Click to reveal an example output</summary>
<pre><code>
The perimeter is: 16
The perimeter is: 28
</code></pre>
</details>

## Challenge 2: Greet Multiple People

Create a function that takes two parameters: `greeting` and `name`, and prints a custom greeting message. 

```python
# Define a function 'custom_greet' that takes parameters 'greeting' and 'name'
def 
    # Print the custom greeting message to greet members by name and custom greeting


# Test the function with different greetings and names

```

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# Concatenate the 'greeting' and 'name' parameters with a comma and space in between to form the message.
</code></pre>
</details>

<details>
<summary>Click to reveal an example output</summary>
<pre><code>
Welcome, Alice!
Good morning, Bob!
</code></pre>
</details>

## Challenge 3: Calculate Robot Speed

Create a function called `calculate_speed` to find out the speed required for the robot to travel a certain distance in a given time period.

```python
# Define a function 'calculate_speed' with parameters 'distance' and 'time'
def 
    # Calculate speed (Speed = Distance / Time)

    # Print the speed

# Test the function with different distances and time periods


```

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# Use the formula for speed: Speed = Distance / Time.
# Make sure both 'distance' and 'time' are positive numbers.
</code></pre>
</details>

<details>
<summary>Click to reveal an example output</summary>
<pre><code>
The required speed is: 20.0 units per time period
The required speed is: 50.0 units per time period
</code></pre>
</details>


Functions with parameters and arguments are powerful tools in programming. They let us create flexible and reusable code components that can perform tasks based on the inputs provided. As you write more functions, you'll become adept at crafting reusable and organized code!
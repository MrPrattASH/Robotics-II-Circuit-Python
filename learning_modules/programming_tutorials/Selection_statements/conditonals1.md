# Conditional Statements in CircuitPython

In this tutorial, we'll learn how to use conditional statements (`if`, `elif`, `else`) in CircuitPython to control the flow of our programs. Conditional statements allow us to execute certain pieces of code based on specific conditions.

## Introduction to Variables and Types

Before we dive into conditional statements, let's review variable types. In this course, we'll work with four main types of variables:

- **Integer (int)**: Whole numbers such as `0`, `24`, `432`
- **Float (float)**: Decimal numbers such as `0.3`, `435.4`
- **String (str)**: Text within double quotes `"Hello, world!"` or single quotes `'Distance away is: '`
- **Boolean (bool)**: Either `True` or `False`

```python
age = 15 # Integer
height = 5.7 # Float
greeting = "Hello!" # String
is_student = True # Boolean
```

## Boolean Expressions and Logical Operators (`and`, `or`, `not`)

Boolean expressions evaluate to a Boolean value (`True` or `False`). We use logical operators to create more complex Boolean expressions. The main logical operators are:

- `and`: Returns `True` if both expressions are `True`
- `or`: Returns `True` if at least one expression is `True`
- `not`: Returns the opposite of the expression's Boolean value

### Example: Logical Operators

```python
a = True
b = False

# 'and' operator example
print(a and b) # Output: False

# 'or' operator example
print(a or b) # Output: True

# 'not' operator example
print(not a) # Output: False
```

### Practice: Boolean & Logical Operators

Write a small piece of code in your microcontroller's `code.py` to test various combinations of Boolean and logical operators:

```python
x = True
y = False
z = True

print(x and y)  # False
print(x or y)   # True
print(not z)    # False
print(x and z)  # True
print(y or z)   # True
```

## Conditional Statements

Conditional statements allow us to execute code only if specific conditions are met. Let's explore the different types of conditional statements.

### If Clause

An `if` clause checks the condition and executes the body only if the condition is `True`. The structure looks like this:

```python
if <condition>:
    <body>
```

- `<condition>`: The Boolean expression that is checked.
- `<body>`: The indented code block that runs if the condition is `True`.

### Example: If Clause

```python
is_hot = True
if is_hot: # This condition is True, so the body below will execute
    print("Take off your jacket!")

# We can also write
if is_hot == True: 
    print("Take off your jacket!")   
# However, since is_hot = True, writing True == True is redundant.
```

### Practice

Using your microcontroller, make `my_condition` a Boolean to display the three print statements in your serial console:

```python
# vvv your code here
my_condition = True
# ^^^ your code here
if my_condition: # don't change this
    print("You're doing...")
    print("fantastic!!")
    print(":)")
```

**Expected Serial Output:**

```
You're doing...
fantastic!!
:)
```

### If-Else Clause

An `if-else` clause provides an alternative block of code that runs if the `if` condition is `False`. The structure looks like this:

```python
if <condition>:
    <body-1>
else:
    <body-2>
```

- `<body-2>`: The indented code block that runs if the condition is `False`.

### Example: If-Else Clause

```python
is_hot = False
if is_hot: # This condition is False, so the `else` body will execute
    print("Take off your jacket!")
else:
    print("Leave your jacket on.")
```

### Practice

On your microcontroller, write an `if-else` statement where `visitor_count` is incremented if `is_student` is `False`:

```python
is_student = False
visitor_count = 0
# Don't change the above code
# vvv write your code here


# ^^^ write your code here
# don't change the below code
print(visitor_count)
```

**Expected Output:**

```
Visitor Count: 1
```

## Comparison Operators

Comparison operators are often used in conditional statements. Here are the main ones:

- `==` (equals): Checks if two values are equal.
- `!=` (not equals): Checks if two values are not equal.
- `<` (less than): Checks if the left value is less than the right value.
- `<=` (less than or equals): Checks if the left value is less than or equal to the right value.
- `>` (greater than): Checks if the left value is greater than the right value.
- `>=` (greater than or equals): Checks if the left value is greater than or equal to the right value.

### Example: Comparison Operators

```python
a = 5
b = 10
print(a == 5) # True, because a is 5
print(a != 5) # False, because a is 5
print(a < 10) # True, because 5 is less than 10
print(a <= 5) # True, because 5 is equal to 5
print(a > 1)  # True, because 5 is greater than 1
print(b >= 20) # False, because 10 is not greater than or equal to 20
```

### Practice

In your microcontroller's `code.py`, write and predict the output of these comparison statements:

```python
x = 7
y = 3
print(x == y) 
print(x != y)
print(x < y)  
print(x <= 7) 
print(x > y)  
print(y >= 3) 
```

### Comparison Operators in an If Statement

Let's use comparison operators in an if statement and create a practice exercise.

```python
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

### Practice

On your microcontroller, write a conditional statement using comparison operators to check the value of `num`. We should have 3 outputs:
* If num is greater than 10: print `"Greater than 10"`
* else if num is equal to 10: print `"Equal to 10"`
* otherwise: print `"less than 10"`

```python
num = 5
decision = ""
# Don't change the above code
# vvv write your code here


# ^^^ write your code here
# Don't change the below code
print(decision)
```

**Expected Output:**

```
Less than 10
```

### Elif Clause

An `elif` clause (short for "else if") allows for multiple conditions to be checked in sequence. The structure looks like this:

```python
if <condition-1>:
    <body-1>
elif <condition-2>:
    <body-2>
```

- `elif` stands for "else if".
- Its condition is checked only if none of the previous conditions were `True`.

### Example: Elif Clause

```python
temperature = 30
if temperature > 40:
    print("It's really hot!")
elif temperature > 30:
    print("It's hot!")
else:
    print("It's not hot.")
```

### Example Where Elif Executes

```python
temperature = 35
if temperature > 40:
    print("It's really hot!")
elif temperature > 30:
    print("It's hot!") # This will execute because the condition is True
else:
    print("It's not hot.")
```

### Practice

On your microcontroller, write a conditional statement to check the variable `is_allowed`.
* If is_allowed is true, assign message the value `"Access granted"`
* otherwise, assign message the value `"Access denied"`

```python
is_allowed = False
message = ""
# Don't change the above code
# vvv write your code here


# ^^^ write your code here
# Don't change the below code
print(message)
```

**Expected Output:**

```
Access denied
```

### Combining If, Elif, and Else

You can combine `if`, `elif`, and `else` for more complex decision-making. The structure looks like this:

```python
if <condition-1>:
    <body-1>
elif <condition-2>:
    <body-2>
else:
    <body-3>
```

- Use this structure when there are multiple conditions to check in sequence.

### Example: Combining Clauses

```python
score = 85
if score >= 90:
    print("Grade: A") # This will skip execution because `score >= 90` is false
elif score >= 80:
    print("Grade: B") # This will execute because `score >= 80` is true
else:
    print("Grade: C")
```

# Final Practice Challenges:

## Practice Exercise #1
Using the code below as a template, write a selection statement that:
* an if statement that will print if the variable `is_touched` is True. 

```python
is_touched = True # don't change this

# write your code here vvv



# write your code here ^^^

print("The touch sensor was pressed")
```

## Practice Exercise #2
Using the code below as a template, write a selection statement that:
* an if/else statement that will print "touched"m if `is_touched` is `True`, and "non touched" if `is_touched` is `False`.

```python
is_touched = False # don't change this

# write your code here vvv



# write your code here ^^^

print("Touch sensor test complete")
```

## Practice Exercise #3
Using the code below as a template, write a selection statement that:
* an if/elif/else statement that:
* if volume is < 20, print "turn up the volume"
* if volume is > 20 and < 50, print "just right"
* else, print "turn it down"

```python
volume = 24
# write your code here vvv



# write your code here ^^^

print("volume test complete")
```

## Practice Exercise #4
*modified from [this](https://sites.google.com/view/circuitpython/tutorials/button-and-led/conditionals-i) tutorial* 

* For this exercise, we've defined two variables, `eight_characters` and  `contains_number` to check the strength of a password. 
* Write a conditional statement that assigns a variable called `password_strength` depending on the following criteria:
    * `password_strength = "Strong"` if a password has 8 characters and contains a number
    * `password_strength = "Medium"` if a password has 8 characters or contains a number
    * `password_strength = "Weak"` Otherwise, if a password contains neither 8 characters nor contains a number
* *Note: it is not required to actually **create** a password for this challenge, only to evaluate a hypothetical password based on the criteria*

Using the code below as a template, write a selection statement that will output a "Medium" print password strength string based on the criteria:

```python
eight_characters = True
contains_number = False
password_strength = ""
# Don't change the above code
# vvv write your code here


# ^^^ write your code here
# Don't change the below code
print(password_strength)
```

**Expected Output:**

```
Medium
```
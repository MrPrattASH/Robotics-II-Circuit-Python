# Basic Python Syntax

## What is a Computer Program?
A computer program is a set of instructions that tells a robot how to perform specific tasks or respond to certain conditions. This involves receiving inputs from the environment (*such as data from sensors like cameras, microphones, or touch sensors*) that provide information about the robot's surroundings or instructions from human operators. The robot's computer then processes these inputs and determines appropriate outputs, which are actions or responses executed by the robot. Outputs could involve moving parts of the robot, navigating a space, or communicating information back to humans or other systems. Understanding how programs guide input and output is essential for students interested in robotics, as it defines how robots interact with and respond to the world around them.

There are 2 ways we can write code for our microcontroller. A REPL (Read-Eval-Print Loop) and a Python script saved in a `.py` file. 
- A REPL is an interactive environment where you can type code line by line and see immediate results, making it great for testing code snippets or learning how individual commands work. However, we can't write multiple instructions in our REPL. 
- On the other hand, a script in a `.py` file is used to write a complete set of instructions that can be executed all at once, which is ideal for developing larger programs or projects. 
While a REPL offers quick feedback for experimentation, script files allow for the development and execution of more structured and complex code. We'll be using scripts for the majority of this course. 

## Interactive Tutorials
For these tutorials, you're going to need:
* your m4 microcontroller board
* the serial port open and running

1. Read the section intro, and the task requirements.
2. copy/paste the existing code to your `code.py` file on your `circuitpy` device, then modify the code to satisfy the requirements.
3. save this code to your metro m4's `code.py` file.
4. look at the serial output. Did it match the intended output?
5. check the hint, or solution, depending on what you need. 


---

## A Note on Code Comments...
In programming, we need a way to distinguish what is an instruction for our robot, and what is a note for us as programmers. A code comment is a piece of text in a program that is ignored by the computer when the program runs. It is used to explain what certain parts of the code do, making it easier for others (or yourself) to understand when reading the code later. Comments can clarify complex code, indicate the purpose of variables or functions, and remind programmers of things to fix or check. In Python, a single-line comment is created by placing a `#` symbol before the text. For example, in Python, you might see:

```python
# This variable stores the user's age. The computer ignores this line
user_age = 25 # (the computer reads all non-green text here!)
```

---

## Section 0. Arithmetic operators

In python, just like on your calculator, you can do a lot of math in line. Take a look at some examples:

| Operator     | Description                                               | Example          | Result                       |
|--------------|-----------------------------------------------------------|------------------|------------------------------|
| `+`          | Addition: Adds two numbers together.                      | `5 + 3`          | `8`                          |
| `-`          | Subtraction: Subtracts the second number from the first.  | `5 - 3`          | `2`                          |
| `*`          | Multiplication: Multiplies two numbers.                   | `5 * 3`          | `15`                         |
| `/`          | Division: Divides the first number by the second.         | `5 / 3`          | `1.6666666666666667`         |
| `//`         | Floor Division: Divides and returns the largest integer.  | `5 // 3`         | `1`                          |
| `%`          | Modulus: Finds the remainder after division.              | `5 % 3`          | `2`                          |
| `**`         | Exponentiation: Raises the first number to the power of the second. | `5 ** 3` | `125`                        |

### Task 1: Multiplication
Write a Python program to multiply two numbers, 4 and 5, and print the result. Copy and paste the following into your code.py file. 

```python
print(4 * 5)
```

<details>
 <summary>Click to reveal the expected output</summary>
<pre><code>
20
</code></pre>
</details>

### Task 2: Addition
Write a Python program to add two numbers, 10 and 15, and print the result.

<details>
 <summary>Click to reveal a hint</summary>
<pre><code>
# Use the + operator to add numbers.
</code></pre>
</details>

<details>
 <summary>Click to reveal the expected output</summary>
<pre><code>
25
</code></pre>
</details>

---

## Section 1. Variables
In programming, a variable is like a container that holds data. You can think of it as a labeled box where you can store and manage information that your program can use later. The label (the variable name) helps you identify and access the data stored in the box.

1. **int** (short for "integer"): This is a type of variable that holds whole numbers, both positive and negative, and zero. For example, values like `5`, `-3`, and `100` are integers.
2. **bool** (short for "boolean"): This is a type of variable that can only hold one of two values: `true` or `false`. Booleans are often used in programming to represent conditions, helping the program make decisions.
3. **string**: This is a type of variable that holds a sequence of characters, typically used to represent text. For example, `"hello"`, `"123 Main St."`, and `"Welcome!"` are strings. Strings can include letters, numbers, spaces, and special characters.

By using these different types of variables, programmers can handle various kinds of data effectively within their programs.

### Task 1: Define and Print Variables
Define the following variables and print them:

```python
city = "New York"
temperature = 23
rainy = False

# Print the first variable
print(city)

# Now print the other two variables below
```

<details>
 <summary>Click to reveal a hint</summary>
<pre><code>
# Use the print() function to output variable values.
</code></pre>
</details>

<details>
 <summary>Click to reveal the expected output</summary>
<pre><code>
New York
23
False
</code></pre>
</details>

### Task 2: Working with Different Data Types
Define the following variables and print them:

```python
product = "Laptop"
quantity = 5
price = 999.99
in_stock = True

# Print all variables below
```

<details>
 <summary>Click to reveal a hint</summary>
<pre><code>
# Remember to print each variable separately.
</code></pre>
</details>

<details>
 <summary>Click to reveal the expected output</summary>
<pre><code>
Laptop
5
999.99
True
</code></pre>
</details>

---
Great work! You've now got a basic understanding of some simple Python syntax. 
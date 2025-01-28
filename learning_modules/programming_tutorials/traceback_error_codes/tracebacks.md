# Introduction to Debugging with Traceback Errors

When you run a piece of code and encounter an error, you'll often see a "traceback" in the serial console. This traceback provides valuable information about what went wrong, where it happened, and sometimes hints at why the error occurred.

## Understanding Traceback Errors

A traceback error acts like a map leading you to the problem in your code. It usually includes:

- **Error Type**: The kind of problem encountered (e.g., SyntaxError, NameError).
- **File and Line Number**: Where in the code the error occurred.
- **Description**: A brief explanation of the issue.

--- 
### Using Tracebacks in Debugging

1. **Read the Error Type**: Identifying whether it's a SyntaxError, NameError, etc., helps narrow down potential fixes.
2. **Locate the Line Number**: This tells you exactly where to start looking for the problem.
3. **Understand the Description**: Look for hints in the message about what might be wrong.

### Common Debugging Strategies

- **Check Syntax**: Ensure all parentheses, brackets, and quotes are correctly paired and placed.
- **Check Variable Names**: Ensure consistency in variable naming throughout your code.
- **Verify Data Types**: Ensure compatibility of data types in operations.
- **Use Print Statements**: Insert print statements to track variable values and flow.

Let's practice using these strategies with some coding tasks.

---
## Debugging Practice: Task 1 - Syntax Error

**Code to Paste:**

```python
print("Welcome to CircuitPython")
print("This line is missing something"
```

**Traceback Clue**: Look at the serial console for a "SyntaxError" message. This error usually means there's something structurally incorrect with your code, like a missing parenthesis.

<details>
 <summary>Strategy Hint</summary>
<pre><code>
# Strategy: Check to ensure every opening parenthesis has a closing pair.
</code></pre>
</details>

<details>
 <summary>Solution</summary>
<pre><code>
print("Welcome to CircuitPython")
print("This line is missing something")
</code></pre>
</details>

## Debugging Practice: Task 2 - Name Error

**Code to Paste:**

```python
animal = "Tiger"
print(animal)
print(animel)
```

**Traceback Clue**: The console should display a "NameError," indicating that a variable is being used before it's defined or is misspelled.

<details>
 <summary>Strategy Hint</summary>
<pre><code>
# Strategy: Double-check spelling of variable names; consistent naming is key.
</code></pre>
</details>

<details>
 <summary>Solution</summary>
<pre><code>
animal = "Tiger"
print(animal)
print(animal)
</code></pre>
</details>

## Debugging Practice: Task 3 - Undefined Variable

**Code to Paste:**

```python
print(total)
num1 = 5
num2 = 10
total = num1 + num2
```

**Traceback Clue**: You might see a "NameError" telling you that the variable `total` is being referenced before assignment.

<details>
 <summary>Strategy Hint</summary>
<pre><code>
# Strategy: Ensure all variables are defined before they are used.
</code></pre>
</details>

<details>
 <summary>Solution</summary>
<pre><code>
num1 = 5
num2 = 10
total = num1 + num2
print(total)
</code></pre>
</details>

## Debugging Practice: Task 4 - Type Error

**Code to Paste:**

```python
age = "20"
new_age = age + 5
print("New age:", new_age)
```

**Traceback Clue**: Look for a "TypeError," which happens when you try to perform operations incompatible with the variables' data types.

<details>
 <summary>Strategy Hint</summary>
<pre><code>
# Strategy: Ensure that arithmetic operations involve compatible data types. Convert strings to numbers where needed using functions like int().
</code></pre>
</details>

<details>
 <summary>Solution</summary>
<pre><code>
age = "20"
new_age = int(age) + 5
print("New age:", new_age)
</code></pre>
</details>

--- 
By practicing with these tasks and learning to decode traceback errors, you'll build your ability to debug efficiently and write cleaner, more effective code. Remember, debugging is an essential skill to build as a programmer. 
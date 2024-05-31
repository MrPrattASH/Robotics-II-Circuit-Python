# Selection Statements
One of the more important parts of computer programming and robotics is the ability for robots to think. They do so through *selection statements*. Think about the following:
* If it is raining, wear a raincoat to school. Otherwise, don't bring a jacket. 
* If you are hungry, eat some food. If Not, don't eat food. 
* If you have money, purchase lunch. Else, bring lunch from home. 

You already intuitively know how to create selection statements, we do it all the time in real life. In programming, it looks a little different. Consider the rainjacket above, this is how we would write it in code. 
```
is_raining = False

if is_raining:
    print("I should bring a jacket!")
else:
    print("Great, I don't need a jacket!")
```

## Selection Statements in Python
In Python, we use `if` and `else` statements to signify *conditional statements* or *selection statements*. Similar to our while True loop, anything indented is **inside** the selection statement
```
if is_raining:
    print("this is inside the selection statement, and only prints if is_raining is True)
print("this is  outside. Notice the indentations has changed. This will ALWAYS print")
```
With conditional statements, only `True` statements will run. We use the sing `==` to check if something is equivalent. If you remember with variables:
* ` distance = 50` is an **assignment** statement. We are **assigning** the value of `50` to the variable `distance`. 
* `if distance == 50:` This is a comparrison or conditional statement. 2 `==` in a row denote an equivalency check, are these values `distance` and `50` equivalent? If yes, then it is `True` and will run. 
For example:
```
distance = 50
if distance == 50:
    print("this was a true statment! and this WILL print)
else:
    print("this is a false statement, because the above 'if' was true")
```

## Practice Exercise #1
Using the code below as a template, write a selection statement that:
* an if statement that will print if the variable `is_touched` is True. 
```
is_touched = True # don't change this

# write your code here vvv



# write your code here ^^^

print("The touch sensor was pressed")
```

## Practice Exercise #2
Using the code below as a template, write a selection statement that:
* an if/else statement that will print "touched"m if `is_touched` is `True`, and "non touched" if `is_touched` is `False`.
```
is_touched = False # don't change this

# write your code here vvv



# write your code here ^^^

print("Touch sensor test complete")
```

## If, Elif, Else
The `if` statement is helpful if we have one condition to check. The `else` statement **always** runs if the above if statement is NOT true. However, what if we have 2 different statements that we want to check? Then we can use an if, elif, else statement. (elif == "else if")
```
distance = 50

if distance > 50:
    print("far away")
elif distance < 50 and distance > 25: 
    print("just right)
else:
    print("too close!")
```

## Practice Exercise #3
Using the code below as a template, write a selection statement that:
* an if/elif/else statement that:
* if volume is < 20, print "turn up the volume"
* if volume is > 20 and < 50, print "just right"
* else, print "turn it down"
```
volume = 24
# write your code here vvv



# write your code here ^^^

print("volume test complete")
```

## Practice Exercise #4
*modified from [this](https://sites.google.com/view/circuitpython/tutorials/button-and-led/conditionals-i) tutorial* 

Using the code below as a template, write a selection statement that:
* For this exercise, we've defined two variables, `eight_characters` and  `contains_number` to check the strength of a password. 
* Write a conditional statement that assigns a variable called `password_strength` depending on the following criteria:
    * If both variables are True, set password_strength to "Strong"
    * If only one of the variables is True, set password_strength to "Medium"
    * Otherwise, set password_strength to "Weak"
* Note: it is not required to actually *create* a password for this challenge, only to evaluate a potential password based on the criteria

```
eight_characters = True
contains_number = False
# don't change these ^^^

# write your code here vvv



# write your code here ^^^

print(password_strength)
```


##### Quick Links
* [Home](README.md)
* [Tutorials](learning_modules/tutorials_list.md)
* [Circuit Python Cheat Sheet](learning_modules/circuit_python_cheatsheet.md)
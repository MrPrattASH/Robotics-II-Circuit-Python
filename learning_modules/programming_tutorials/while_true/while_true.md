# Forever Loops
In robotics, we always run our programs forever, using iteration, or a loop. 

In this first tutorial, we'll learn:
* What a Loop or "iteration" is. 
* How loops differ from single line programs

Let's try the difference between these 2 programs

### Single Line Program
1. Connect the M4 to your computer, and load *code.py*
2. On line 1, write
` print("this is a non-looped program)`
3. Open the serial console. 
4. Save this program and observe the serial output

### While True
1. delete all existing code. 
2. write in this code:

``` 
import time

while True:
    print("this is in a loop!)
    time.sleep(1)

```

3. Open the serial console
4. Save this program and observe the serial output. 

## Examining a While True Loop:
You've likely noticed by now that rather than printing the statement once, it will print forever, in a loop! That's what the "while True:" statement does. Let's examine this:

* The word "while" is a condition for a loop. While the condition inside the following statement is true, the code "inside" the loop will continue to run. In our case, it will print "This is in a loop!" forever. 
* The words next to the "while" are the conditional statement. We only ever run "True" statements:
     * `while True:` this will run because the statement is simply "True"
     * `while 1 == 1:` This will also run because 1 is equivalent to 1
     * `while 5 == 7:` This will *never* run, because 5 is not equal to 7. 
* The last part of our conditional statement is the ":" colon. The colon signifies to our computer that the statement is over. 
    * much like this indentation in the bullet, anything that is *indented* inside of the "while True:" statement will run. For example try to run the following code:
* The `import time` and `time.sleep(1)` are special lines from a "module" that allow us to put second pauses into our code. 

``` 
import time

print("this is before the loop")
while True:
    print("this is inside the loop")
    print("Still inside the loop")
    time.sleep(1)
print("this is NOT indented, so it is outside the loop")
print("the statement directly above, and this statement, will NEVER print")
```

* The final 2 `print` statements will **never** print on our serial console, because they are *after* our forever, while True: loop. 
* In python, indents (tabs or x4 spaces) keep track of what parts of code are inside loops, or conditional statements, and what are not. 

# Key Takeaways
All of our robotics programs will have a single while True: loop inside of them, and this is where all of our code will run. Much like a robot vacuum, we want our robot following instructions forever, until it is powered off. 
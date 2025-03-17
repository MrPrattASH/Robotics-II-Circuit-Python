# Drawing Robot Challenge

Welcome to the Drawing Robot Challenge! This challenge will get you to practice creating user-defined functions for your drawing robot and exploring creative shape-making using functions, loops, and parameters. We're going to strap a marker onto our rover, and practice drawing some shapes. 

# Video Tutorial

This video tutorial, **you do not need to watch the entire vide**
* Use the "Chapters" function to skip ahead and watch the marker mounting section. 
* After mounting your marker, move on to the challenges below. 
* *If you get stuck on these challenges, come back and watch through the remainder of the video.*

{% include youtube.html id="eVwYuASxglM" %}

***

## 1. Functions for Stop

**Challenge:** Create a function that stops your rover

<details>
<summary>Click to reveal a solution</summary>
<pre><code>
def stop():
    m1.throttle = 0  # Replace with your calibrated stop value for m1
    m2.throttle = 0  # Replace with your calibrated stop value for m2
</code></pre>
</details>

## 2. Move Forward Function

**Challenge:** Create a function to drive the rover forward for a specified duration, using a parameter to define this time.

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# Accept a parameter in your function to determine how many seconds the rover should move forward.
# Pass the parameter to a sleep function to control the movement duration.
</code></pre>
</details>

<details>
<summary>Click to reveal a solution</summary>
<pre><code>
def move_forward(sleep_time):
    m1.throttle = 0.5  # Adjust throttle for m1
    m2.throttle = -0.5 # Adjust throttle for m2 (or invert if needed)
    time.sleep(sleep_time)
    stop()
</code></pre>
</details>

## 3. Turning Function

**Challenge:** Write a function to turn your rover, using a parameter for the turning duration.

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# Turn the motors in opposite directions for a successful turning function.
# Use a parameter to specify the duration of the turn.
</code></pre>
</details>

<details>
<summary>Click to reveal a solution</summary>
<pre><code>
def turn(duration):
    m1.throttle = 0.5  # Throttle for clockwise turn
    m2.throttle = 0.5  # Ensure both motors are coordinated correctly
    time.sleep(duration)
    stop()
</code></pre>
</details>

## 4. Calibrating 90° and 180° Turns

**Challenge:** Calibrate your rover for precise 90° and 180° turns, and store these durations in variables.

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# You might need to experiment with different durations to achieve precise angles.
# Store these durations in variables to use in your functions.
</code></pre>
</details>

<details>
<summary>Click to reveal a solution</summary>
<pre><code>
turn_90_duration = 0.6  # Replace with your calibrated value
turn_180_duration = 1.2 # Replace with your calibrated value

turn(turn_90_duration)
turn(turn_180_duration)
</code></pre>
</details>

## 5. Create a Square Shape

**Challenge:** Use your functions to make the robot draw a square. A square has four equal sides, each connected by 90° turns.

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# Use a for loop to repeat movement and turning four times.
# Consider how long each side should be relative to your movement duration.
</code></pre>
</details>

<details>
<summary>Click to reveal a solution</summary>
<pre><code>
def draw_square():
    for i in range(4):
        move_forward(3)  # Move forward for 3 seconds
        turn_90()        # Turn 90°
</code></pre>
</details>

## 6. Free Challenges

**Challenge:** Utilize `for` loops to create at least three custom shapes. This is your opportunity to design creatively!

### Ideas for Custom Shapes

<details>
<summary>Click to reveal a hint for a triangle</summary>
<pre><code>
# For an equilateral triangle, use three sides and adjust your turn to approximately 120°.
</code></pre>
</details>

<details>
<summary>Click to reveal a solution for a triangle</summary>
<pre><code>
def draw_triangle():
    for _ in range(3):
        move_forward(3)
        turn(1.33)  # Example duration for a 120° turn
</code></pre>
</details>

<details>
<summary>Click to reveal a hint for a pentagon</summary>
<pre><code>
# For a regular pentagon, use a turn angle of approximately 72°.
</code></pre>
</details>

<details>
<summary>Click to reveal a solution for a pentagon</summary>
<pre><code>
def draw_pentagon():
    for _ in range(5):
        move_forward(2)
        turn(0.8)  # Example duration for a 72° turn
</code></pre>
</details>
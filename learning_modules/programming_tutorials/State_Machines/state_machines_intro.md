# State Machine Tutorial

In robotics, we often need our creations to do more than just follow a single list of commands. They need to react to the world around them. For that, we use a powerful tool called a **State Machine**.

A state machine is a way to model a robot's behavior as a collection of "states." A **state** is simply what the robot is doing right now (like "driving forward" or "waiting for a command"). The robot stays in a state until an **event**—like a sensor reading—causes it to **transition** (or switch) to a new state.

## Why Use State Machines?

Traditional programming often runs from top to bottom. This is fine for simple tasks, but robots in the real world need to make constant decisions. Is there a wall ahead? Is my motor spinning fast enough? State machines give us a clean, organized way to handle these situations. Instead of a messy web of `if/else` statements, we get a clear map of our robot's "behaviors" (states) and the rules for switching between them. It makes our code much easier to read, test, and improve. It also makes our code safer for humans to interact with our robot. 

## Example: The Simple Bumper Bot

Let's design a robot that does one thing: it drives forward until its bumper sensor hits a wall, and then it stops. This robot needs only two states:
* **"Moving Forward"** and **"Stopped"**.
* Transition Event 
* *(For this simple example, we'll imagine a person has to reset the robot to make it move again)*


Here's the high-level diagram:

```ascii
+-----------------+      Bumper Hit       +-----------+
|                 | --------------------> |           |
|  Moving Forward |                       |  Stopped  |
|                 | <-------------------- |           |
+-----------------+    (Manual Reset)     +-----------+
```

Now let's break down what's happening inside each state using a flowchart.

---

### **STATE: Moving Forward**

This is the robot's starting state. Its job is to move and check its bumper. It's important to note that the robot **remains in the MOVING_FORWARD state until a transition event happens**, in this case, the bumper pressed

```
STATE: MOVING_FORWARD
---------------------------------
[ ACTION ] Start both motors to drive forward.
      |
      V
[ SENSE ] Check the front bumper sensor.
      |
      V
[ DECISION ] Is the bumper pressed?
      |
      +---- [ IF FALSE ] ----> Stay in MOVING_FORWARD state.
      |
      +---- [ IF TRUE ]  ----> TRANSITION to STOPPED state.
```

### **STATE: Stopped**

In this state, the robot does nothing but wait.

```
STATE: STOPPED
---------------------------------
[ ACTION ] Stop both motors.
      |
      V
[ .... ] Robot waits here indefinitely.
```

The critical thing to note here is the **transition event**: when the `bumper is pressed` decision is `TRUE`, the robot transitions from `MOVING_FORWARD` to `STOPPED`. There is no transition event from Stopped. 

***

## Practice 1: The Blinking Light Bot

Your turn! Let's create a state machine for a robot with a single light and a single button. When you press the button, the light should turn on. When you press it again, the light should turn off.

The two states are **"Light On"** and **"Light Off"**.

Your task is to write out the flowchart-style pseudo-code for each state.

**Hints:**
*   What is the "SENSE" action in each state? (think about what hardware component is the "sensor" in this robot)
*   What is the "DECISION" that causes a transition? (usually this is the "if" or "elif" statement)
*   The "ACTION" in each state is very simple: what should the light be doing?

<details>
<summary>Click to reveal the solution</summary>
<pre><code>
STATE: LIGHT_ON
---------------------------------
[ ACTION ] Turn the light ON.
      |
      V
[ SENSE ] Check the button sensor.
      |
      V
[ DECISION ] Is the button pressed?
      |
      +---- [ IF TRUE ]  ----> TRANSITION to LIGHT_OFF state.


STATE: LIGHT_OFF
---------------------------------
[ ACTION ] Turn the light OFF.
      |
      V
[ SENSE ] Check the button sensor.
      |
      V
[ DECISION ] Is the button pressed?
      |
      +---- [ IF TRUE ]  ----> TRANSITION to LIGHT_ON state.

      ** Note, I excluded the IF FALSE conditions here, as it simply is "stay in current state"**
</code></pre>
</details>

***

## Challenge #1: The Patrolling Guard Bot

Design a state machine for a robot that 'patrols' a hallway in the school. It moves in one direction until it hits a wall, then it turns around and moves in the other direction.

It will have two states: **"Moving Left"** and **"Moving Right"**. It has a bumper on both the left and right sides. Assume that we have NO human or obstacle detection. It's not a very smart robot. 

```
# Write the flowchart pseudo-code for the "Moving Left" state.
# It should move left and check its left bumper.

# Write the flowchart pseudo-code for the "Moving Right" state.
# It should move right and check its right bumper.
```

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# The action in the "Moving Left" state is to drive the motors to move left.
# The sense action is to check the left bumper.
# The decision will cause a transition to the "Moving Right" state.
</code></pre>
</details>

<details>
<summary>Click to reveal an example solution</summary>
<pre><code>
STATE: MOVING_LEFT
---------------------------------
[ ACTION ] Start motors to move LEFT.
      |
      V
[ SENSE ] Check the LEFT bumper sensor.
      |
      V
[ DECISION ] Is the LEFT bumper pressed?
      |
      +---- [ IF TRUE ]  ----> TRANSITION to MOVING_RIGHT state.


STATE: MOVING_RIGHT
---------------------------------
[ ACTION ] Start motors to move RIGHT.
      |
      V
[ SENSE ] Check the RIGHT bumper sensor.
      |
      V
[ DECISION ] Is the RIGHT bumper pressed?
      |
      +---- [ IF TRUE ]  ----> TRANSITION to MOVING_LEFT state.
</code></pre>
</details>

## Challenge #2: The Scaredy Bot

This robot is afraid of the dark! It has a light sensor. It will stay in one place as long as the lights are on. If it gets dark, it will spin in a circle in a panic until the light comes back on.

The two states are **"Waiting Calmly"** and **"Spinning in Panic"**.

```
# Write the flowchart pseudo-code for the "Waiting Calmly" state.
# It should be still and check the light sensor.

# Write the flowchart pseudo-code for the "Spinning in Panic" state.
# It should be spinning and checking the light sensor.
```

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# Think about what light sensor reading means "dark." A low value or a high value?
# Let's assume a low light level means it's dark.
# The transition from "Waiting Calmly" to "Spinning in Panic" happens when the light level is low.
</code></pre>
</details>

<details>
<summary>Click to reveal an example solution</summary>
<pre><code>
STATE: WAITING_CALMLY
---------------------------------
[ ACTION ] Stop all motors.
      |
      V
[ SENSE ] Read the light sensor value.
      |
      V
[ DECISION ] Is the light level LOW (it's dark)?
      |
      +---- [ IF TRUE ]  ----> TRANSITION to SPINNING_IN_PANIC state.


STATE: SPINNING_IN_PANIC
---------------------------------
[ ACTION ] Start motors to spin in a circle.
      |
      V
[ SENSE ] Read the light sensor value.
      |
      V
[ DECISION ] Is the light level HIGH (lights are on)?
      |
      +---- [ IF TRUE ]  ----> TRANSITION to WAITING_CALMLY state.
</code></pre>
</details>

***

## Challenge #3: The "Fetch" Bot (3 States)

This robot is programmed to play a simple game of fetch. It will wait patiently, and when you press a button, it will run forward for a short time to "get the ball," and then run backward to "bring it back."

This robot has three states:
1.  **Waiting:** The robot is stopped and waiting for the game to start.
2.  **Fetching:** The robot is driving forward.
3.  **Returning:** The robot is driving backward to its starting spot.

It uses a **button** to start and an internal **timer** to know how long to drive.

```
# Write the flowchart pseudo-code for the "Waiting" state.
# It should be still and check if the button has been pressed.

# Write the flowchart pseudo-code for the "Fetching" state.
# It should drive forward and use a timer (e.g., 3 seconds) to know when to stop.

# Write the flowchart pseudo-code for the "Returning" state.
# It should drive backward for the same amount of time before going back to wait.
```

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# The transition from "Waiting" to "Fetching" is a button press.
# The transitions from "Fetching" to "Returning", and from "Returning" back to "Waiting", are both based on a timer finishing.
</code></pre>
</details>

<details>
<summary>Click to reveal an example solution</summary>
<pre><code>
STATE: WAITING
---------------------------------
[ ACTION ] Stop all motors.
      |
      V
[ SENSE ] Check the button sensor.
      |
      V
[ DECISION ] Is the button pressed?
      |
      +---- [ IF TRUE ]  ----> TRANSITION to FETCHING state.


STATE: FETCHING
---------------------------------
[ ACTION ] Drive motors FORWARD. Start a 3-second timer.
      |
      V
[ SENSE ] Check if the timer is finished.
      |
      V
[ DECISION ] Is 3 seconds over?
      |
      +---- [ IF TRUE ]  ----> TRANSITION to RETURNING state.


STATE: RETURNING
---------------------------------
[ ACTION ] Drive motors BACKWARD. Start a 3-second timer.
      |
      V
[ SENSE ] Check if the timer is finished.
      |
      V
[ DECISION ] Is 3 seconds over?
      |
      +---- [ IF TRUE ]  ----> TRANSITION to WAITING state.
</code></pre>
</details>

***

## Challenge #4: Smart Line Follower (4 States)

This robot is designed to follow a black line on a white floor. However, it also has a distance sensor on the front to avoid collisions. If it sees an obstacle, it will stop and wait for the obstacle to be moved before it continues following the line.

This robot has four states:
1.  **Follow Line:** The robot is centered on the line and driving forward.
2.  **Adjust Left:** The robot has drifted off the line to the right and needs to turn left to get back on track.
3.  **Adjust Right:** The robot has drifted off the line to the left and needs to turn right to get back on track.
4.  **Obstacle Stop:** The robot has detected something in its path and is waiting.

It uses **two line sensors** (left and right) and a **front distance sensor**.

```
# Write the flowchart pseudo-code for all four states.
# In any of the three moving states, what should happen if the distance sensor detects an obstacle?
# How does the robot know when it's back on the line after adjusting?
```

<details>
<summary>Click to reveal a hint</summary>
<pre><code>
# The "Obstacle Stop" state can be reached from ANY of the other three states.
# Assume the robot is on the line when both left and right sensors see black.
# If the right sensor sees white, the robot has drifted right.
# If the left sensor sees white, the robot has drifted left.
</code></pre>
</details>

<details>
<summary>Click to reveal an example solution</summary>
<pre><code>
STATE: FOLLOW_LINE
---------------------------------
[ ACTION ] Drive motors FORWARD.
      |
      V
[ SENSE ] Read distance sensor AND both line sensors.
      |
      V
[ DECISION ] Is there an obstacle?
      |
      +---- [ IF TRUE ] ----> TRANSITION to OBSTACLE_STOP state.
      |
      +---- [ IF FALSE ] ---> [ DECISION ] Does right sensor see WHITE?
                                |
                                +---- [ IF TRUE ] ----> TRANSITION to ADJUST_LEFT state.
                                |
                                +---- [ IF FALSE ] ---> [ DECISION ] Does left sensor see WHITE?
                                                        |
                                                        +---- [ IF TRUE ] ----> TRANSITION to ADJUST_RIGHT state.


STATE: ADJUST_LEFT
---------------------------------
[ ACTION ] Turn slightly LEFT.
      |
      V
[ SENSE ] Read distance sensor AND right line sensor.
      |
      V
[ DECISION ] Is there an obstacle?
      |
      +---- [ IF TRUE ] ----> TRANSITION to OBSTACLE_STOP state.
      |
      +---- [ IF FALSE ] ---> [ DECISION ] Does right sensor see BLACK again?
                                |
                                +---- [ IF TRUE ] ----> TRANSITION to FOLLOW_LINE state.


STATE: ADJUST_RIGHT
---------------------------------
[ ACTION ] Turn slightly RIGHT.
      |
      V
[ SENSE ] Read distance sensor AND left line sensor.
      |
      V
[ DECISION ] Is there an obstacle?
      |
      +---- [ IF TRUE ] ----> TRANSITION to OBSTACLE_STOP state.
      |
      +---- [ IF FALSE ] ---> [ DECISION ] Does left sensor see BLACK again?
                                |
                                +---- [ IF TRUE ] ----> TRANSITION to FOLLOW_LINE state.


STATE: OBSTACLE_STOP
---------------------------------
[ ACTION ] Stop all motors.
      |
      V
[ SENSE ] Read the distance sensor.
      |
      V
[ DECISION ] Is the obstacle gone?
      |
      +---- [ IF TRUE ]  ----> TRANSITION to FOLLOW_LINE state.
</code></pre>
</details>

***

## Challenge #5: The Warehouse Bot (5 States)

This is your final design challenge! There is no solution provided, so it's up to you to think through the logic completely.

**The Mission:**
Your robot works in a small warehouse. It must start at a home base, follow a line to a pickup station, wait for a package to be "loaded" (signaled by a button press), follow the line to a red-colored drop-off zone, "unload" the package (by waiting for 3 seconds), and finally return to the home base to start again.

**The Robot's States:**
You must design a system with these five states:
1.  **Following to Pickup:** The robot is following the line from home base to the package pickup station.
2.  **Waiting for Load:** The robot has arrived at the pickup station and is waiting for the "load package" button to be pressed.
3.  **Delivering Package:** The robot has the package and is following the line from the pickup station to the drop-off zone.
4.  **Dropping Off:** The robot has found the red drop-off zone and is waiting for 3 seconds to "unload."
5.  **Returning Home:** The robot is now empty and following the line back to the home base.

**The Robot's Sensors:**
*   **Line Sensor(s):** To follow the black line.
*   **Bumper Sensor:** To detect when it has arrived at the pickup station wall.
*   **Button:** To signal that a package has been loaded.
*   **Color Sensor:** To detect the red drop-off zone.
*   **Internal Timer:** To handle the 3-second drop-off time.

**Your Task:**
1.  Think about the transitions. What event causes the robot to go from one state to the next? (e.g., from `Following to Pickup` to `Waiting for Load`).
2.  Write the flowchart-style pseudo-code for **each of the five states**. Be sure to include the Action, Sense, and Decision steps for every state. Good luck
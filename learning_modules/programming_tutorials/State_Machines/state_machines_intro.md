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

The critical thing to note here **transition event**: when the `bumper is pressed` decision is `TRUE`, the robot transitions from `MOVING_FORWARD` to `STOPPED`.

***

## Practice 1: The Blinking Light Bot

Your turn! Let's create a state machine for a robot with a single light and a single button. When you press the button, the light should turn on. When you press it again, the light should turn off.

The two states are **"Light On"** and **"Light Off"**.

Your task is to write out the flowchart-style pseudo-code for each state.

**Hints:**
*   What is the "SENSE" action in each state?
*   What is the "DECISION" that causes a transition?
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
      +---- [ IF FALSE ] ----> Stay in LIGHT_ON state.
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
      +---- [ IF FALSE ] ----> Stay in LIGHT_OFF state.
      |
      +---- [ IF TRUE ]  ----> TRANSITION to LIGHT_ON state.
</code></pre>
</details>

***

## Challenge #1: The Patrolling Guard Bot

Design a state machine for a robot that patrols a hallway. It moves in one direction until it hits a wall, then it turns around and moves in the other direction.

It will have two states: **"Moving Left"** and **"Moving Right"**. It has a bumper on both the left and right sides.

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
      +---- [ IF FALSE ] ----> Stay in MOVING_LEFT state.
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
      +---- [ IF FALSE ] ----> Stay in MOVING_RIGHT state.
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
      +---- [ IF FALSE ] ----> Stay in WAITING_CALMLY state.
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
      +---- [ IF FALSE ] ----> Stay in SPINNING_IN_PANIC state.
      |
      +---- [ IF TRUE ]  ----> TRANSITION to WAITING_CALMLY state.
</code></pre>
</details>
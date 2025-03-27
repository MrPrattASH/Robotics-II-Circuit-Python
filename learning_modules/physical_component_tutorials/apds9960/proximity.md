# APDS-9960 Proximity Sensor Tutorial

In this tutorial, you'll learn how to use the APDS-9960 sensor in proximity mode. This sensor can detect the presence of an object and measure how close it is to the sensor. You'll learn how to wire the sensor, understand how it works, see a code example, and complete some challenges to test your understanding.

# Video Tutorial
{% include youtube.html id="ERC_cFBGCIc" %}

***

# Text Tutorial

![Wiring Diagram](wiring.png)

To wire the APDS-9960 sensor using StemmaQT, follow these steps:

1. **Connect the Blue Wire (Data):** Connect the blue wire to the data (SDA) pin on your microcontroller board.
2. **Connect the Yellow Wire (Data):** Connect the yellow wire to the clock (SCL) pin on your microcontroller board.
3. **Power and Ground:**
   - Connect the red wire to the 3.3V or 5V power pin.
   - Connect the black wire to the ground (GND) pin.

***

## How the Proximity Sensor Works

The APDS-9960 sensor includes a proximity sensor that can measure the distance to an object without physical contact.

- **Proximity Detection:** The sensor uses infrared light to detect objects. It emits infrared light, which reflects off nearby objects and returns to the sensor.
- **Signal Processing:** The sensor processes the reflected light to determine how close an object is.
- **Use Cases:** Proximity sensing is used in applications like gesture recognition, detecting when a device is picked up, and if an object has gotten relatively closer or further away. 

### I2C Communication

I2C (Inter-Integrated Circuit) is a communication protocol commonly used in microcontrollers and sensors to facilitate communication between devices. It allows multiple "slave" devices to communicate with one or more "master" controllers using only two wires, making it a simple and efficient method for data transfer. Effectively we could connect 20+ sensors to these single 2 pins and be able to interact with them all, rather than needing 20 individual digital/analog pins. 

#### Key Components of I2C:

1. **SCL (Serial Clock Line):**
   - SCL is the clock line that is controlled by the master device.
   - It synchronizes the data transfer between the master and slave devices.
   - Both the master and slave devices rely on SCL to know when to read or write data.

2. **SDA (Serial Data Line):**
   - SDA is the data line used to transfer data between devices.
   - It is a bidirectional line, meaning it can be used by both master and slave devices to send and receive data.
   - Data on the SDA line is transferred in synchronization with the clock pulses on the SCL line.

#### How I2C Works:

- **Addressing:** Each device on the I2C bus has a unique address. The master sends an address to indicate which slave it wants to communicate with. This is typically denoted as [0x0a] or [0x20], etc, with each binary being a different device. 
- **Data Transfer:** Data is transferred in bytes. The master controls the clock, while data is sent over the SDA line in synchronization with the clock pulses.

***

## Code Example

Here's a basic code example to get started with the APDS-9960 sensor in proximity mode:

```python
import board
import busio
import time
import adafruit_apds9960.apds9960

# Set up I2C connection
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

# Enable proximity sensing
sensor.enable_proximity = True

while True:
    proximity = sensor.proximity
    print("Proximity:", proximity)
    time.sleep(1)
```

***

## Challenges

### Challenge 1: Detecting Object Presence

Use the proximity sensor to detect when an object is placed near the sensor. Try different objects and observe the proximity values.

### Challenge 2: Proximity Alert

Create a function that triggers an alert when an object comes within a certain distance of the sensor.

- Use a threshold for proximity to determine when to alert.
- Experiment with different distances to set your threshold.

<details>
<summary>Click to reveal a hint for Challenge 2</summary>
You can use a simple threshold, e.g., if proximity > 50, trigger an alert. Adjust the threshold based on your needs.
</details>

# project_planner

[<img src="/images/protodraw.png" alt="protodraw.png" width="350" height="250">](/images/protodraw.png)

## Project Goal:

To make a ping pong float in a tube at a specific height using a fan controlled by a turning a potentiometer.

## Pseudo Code
Step 1. Get a rotor spinning

Step 2. Find the distance of the ping pong ball using the HCSR04

Step 3. Put step 1+2 together without PID

Step 4. Add PID

```python
import time
import board
import adafruit_hcsr04  # this line imports code for the ultrasonic sensor
from analogio import AnalogIn  # this line imports code for the potentiometer


Setpoint = 0   # the input variable for the PID, controlled by the potentiometer

# some helpful reference code for the ultrasonic sensor
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)   # this sets it up for use
print((sonar.distance,))
time.sleep(0.1)

# some helpful reference code for the potentiometer:
potentiometer = AnalogIn(board.A1)  # potentiometer connected to A1, power & ground
while True:
 
    print((potentiometer.value,))      # Display value
 
    time.sleep(0.25)          

# SetPoint should equal a mapped version of the potentiometer value

# Use PID algorithm to determine the correct output value for the motor

# We might do an early version of PID, just P value,
# if distance < SetPoint, increase VMotor
# if distance > SetPont, decrease VMotor
```

## Progress Notes:

Sean: I have currently wired the potentiometer and the ultransonic distance sensor up to the metro express and have both up running. I have the motor hooked up to the 9V battery pack, but I need to install some circuitPython libraries to control it. I currently have version 5x of circuitPython downloaded, and I need to replace my lib folder with version 6x, but I'm not sure how to do that. Once I am able to control the motor with the potentiometer, I'll be ready to put the whole project together in the lab with Hank.

Here is the current code I have put together on March 13. 

[Current Code]()

## CAD Rough Sketch

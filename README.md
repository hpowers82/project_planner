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
The propeller is 5.5cm in diameter, and the ping pong ball is 4cm in diameter.
Mesh or some thin rods would be needed just above the propeller in the tube in order to keep the ping pong ball from hitting the propeller and damaging it.
A normal motor would probably be only able to handle lifting the ball up a foot at most unless we add more power, so the length of the tube only needs to account for the propeller + 1 foot of length for the ping pong ball to move up and down in.

Materials Needed for Wiring:
- Motor kit
- Potentiometer

## CAD Rough Sketch

# project_planner

[<img src="/images/protodraw.png" alt="protodraw.png" width="350" height="250">](/images/protodraw.png)

## Project Goal:

To make a ping pong float in a tube at a specific height using a fan controlled by a turning a potentiometer.

## Pseudo Code
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

```
## CAD Rough Sketch


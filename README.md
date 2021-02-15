# project_planner

[<img src="/images/protodraw.png" alt="protodraw.png" width="350" height="250">](/images/protodraw.png)

## Project Goal:

To make a ping pong float in a tube at a specific height using a fan controlled by a turning a potentiometer.

## Pseudo Code
```python
import time
import board
from analogio import AnalogIn  # this line sets up the potentiometer




Setpoint = 0   # the input variable for the PID, controlled by the potentiometer

# some helpful reference code for the potentiometer:
potentiometer = AnalogIn(board.A1)  # potentiometer connected to A1, power & ground
while True:
 
    print((potentiometer.value,))      # Display value
 
    time.sleep(0.25)          

```
## CAD Rough Sketch


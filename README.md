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

3/13/21 Sean: I have currently wired the potentiometer and the ultransonic distance sensor up to the metro express and have both up running. I have the motor hooked up to the 9V battery pack, but I need to install some circuitPython libraries to control it. I currently have version 5x of circuitPython downloaded, and I need to replace my lib folder with version 6x, but I'm not sure how to do that. Once I am able to control the motor with the potentiometer, I'll be ready to put the whole project together in the lab with Hank.

3/22/21 Sean: I have wired up the LCD and have it printing out the distance values from the ultrasonic sensor. I had a problem with printing out the current potentiometer value on my LCD screen. The LCD would print out the value from the potentiometer when I would save my code, but it wouldn't change when I would turn the potentiometer. This is what my code for the potentiometer and LCD looked like:
```python
# Code for the potentiometer:
potentiometer = AnalogIn(board.A1)  # potentiometer connected to A1, power & ground
Setpoint = potentiometer.value  # the input variable for the PID, controlled by the potentiometer

while True:
 
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print('Setpoint: ' + str(Setpoint))
    lcd.set_cursor_pos(1,0)
    lcd.print('Distance: ' + str(sonar.distance))
    time.sleep(.05)
```
I then realized that the metro express was only reading the potentiometer value once because I had the "Setpoint = potentiometer.value" line in the main part of the code, instead of in the "While True:" loop. I then cut and pasted that line of code into the loop and it started working:
```python
# Code for the potentiometer:
potentiometer = AnalogIn(board.A1)  # potentiometer connected to A1, power & ground

while True:
    Setpoint = potentiometer.value  # the input variable for the PID, controlled by the potentiometer
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print('Setpoint: ' + str(Setpoint))
    lcd.set_cursor_pos(1,0)
    lcd.print('Distance: ' + str(sonar.distance))
    time.sleep(.05)
```
The next problem I'm working on right now is the potentiometer has a range of values it will print out from 0 to 65,520. I need to use the potentiometer to set a distance from 0 to 30cm. I need to figure out how to map the values so that the LCD will print out values 0-30, controlled by the potentiometer.

3/24/21 Sean: I was having a problem with my distance reading on my LCD screen. Every time the ultrasonic sensor would get an error, the distance reading on my lcd would go blank. For example: maybe the sensor has a wire in front of it that it is trying to read or it is suddenly super far from its target, an error would come up on my serial monitor (Beagle) . In order to get my lcd displaying the distance again, I would have to save the code again and reset everything. I saw on [Alden's circuitPython repo](https://github.com/adent11/CircuitPython) that for his distance sensor code he had this:
```python
while True:
    try:
        dist = ultrasonic.distance
        print(dist)
        if dist <= 20:
            r = simpleio.map_range(dist, 0, 20, 255, 0)
            b = simpleio.map_range(dist, 5, 20, 0, 255)
            g = simpleio.map_range(dist, 20, 35, 0, 255)
        else:
            r = simpleio.map_range(dist, 0, 20, 255, 0)
            b = simpleio.map_range(dist, 20, 35, 255, 0)
            g = simpleio.map_range(dist, 20, 35, 0, 255)
        neopixel.fill((int(r), int(g), int(b)))
        print(dist)
    except RuntimeError:
        print("Retrying!")
    time.sleep(.1)
```
The main part of this is the 'try:' and 'except' function. If the 'dist = ultrasonic.distance' line comes up with an error within the 'try:' function, the 'except RuntimeError:' will be activated. I made it so that my LCD would print "Retrying!" in that situation. Using this setup for running the 'dist = ultrasonic.distance' fixed my problem, so that every time there is an error, the LCD prints "Retrying" and it auto-resets so it imediately starting re-printing the distance reading.
I now have the LCD printing out the mapped values for my potentiometer from 0-30. A helpful website I referenced for mapping values using circuitPython was [this](https://circuitpython.readthedocs.io/projects/simpleio/en/latest/api.html). Here is my current code I'm using for mapping the potentiometers ("Setpoint" is the variable I'm using) :
```python
   Setpoint = potentiometer.value  # the input variable for the PID, controlled by the potentiometer
   Setpoint = simpleio.map_range(Setpoint,0,65520,0,30)  # maps the potentiometer value using the variable setpoint, changes the range from 0-65,520 to 0-30
```

3/29/21 Sean: The only components to the project that I didn't have wired were the motor and the battery pack. I popped in to Mr H's office hours this morning and got some help with the wiring, here is a diagram:
![Wiring Diagram](images/Motor+batterypack+potentiometer-wiring.png
)
Even though this diagram is for an arduino, I used it for a Metro Express. For a Metro Express, the wire that connects the Metro to the transistor has to be connected to pin A0 with the scwiggly sine line nex to it. I wired my potentiometer to the A1 pin on my Metro Express. The most important things to remember when wiring the battery pack are to not have in all the batteries until you are sure no power/ground wires are touching each other, and make sure there are no wires connecting the battery pack power to the Metro Express, because it isn't made to handle that much power.
For the code, I can use the potentiometer to make the motor accelerate and decelerate smoothly. This is my current code for testing/running the motor/potentiometer control:
```python
import time
import board
import simpleio
from analogio import AnalogIn
from analogio import AnalogOut # code for the motor speed/voltage stuff

analog_out = AnalogOut(board.A0) # motor control pin

# Code for the potentiometer:
potentiometer = AnalogIn(board.A1)  # potentiometer connected to A1, power & ground

while True:
    analog_out.value = potentiometer.value
    time.sleep(.1)
```
The next thing I need to do is integrate this code into my full code with the ultrasonic sensor and LCD.

Here is the current code I have put together on March 24. 

[Current Code](https://github.com/hpowers82/project_planner/blob/main/March-24-Code.py)

## CAD Rough Sketch

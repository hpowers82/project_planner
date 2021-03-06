import time
import board
import adafruit_hcsr04  # this line imports code for the ultrasonic sensor
import simpleio
from analogio import AnalogIn  # this line imports code for the potentiometer




# some helpful reference code for the ultrasonic sensor
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)   # this sets it up for use


# Code for the potentiometer:
potentiometer = AnalogIn(board.A1)  # potentiometer connected to A1, power & ground
#Setpoint = potentiometer.value  # the input variable for the PID, controlled by the potentiometer

while True:
 
    print("distance: ")
    print(sonar.distance)
    print("Setpoint: ")
    print(potentiometer.value)
    time.sleep(0.25)
    
 


    
    

# SetPoint should equal a mapped version of the potentiometer value
# The range of values in circuitPython for a potentiometer is 0 to 65520


# Use PID algorithm to determine the correct output value for the motor

# We might do an early version of PID, just P value,
# if distance < SetPoint, increase VMotor
# if distance > SetPont, decrease VMotor

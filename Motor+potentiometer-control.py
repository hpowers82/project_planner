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

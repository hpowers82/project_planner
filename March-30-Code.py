import time
import board
import adafruit_hcsr04  # this line imports code for the ultrasonic sensor
import simpleio
from analogio import AnalogIn  # this line imports code for the potentiometer
from analogio import AnalogOut # code for the motor speed/voltage stuff
from lcd.lcd import LCD     # these two lines import code for the lcd
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
#from adafruit_motorkit import MotorKit    # these two lines are for controlling the motor/fan
#kit = MotorKit()

lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)

analog_out = AnalogOut(board.A0) # motor control pin

# some helpful reference code for the ultrasonic sensor
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)   # this sets it up for use



# Code for the potentiometer:
potentiometer = AnalogIn(board.A1)  # potentiometer connected to A1, power & ground



while True:
    Setpoint = potentiometer.value  # the input variable for the PID, controlled by the potentiometer
    Setpoint = simpleio.map_range(Setpoint,0,65520,0,30)
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print('Setpoint: ' + str(Setpoint))
    lcd.set_cursor_pos(1,0)
    try:
        lcd.print('Distance: ' + str(sonar.distance))
    except RuntimeError:
        lcd.print('Retrying!')
    analog_out.value = potentiometer.value  # sets the potentiometer value as the imput for how fast the motor spins
    time.sleep(.1)


    
    

# SetPoint should equal a mapped version of the potentiometer value
# The range of values in circuitPython for a potentiometer is 0 to 65520


# Use PID algorithm to determine the correct output value for the motor

# We might do an early version of PID, just P value,
# if distance < SetPoint, increase VMotor
# if distance > SetPont, decrease VMotor

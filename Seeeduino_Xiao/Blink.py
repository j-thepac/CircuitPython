import time
import board
from digitalio import DigitalInOut,Direction


led = DigitalInOut(board.D13) #D13 is a built in LED

#A1 - A10 can be used as well if u use a separate LED and a Resistor 100 - 400 ohms refer below for calculations
led.direction=Direction.OUTPUT

while True:
    led.value = True
    time.sleep(1)
    led.value=False
    time.sleep(1)

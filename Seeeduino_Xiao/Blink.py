
#-----------
#A1 - A10 can be used as well if u use a separate LED and a Resistor 100 - 400 ohms refer below for calculations
import time
import board
from digitalio import DigitalInOut,Direction

led = DigitalInOut(board.D13) #A1
led.direction=Direction.OUTPUT

led_2 = DigitalInOut(board.A1) #A1
led_2.direction=Direction.OUTPUT

while True:
    led.value = True
    led_2.value = True
    time.sleep(1)

    led.value=False
    led_2.value=False
    time.sleep(1)



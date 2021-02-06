import os
import board
from digitalio import DigitalInOut, Direction
import time
import touchio

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT
 
touches = []
for p in (board.CAP1, board.CAP2, board.CAP3):
    touches.append(touchio.TouchIn(p))
 
leds = []
for p in (board.LED5, board.LED6, board.LED7):
    led = DigitalInOut(p)
    led.direction = Direction.OUTPUT
    leds.append(led)
    led.value = False
 
cap_touches = [False, False, False]
 
def read_caps():
    cap_touches[0] = touches[0].raw_value > 3000
    cap_touches[1] = touches[1].raw_value > 3000
    cap_touches[2] = touches[2].raw_value > 3000
    return cap_touches
 
while True:
    caps = read_caps()
    print(caps)
    for i,c in enumerate(caps):leds[i].value = c
    time.sleep(0.1)
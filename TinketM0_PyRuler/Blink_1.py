import board
import digitalio
import time

caps=[board.CAP0,board.CAP1,board.CAP2,board.CAP3]
leds=[board.LED4,board.LED5,board.LED6,board.LED7]
main_led=board.D13


temp=1
led = digitalio.DigitalInOut(leds[temp])
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)




	

#RUn all Leds 

import board
import digitalio
import time

caps=[board.CAP0,board.CAP1,board.CAP2,board.CAP3]

led1=digitalio.DigitalInOut(board.LED4)
led1.direction = digitalio.Direction.OUTPUT

led2=digitalio.DigitalInOut(board.LED5)
led2.direction = digitalio.Direction.OUTPUT

led3=digitalio.DigitalInOut(board.LED6)
led3.direction = digitalio.Direction.OUTPUT

led4=digitalio.DigitalInOut(board.LED7)
led4.direction = digitalio.Direction.OUTPUT

main_led=digitalio.DigitalInOut(board.D13)
main_led.direction = digitalio.Direction.OUTPUT

leds=[main_led,led1,led2,led3,led4]

def led_on(led):
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)

num=0
while True:
    led_on(leds[num])
    if (num==4):num=0
    else:num=num+1

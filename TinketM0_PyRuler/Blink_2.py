import board
import digitalio
import time

caps=[board.CAP0,board.CAP1,board.CAP2,board.CAP3]
leds=[board.LED4,board.LED5,board.LED6,board.LED7]
main_led=board.D13

num=4
while True:
    led_no(board.LED+num)
    if (num==7):num=4
    else:num=num+1


def led_on(led_obj):
    leds=[board.LED4,board.LED5,board.LED6,board.LED7]
    led = digitalio.DigitalInOut(led_obj)
    led.direction = digitalio.Direction.OUTPUT

    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)




	

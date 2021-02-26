import machine
import ssd1306
import time

#Pin11 -GP8 - SDA
#Pin12 -GP9-SCL
oled = ssd1306.SSD1306_I2C(128, 64, machine.I2C(0))#width,height,protocol,address

oled.text("Hello everyone", 0, 0)
oled.show()
time.sleep(2)
oled.text("Welcome to my", 0, 10)
oled.text("channel", 0, 20)
oled.show()
time.sleep(2)
oled.text("Thank You", 0, 30)
oled.show()
